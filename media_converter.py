from moviepy.editor import VideoFileClip

def convert_to_mp3(input_file, output_file):
    video = VideoFileClip(input_file)
    audio = video.audio
    audio.write_audiofile(output_file)
    audio.close()

def batch_convert(input_folder, output_folder):
    import os

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
    input_folder = "downloads/"  # Replace with the path to your input folder containing MP4 files
    output_folder = "mp3_convert/"  # Replace with the path to your output folder for MP3 files
    batch_convert(input_folder, output_folder)
