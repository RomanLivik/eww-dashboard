# Minimalist black and white eww dashboard

## Features 
* Mini player
* CMatrix effect
* Time widget
* Fast access to your apps
* Quick analysis of CPU usage, RAM, and ROM

## Requirements

To ensure everything displays and functions correctly, install the following:
* Eww (Wayland version): eww-wayland
* Fonts: JetBrainsMono Nerd Font (Critical for icons)
* Media Controls: playerctl (for the music player tile)

## Structure of project
```
~/.config/eww/
├── eww.yuck         # Layout and logic
├── eww.scss         # Styling
└── scripts/
    └── matrix.sh    # Matrix animation logic
```

## Screenshot
<img width="1918" height="1078" alt="изображение" src="https://github.com/user-attachments/assets/050f98d8-e1c6-4f65-aa4d-a899f8386900" />

## Installation
```
git clone https://github.com/RomanLivik/eww-dashboard
cd eww-dashboard
cp eww ~/.config/
```

## Launch
```
eww daemon
eww open dashboard
```
## Configuration for Hyprland

To make the dashboard sit permanently on your desktop background without interfering with windows, the eww.yuck uses :stacking "bottom".

Add this to your hyprland.conf to launch it on startup:
```
exec-once = eww daemon && eww open dashboard
```

## Important Notes
* Encoding: Do not add icons or non-English characters to eww.scss. All icons are handled as text labels within eww.yuck to prevent CSS parser crashes.
* Monochrome Icons: Icons are using Nerd Font symbols. Their color is controlled via the color: #ffffff; property in the SCSS file.
* The widget is set to 1200px width. If you find it too large for your scaling, adjust the :width and :height values in the geometry section of eww.yuck
