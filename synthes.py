import sounddevice as sd
import time
import torch

language = 'ru'
model_id = 'en_v4'
sample_rate = 48000
speaker = 'kseniya'
put_accent = True
put_yoo = True
device = torch.device('cpu')

model, _= torch.hub.load(repo_or_dir='snakers4/silero-models',
                                       model='silero_tts',
                                       language=language,
                                       speaker=model_id)
model.to(device)

def tts(text):
    audio = model.apply_tts(text=text,
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent)

    sd.play(audio, sample_rate)
    time.sleep( len(audio) / sample_rate )
    sd.stop()
