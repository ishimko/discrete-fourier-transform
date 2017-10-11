from math import cos, pi

from drawer import Drawer
from helper import randoms_from
from signals import fourier_spectrum, restore_signal, polyharmonic_signal, filter_signal

from fft import get_fft_spectrum


N = 64
TEST_SIGNAL = lambda signal_index, N: 10 * cos((2 * pi * signal_index) / N)
TEST_AMPLITUDES = [1, 3, 5, 8, 10, 12, 16]
TEST_PHASES = [pi / 6, pi / 4, pi / 3, pi / 2, 3 * pi / 4, pi]

POLY_COUNT = 30
TEST_SPECTRUM = [(0, 0)] + list(zip(list(randoms_from(TEST_AMPLITUDES, POLY_COUNT)), list(randoms_from(TEST_PHASES, POLY_COUNT))))
LABELS = ['Original signal', 'Restored signal']


def main():
    drawer = Drawer()

    # 2nd task - discrete fourier transform
    original_signal_values = [TEST_SIGNAL(i, N) for i in range(N)]
    spectrum = fourier_spectrum(original_signal_values)
    restored_signal_values = [restore_signal(i, spectrum) for i in range(N)]
    harmonic_signals_values = [original_signal_values, restored_signal_values]

    drawer.draw_signal_comparison(harmonic_signals_values, [spectrum], LABELS)

    # 3rd task - discrete fourier transform of polyharmonic
    test_polyharmonic_signal = lambda signal_index, N: polyharmonic_signal(signal_index, N, len(TEST_SPECTRUM), TEST_SPECTRUM)

    original_poly_signal_values = [test_polyharmonic_signal(i, N) for i in range(N)]
    poly_spectrum = fourier_spectrum(original_poly_signal_values)
    restored_poly_signal_values = [restore_signal(i, poly_spectrum) for i in range(N)]
    polyharmonic_signals_values = [original_poly_signal_values, restored_poly_signal_values]

    drawer.draw_signal_comparison(polyharmonic_signals_values, [poly_spectrum], LABELS)

    # 4th task - fast fourier transform of polyharmonic
    fft_spectrum = get_fft_spectrum(original_poly_signal_values)
    restored_fft_poly_signal_values = [restore_signal(i, fft_spectrum) for i in range(N)]
    fft_signals_values = [original_poly_signal_values, restored_fft_poly_signal_values]

    drawer.draw_signal_comparison(fft_signals_values, [fft_spectrum], LABELS)

    # filter
    original = [test_polyharmonic_signal(i, N) for i in range(N)]
    spectrum = fourier_spectrum(original)
    spectrum_high_filtered = filter_signal(spectrum, lambda x: x < 15)
    high_filtered_signal = [restore_signal(i, spectrum_high_filtered) for i in range(N)]
    spectrum_low_filtered = filter_signal(spectrum, lambda x: x > 15)
    low_filtered_signal = [restore_signal(i, spectrum_low_filtered) for i in range(N)]
    drawer.draw_filtered(
        (original, spectrum),
        (high_filtered_signal, spectrum_high_filtered),
        (low_filtered_signal, spectrum_low_filtered)
    )

    drawer.show()


if __name__ == '__main__':
    main()
