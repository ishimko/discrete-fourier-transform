from matplotlib import pyplot as plt


SPECTRUMS_COLORS = ['b', 'g', 'r', 'c']

class Drawer:
    def __init__(self, *args, **kwargs):
        self.fig_num = 0

    def plot_values(self, signal_values):
        return list(zip(*enumerate(signal_values)))

    def draw_signal_comparison(self, signals, spectrums, labels):
        assert len(signals) == len(labels)
        plt.subplots_adjust(bottom=0.25)

        plt.figure(self.fig_num)
        plt.subplot(1, 3, 1)
        lines = []
        for signal_values in signals:
            x_points, y_points = self.plot_values(signal_values)
            line, = plt.plot(x_points, y_points)
            lines.append(line)

        for i, spectrum in enumerate(spectrums):
            amps, phases = zip(*spectrum)
            axes = plt.subplot(1, 3, 2)
            line_format = SPECTRUMS_COLORS[i % len(SPECTRUMS_COLORS)]
            self.draw_amplitudes(amps, line_format)

            axes = plt.subplot(1, 3, 3)
            axes.stem(*self.plot_values(phases), linefmt=line_format, markerfmt=' ', basefmt=' ')

        plt.figlegend(lines, labels, loc='lower center')
        self.fig_num += 1
    
    def draw_filtered(self, *signals):
        plt.figure()
        length = len(signals)
        for i, signal_info in enumerate(signals):
            values, spectrum = signal_info
            amps, _ = zip(*spectrum)
            plt.subplot(2, length, i + 1)
            plt.plot(*self.plot_values(values))
            plt.subplot(2, length, i+1 + length)
            self.draw_amplitudes(amps)
    
    def draw_amplitudes(self, amplitudes, linefmt='b'):
        plt.stem(*self.plot_values(amplitudes), linefmt=linefmt, markerfmt=' ', basefmt=' ')

    def show(self):
        plt.show()
