from scipy.io import wavfile
fs, data = wavfile.read('string_1.wav')

data.shape

from pyramid.arima import auto_arima
