import matplotlib.pyplot as plt

from scipy.io import wavfile as wav
from scipy.fftpack import fft
import numpy as np
rate, data = wav.read('/Users/philhannant/Desktop/Tam200.wav')
fft_out = fft(data)
plt.plot(data, np.abs(fft_out))

plt.show()