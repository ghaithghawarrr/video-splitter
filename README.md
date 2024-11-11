# Video Frame Extractor

This Python script extracts frames from a video file within a specified time range, saving them as high-quality PNG images. It uses OpenCV for video processing, allowing precise extraction of frames between a given `start_time` and `end_time` (in seconds).

## Features
- **Time-based Frame Extraction**: Specify `start_time` and `end_time` to extract frames from a precise video segment.
- **Automatic Folder Creation**: Output folder is created automatically if it doesn’t exist.
- **Lossless Quality**: Saves frames as PNG images without compression to preserve the highest quality.
- **Error Handling**: Handles common issues, such as missing files, incorrect time ranges, and issues with writing frames.

## Requirements
- Python 3.6+
- OpenCV library (`cv2`)
  
  Install OpenCV via pip:
  ```bash
  pip install opencv-python
  ```

## Usage
1. **Specify Parameters**: Set the `video_path` to the input video file, `output_folder` to the destination folder, and define `start_time` and `end_time` in seconds.
2. **Run the Script**: Execute the script, and it will save frames from the specified time range into the output folder.

```python
# Example Usage
video_path = "path/to/your/video.mp4"  # Path to your video file
output_folder = "output_frames"        # Folder to save frames
start_time = 10.0                      # Start time in seconds
end_time = 20.0                        # End time in seconds

extract_frames(video_path, output_folder, start_time, end_time)
```

## Function Details

```python
def extract_frames(video_path: str, output_folder: str, start_time: float, end_time: float) -> None:
```
- **Parameters**:
  - `video_path`: Path to the input video file.
  - `output_folder`: Directory to save the extracted frames.
  - `start_time`: Start time for extraction in seconds.
  - `end_time`: End time for extraction in seconds.

The script includes comprehensive error handling:
- **File Errors**: Ensures the video file exists and is accessible.
- **Time Validation**: Validates that start and end times are within the video duration and are correctly ordered.
- **Frame Writing**: Checks if frames are written successfully to the output folder.

## Example Output
Upon completion, extracted frames are saved in the specified output folder with filenames like:
```
output_frames/frame_0001.png
output_frames/frame_0002.png
...
```
