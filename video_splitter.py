import cv2
import os

def extract_frames(video_path: str, output_folder: str, start_time: float, end_time: float) -> None:
    """
    Extracts frames from a video file between a specified start and end time and saves them as PNG images.

    Parameters:
    - video_path (str): Path to the input video file.
    - output_folder (str): Directory where the extracted frames will be saved.
    - start_time (float): Start time in seconds for frame extraction.
    - end_time (float): End time in seconds for frame extraction.
    """
    try:
        # Check if video file exists
        if not os.path.isfile(video_path):
            raise FileNotFoundError(f"The video file '{video_path}' does not exist.")

        # Ensure the output folder exists
        os.makedirs(output_folder, exist_ok=True)
        
        # Open the video file
        video = cv2.VideoCapture(video_path)
        
        # Check if the video file was opened successfully
        if not video.isOpened():
            raise ValueError("Error opening video file. Please check the video path and format.")

        # Get the video's frames per second (fps) to calculate frame positions
        fps = video.get(cv2.CAP_PROP_FPS)
        total_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
        video_duration = total_frames / fps

        # Validate start and end times
        if start_time < 0 or end_time < 0:
            raise ValueError("Start and end times must be non-negative.")
        if start_time >= end_time:
            raise ValueError("Start time must be less than end time.")
        if start_time > video_duration or end_time > video_duration:
            raise ValueError(f"Specified time range exceeds video length of {video_duration:.2f} seconds.")

        # Calculate starting and ending frames based on time and fps
        start_frame = int(start_time * fps)
        end_frame = int(end_time * fps)

        # Set the starting frame
        video.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
        
        # Start extracting frames within the specified time range
        success, frame = video.read()
        frame_count = start_frame  # Track the current frame number for naming
        
        while success and frame_count <= end_frame:
            # Generate frame filename
            frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.png")
            
            # Save the frame as a PNG image with no compression for high quality
            if not cv2.imwrite(frame_filename, frame, [cv2.IMWRITE_PNG_COMPRESSION, 0]):
                raise IOError(f"Could not write frame {frame_count} to file '{frame_filename}'.")
            
            # Read the next frame and increment the frame count
            success, frame = video.read()
            frame_count += 1
        
        # Release the video capture object
        video.release()
        print(f"Extracted frames from {start_time}s to {end_time}s to '{output_folder}'.")

    except FileNotFoundError as e:
        print(f"File Error: {e}")
    except ValueError as e:
        print(f"Value Error: {e}")
    except IOError as e:
        print(f"I/O Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if 'video' in locals() and video.isOpened():
            video.release()

# Example usage
if __name__ == "__main__":
    video_path = "video.mp4"  # Update with your video file path
    output_folder = "output"   # Update with your desired output folder
    start_time = 10.0  # Start time in seconds
    end_time = 20.0    # End time in seconds
    extract_frames(video_path, output_folder, start_time, end_time)
