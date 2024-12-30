import torch
import librosa
import io
from transformers import pipeline

def convert raw_bytes_to_array(audiobytes):
  audio_bytes=io.BytesIO(audiobytes)
  audio_array=librosa.load(audio_bytes)
  return audio_array

def transcribe_audio(audiobytes):
  device="cuda:0" if torch.cuda.is_available() else "cpu"
  pipe=pipeline(
    task="automatic-speech-recognition",
    model="openai/wisper-small",
    chunk_length_s=30
    device=device
  )
  audioArray=raw_bytes_to_array(audiobytes)
  prediction=pipe(aduioArray,batch_size=1)["text"]
  return prediction
