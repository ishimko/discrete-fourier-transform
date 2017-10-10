import numpy as np


THRESHOLD = 0.001


def get_amp(x):
    return abs(x)


# TODO: correction
def get_phase(x):
    return - np.arctan2(np.imag(x), np.real(x))


def fft(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]

    if N == 1:
        return x
    elif N % 2 > 0:
        raise ValueError("Size of x must be a power of 2")
    else:
        X_even = fft(x[::2])
        X_odd = fft(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        result = np.concatenate([X_even + factor[:N // 2] * X_odd,
                                 X_even + factor[N // 2:] * X_odd])
        return result


def get_spectrum_from_fft(fft_result, N):
    amplitudes = [get_amp(x)* 2 / N for x in fft_result]
    phases = [get_phase(x)  if amplitudes[i] > THRESHOLD else 0 for i, x in enumerate(fft_result)]
    return list(zip(amplitudes, phases))


def get_fft_spectrum(signal):
    fft_result = fft(signal)
    return get_spectrum_from_fft(fft_result, len(signal))
