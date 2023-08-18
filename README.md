# batch-media-converter-python

you can modify the script to create a subfolder named `download_mp3` inside the current working directory and save the converted MP3 files there. Here's how you can do it:

```python
from moviepy.editor import VideoFileClip
import os

def convert_to_mp3(input_file, output_file):
    video = VideoFileClip(input_file)
    audio = video.audio
    audio.write_audiofile(output_file)
    audio.close()

def batch_convert(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".mp4"):
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + ".mp3"
            output_path = os.path.join(output_folder, output_filename)
            print(f"Converting {filename} to {output_filename}")
            convert_to_mp3(input_path, output_path)

if __name__ == "__main__":
    input_folder = "input_folder_path"  # Replace with the path to your input folder containing MP4 files
    output_folder = os.path.join(os.getcwd(), "download_mp3")
    batch_convert(input_folder, output_folder)
```

In this script, `output_folder` is set to a subfolder named `download_mp3` inside the current working directory. You don't need to specify an absolute path for the output folder; the script will create the subfolder within the current working directory. Make sure to replace `"input_folder_path"` with the actual path to your input folder containing the MP4 files.

Save the modified script to a `.py` file and then run it using your Python interpreter. It will convert the MP4 files in the input folder and save the converted MP3 files in the `download_mp3` subfolder within the current working directory.
