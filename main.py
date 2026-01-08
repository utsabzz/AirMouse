import flet as ft
import cv2
import mediapipe as mp
import pyautogui
import threading
import time
import math
import webbrowser

pyautogui.FAILSAFE = False

settings = {
    "smooth_factor": 0.4,
    "pinch_threshold": 25,
    "click_cooldown": 0.5,
    "right_click_hold": 2.0,
    "frame_margin": 150,
    "running": False
}

def air_mouse_loop():
    try:
        screen_width, screen_height = pyautogui.size()

        hand_tracker = mp.solutions.hands
        hands = hand_tracker.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        camera = cv2.VideoCapture(0)
        
        if not camera.isOpened():
            print("Cannot access the camera")
            settings["running"] = False
            return

        previous_x, previous_y = 0, 0
        last_click_time = 0
        pinch_start_time = None
        right_click_done = False

        palm_points = [0, 5, 9, 13, 17]

        while settings["running"]:
            success, frame = camera.read()
            if not success:
                break

            frame = cv2.flip(frame, 1)
            height, width, _ = frame.shape
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            hand_results = hands.process(rgb_frame)

            if hand_results.multi_hand_landmarks:
                hand = hand_results.multi_hand_landmarks[0]

                palm_center_x = sum(hand.landmark[i].x for i in palm_points) / 5
                palm_center_y = sum(hand.landmark[i].y for i in palm_points) / 5

                pixel_x = int(palm_center_x * width)
                pixel_y = int(palm_center_y * height)

                margin = settings["frame_margin"]
                pixel_x = max(margin, min(pixel_x, width - margin))
                pixel_y = max(margin, min(pixel_y, height - margin))

                normalized_x = (pixel_x - margin) / (width - 2 * margin)
                normalized_y = (pixel_y - margin) / (height - 2 * margin)

                target_x = normalized_x * screen_width
                target_y = normalized_y * screen_height

                smoothing = settings["smooth_factor"]
                current_x = previous_x + (target_x - previous_x) * smoothing
                current_y = previous_y + (target_y - previous_y) * smoothing

                pyautogui.moveTo(current_x, current_y)
                previous_x, previous_y = current_x, current_y

                index_x = int(hand.landmark[8].x * width)
                index_y = int(hand.landmark[8].y * height)
                thumb_x = int(hand.landmark[4].x * width)
                thumb_y = int(hand.landmark[4].y * height)

                distance = math.hypot(index_x - thumb_x, index_y - thumb_y)
                current_time = time.time()

                if distance < settings["pinch_threshold"]:
                    if pinch_start_time is None:
                        pinch_start_time = current_time
                        right_click_done = False

                    if (current_time - pinch_start_time >= settings["right_click_hold"]
                        and not right_click_done
                        and current_time - last_click_time > settings["click_cooldown"]):
                        pyautogui.rightClick()
                        last_click_time = current_time
                        right_click_done = True
                else:
                    if pinch_start_time and not right_click_done:
                        if current_time - last_click_time > settings["click_cooldown"]:
                            pyautogui.click()
                            last_click_time = current_time

                    pinch_start_time = None
                    right_click_done = False

        camera.release()
        cv2.destroyAllWindows()
        
    except Exception as error:
        print(f"Problem with camera tracking: {error}")
        settings["running"] = False

def main(page):
    page.title = "Air Mouse Controller"
    page.window_width = 420
    page.window_height = 520
    page.window_resizable = False
    page.theme_mode = "dark"

    mouse_thread = None
    status_message = ft.Text("Ready to start", size=14, color="green")

    def update_status(message, color="green"):
        status_message.value = message
        status_message.color = color
        page.update()

    def toggle_mouse_control(event):
        nonlocal mouse_thread
        
        if not settings["running"]:
            settings["running"] = True
            control_button.text = "Stop Control"
            update_status("Starting hand tracking...", "orange")
            
            try:
                mouse_thread = threading.Thread(target=air_mouse_loop, daemon=True)
                mouse_thread.start()
                update_status("Active - Show your hand to the camera", "green")
            except Exception as problem:
                update_status(f"Failed to start: {str(problem)}", "red")
                settings["running"] = False
                control_button.text = "Start Control"
        else:
            settings["running"] = False
            control_button.text = "Start Control"
            update_status("Hand tracking stopped", "grey")
            
            if mouse_thread and mouse_thread.is_alive():
                time.sleep(0.5)

        page.update()

    def open_github(event):
        webbrowser.open("https://github.com/utsabzz")

    control_button = ft.Button(
        "Start Control",
        on_click=toggle_mouse_control,
        width=200,
        height=80,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=15),
            padding=20
        )
    )

    github_button = ft.TextButton(
        "GitHub: utsabzz",
        on_click=open_github,
        icon="code",
        tooltip="Visit my GitHub profile"
    )

    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("Air Mouse Hand Controller", 
                           size=28, 
                           weight="bold"),
                    
                    ft.Divider(height=1),
                    
                    ft.Container(
                        content=status_message,
                        padding=10
                    ),
                    
                    ft.Container(
                        content=ft.Column(
                            [
                                control_button,
                                ft.Text("Press to begin or stop hand control", 
                                       size=14, 
                                       color="grey")
                            ],
                            horizontal_alignment="center",
                            spacing=15
                        ),
                        padding=10
                    ),
                    
                    ft.Container(height=20),
                    
                    ft.Container(
                        content=ft.Column([
                            ft.Text("How to Use:", 
                                   weight="bold", 
                                   size=18),
                            ft.Text("1. Position your hand in front of your webcam", size=14),
                            ft.Text("2. Move your palm to control the mouse cursor", size=14),
                            ft.Text("3. Bring thumb and index finger together for left click", size=14),
                            ft.Text("4. Hold pinch for 2 seconds for right click", size=14),
                            ft.Text("5. Brief pause between each click", size=14),
                            ft.Text("Important: Ensure camera is not being used by other apps", 
                                   size=12, 
                                   color="orange",
                                   weight="bold"),
                            ft.Text("Tip: Works best with good lighting conditions", 
                                   size=12, 
                                   color="orange"),
                        ], spacing=10),
                        padding=20,
                        border=ft.border.all(1, "#555555"),
                        border_radius=15,
                        margin=10
                    ),
                    
                    ft.Container(
                        content=github_button,
                        padding=ft.padding.only(bottom=20)
                    )
                ],
                spacing=10,
                horizontal_alignment="center"
            )
        )
    )

ft.run(main)