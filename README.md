# Audio Cutter

This project provides a Python script for processing audio content.

## Project Overview

The `extractAudioFromVideoRemoveSilenceAndChunkIt.py` file consists of functionalities that allow for conversion of
video files to audio, removal of silence from the audio file and segmenting the processed audio into chunks.

## Features

1. **Video to Audio Conversion**: Converts a video file into an audio file using the `extract_audio_from_video()`.
2. **Remove Silence from an Audio File**: Removes the silent durations from the processed audio file using
   the `remove_silence(audio_file, min_silence_len=1000, silence_thresh=-50)` function.
3. **Chunk the Audio**: Divides the resulting audio clip into chunks of a defined length using the `extract_to_chunks()`
   function.

## Getting Started

Make sure you have ffmpeg.exe installed on your system. You can download it
from [here](https://www.ffmpeg.org/download.html).

Just add the file you want to extract audio from in the videoInput folder and run the script. The audio file will be
saved in the audioOutput folder.

## Contributing

Just fork the repository and make a pull request. We will review it and merge it if it is good.