import os
from pydub import AudioSegment

data_path = os.path.dirname(os.path.abspath(__file__))
folders = [os.path.join(data_path, name) for name in os.listdir(data_path)
           if os.path.isdir(os.path.join(data_path, name))]
audio_files = [os.path.join(data_path, folder, file) for folder in folders for file in os.listdir(folder)
               if not file.endswith('.json')]

for audio_file in audio_files:
    sound = AudioSegment.from_mp3(audio_file)
    sound.export(audio_file.replace('mp3', 'wav'), format="wav")
    print(audio_file)
