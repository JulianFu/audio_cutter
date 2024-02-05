from moviepy.editor import VideoFileClip, AudioFileClip
from pydub import AudioSegment, silence
import os

# Konvertiert Video zu Audio
video_pre_path = 'videoInput/'
video_name = ''  # hier input Datei Filename eintragen
video_path = video_pre_path + video_name
audio_path = 'AUDIO_' + video_name + '.mp3'
output_audio_path = 'audio_no_silence' + audio_path


# Entfernt Stille aus der Audiodatei
def remove_silence(audio_file, min_silence_len=1000, silence_thresh=-50):
    print(f"Entferne Stille aus '{audio_file}'...")
    """ Entfernt Stille aus einer Audio-Datei """
    # sound = AudioSegment.from_file(audio_file, format="mp3")
    sound = AudioSegment.from_mp3(audio_file)
    print("Starte split_on_silence...")
    non_silent_chunks = silence.split_on_silence(sound, min_silence_len=min_silence_len, silence_thresh=silence_thresh)

    print("Starte combine...")
    # Kombiniert die nicht stillen Teile wieder
    combined = non_silent_chunks[0]
    for chunk in non_silent_chunks[1:]:
        combined += chunk

    return combined


def extract_audio_from_video():
    global audio, output_audio_path
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path, ffmpeg_params=["-ac", "1"])


def remove_silence_if_audio_exists():
    # Entfernt Stille aus der Audiodatei
    if os.path.exists(audio_path):
        edited_audio = remove_silence(audio_path)

        with open(output_audio_path, 'wb') as output_file:
            edited_audio.export(output_file, format="mp3")
            print(f"Audio ohne Stille wurde erfolgreich nach '{output_audio_path}' gespeichert.")
    else:
        print(f"Datei nicht gefunden: {audio_path}")


# Teilt die Audiodatei in Chunks von 10 Minuten auf
def extract_to_chunks():
    print(f"Teile Audio in Chunks von 10 Minuten auf...")
    audio_without_silence = AudioFileClip(output_audio_path)
    audio_duration = audio_without_silence.duration

    audio_path_for_chunks = 'audio_chunks_' + audio_path

    # Erstellen des Verzeichnisses für Audio-Chunks, falls es nicht existiert
    if not os.path.exists(audio_path_for_chunks):
        os.makedirs(audio_path_for_chunks)
    # 600 für 10 Minuten
    for i in range(0, int(audio_duration), 600):
        end_time = min(i + 600, audio_duration)  # Verhindert, dass der letzte Chunk über das Ende des Audios hinausgeht
        audio_chunk = audio_without_silence.subclip(i, end_time)
        current_audio_file_name = f'audio_chunk_{i}.mp3'

        audio_chunk.write_audiofile(audio_path_for_chunks + '/' + current_audio_file_name)
        print(f"Audio Chunk {i} wurde erfolgreich extrahiert.")
    print(f"Audio wurde erfolgreich nach '{audio_path_for_chunks}' extrahiert.")


# ab hier die aurufe
extract_audio_from_video()
remove_silence_if_audio_exists()
# if you want to chunk the audio file, uncomment the following line
# extract_to_chunks()
