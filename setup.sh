#!/bin/bash

# Update package list and install Xvfb
apt-get update
apt-get install -y xvfb

# Start Xvfb with display :99
Xvfb :99 -screen 0 1024x768x24 &

# Export DISPLAY variable to use the virtual display
export DISPLAY=:99

# Run the main Python script
python main.py
