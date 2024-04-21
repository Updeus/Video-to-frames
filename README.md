# Video Frame Extractor

This Python script extracts all frames from a video file and saves them as individual image files. It is useful for tasks that require frame-by-frame analysis of videos, such as video processing, analysis, or machine learning data preparation.

## Features

- Extracts every frame from a video file.
- Saves frames as JPEG images.
- Automatically creates the output directory if it does not exist.

## Dependencies

- Python 3.x
- OpenCV library

## Installation

To use this script, you need to have Python installed on your system. If you don't have Python installed, download and install it from [python.org](https://www.python.org/downloads/).

You will also need the OpenCV library. Install it using pip:

```bash
pip install opencv-python
```

## Usage

1. Clone the repository or download the script to your local machine.
2. Place the video file in a known directory.
3. Open your terminal or command prompt.
4. Navigate to the directory containing the script.
5. Run the script using the following command:

```bash
python VideotoFrames.py --video_path "path_to_your_video.mp4" --output_folder "path_to_output_directory"
```

Replace `"path_to_your_video.mp4"` with the path to your video file and `"path_to_output_directory"` with the path where you want the extracted frames to be saved.

## Example

```bash
python VideotoFrames.py --video_path "C:/Users/updeus/Desktop/testVideo.mp4" --output_folder "C:/Users/updeus/Desktop/Output"
```

This command will extract frames from `testVideo.mp4` and save them to `C:/Users/updeus/Desktop/Output`.

## Troubleshooting

If you encounter errors such as "Could not open video," please check:
- That the path to the video is correct and accessible.
- That the video file is not corrupted and is in a format supported by OpenCV.
- That you have the necessary permissions to read the file and write to the output directory.

For issues with OpenCV not handling video files correctly, ensure that OpenCV is installed with video support by reinstalling it:

```bash
pip uninstall opencv-python
pip install opencv-python
```

## Contributing

Contributions to enhance this script are welcome. Please fork the repository and submit a pull request with your enhancements.

---
