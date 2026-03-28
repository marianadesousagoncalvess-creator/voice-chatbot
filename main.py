import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100
seconds = 5

print("Fale agora...")
audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()

write("audio.wav", fs, audio)
print("Áudio gravado e salvo como audio.wav com sucesso!")