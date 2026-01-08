# AirMouse Hand Controller 🖐️

Control your computer mouse using hand gestures through your webcam. Move your hand to control the cursor, pinch for left click, and hold pinch for right click.

## ✨ Features
- **Hand-controlled cursor**: Move your palm to control the mouse pointer
- **Gesture-based clicks**: Pinch thumb and index finger for left click, hold for right click
- **Smooth tracking**: Configurable smoothing for natural cursor movement
- **Simple interface**: Easy-to-use control panel with clear instructions
- **Cross-platform**: Works on Windows, macOS, and Linux

## 🚀 Quick Start

### Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/utsabzz/air-mouse-controller.git
   cd air-mouse-controller
   ```

2. **Install dependencies**
   ```bash
   pip install flet opencv-python mediapipe pyautogui
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

## 🎮 How to Use
1. Launch the application
2. Click **"Start Control"** to begin hand tracking
3. Position your hand in front of your webcam
4. Move your palm to control the cursor
5. **Left click**: Bring thumb and index finger together briefly
6. **Right click**: Hold thumb and index finger together for 2 seconds
7. Click **"Stop Control"** when finished

### 💡 Tips for Best Results
- Ensure good lighting on your hand
- Keep your hand visible to the camera
- Make deliberate, smooth movements
- Ensure webcam is not being used by other applications

## 📁 Project Structure
```
air-mouse-controller/
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
└── README.md           # This documentation
```

## 🔧 Technical Details
### How It Works
- **MediaPipe** for real-time hand tracking and gesture recognition
- **OpenCV** for webcam video capture and processing
- **PyAutoGUI** for mouse cursor control
- **Flet** for the user interface

### Default Settings
- Cursor smoothing: 0.4
- Pinch detection threshold: 25 pixels
- Click cooldown: 0.5 seconds
- Right click hold time: 2.0 seconds

## 🤝 Usage Policy

### 🆓 Free to Use
**You are free to:**
- Use this software for personal projects
- Modify and adapt the code
- Share it with others
- Use it in educational settings
- Implement in commercial projects

### 🙏 Credits Appreciated
If you use this project, please consider:
- Giving credit to **[utsabzz](https://github.com/utsabzz)**
- Starring the repository ⭐
- Sharing improvements you make
- Letting me know how you're using it!

### Example Attribution
If you use this in your project, a simple attribution like this is appreciated:
```
Hand tracking functionality powered by Air Mouse Controller 
by utsabzz (https://github.com/utsabzz)
```

## ❓ Troubleshooting

### Common Issues
1. **"Cannot access the camera"**
   - Ensure no other application is using the webcam
   - Check camera permissions
   - Try a different USB port if using external webcam

2. **Poor hand tracking**
   - Improve lighting conditions
   - Ensure hand is clearly visible
   - Avoid busy backgrounds

3. **Application runs but cursor doesn't move**
   - Check if hand is being detected
   - Ensure palm is facing the camera
   - Try restarting the application

## 📝 Notes
- All processing happens locally on your computer
- No data is sent to external servers
- Performance depends on your computer's processing power

## 🌟 Support
If you find this project useful:
- ⭐ **Star the repository** on GitHub
- 🐛 **Report issues** if you find bugs
- 💡 **Suggest improvements** or features
- 🔗 **Share with others** who might find it useful

## 👨‍💻 About the Developer
Created by **[utsabzz](https://github.com/utsabzz)** - Passionate about creating accessible technology solutions.

Check out my other projects on GitHub: [github.com/utsabzz](https://github.com/utsabzz)

---

**Enjoy controlling your computer with hand gestures!** If you have any questions or want to share how you're using this project, feel free to reach out!

*Last updated: 8 January 2026*
