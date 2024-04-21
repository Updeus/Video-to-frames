import cv2
import os

def extract_frames(video_path, output_folder):
    # Make sure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Capture the video from the file
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    # Check if video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Loop until the end of the video
    while True:
        ret, frame = cap.read()

        # Break the loop if there are no more frames
        if not ret:
            break

        # Save the frame as an image file
        output_filepath = os.path.join(output_folder, f"frame_{frame_count}.jpg")
        cv2.imwrite(output_filepath, frame)
        print(f"Saved {output_filepath}")
        frame_count += 1

    # When everything done, release the video capture object
    cap.release()
    print("Done! Extracted all frames.")

# Example usage
video_path = 'path_to_your_video.mp4'
output_folder = 'output_frames'
extract_frames(video_path, output_folder)
