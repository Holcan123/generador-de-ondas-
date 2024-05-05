import pyaudio
import numpy as np

frecuencia  = 250  
duracion  = 1
volume = 0.5  

samples_per_second = 44100  # Frecuencia de la onda en Hrz
num_samples = int(duracion  * samples_per_second)

t = np.linspace(0, duracion , num_samples, endpoint=False)
signal = volume * np.sin(2 * np.pi * frecuencia  * t)

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=samples_per_second,
                output=True)

stream.write(signal.astype(np.float32).tobytes())

stream.stop_stream()
stream.close()
p.terminate()

