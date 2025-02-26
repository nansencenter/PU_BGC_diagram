"""
Taylor diagram (Taylor, 2001) implementation with normalized standard deviation.
"""

import numpy as np
import matplotlib.pyplot as plt

class TaylorDiagram:
    """
    Taylor diagram with normalized standard deviation.
    """

    def __init__(self, refstd, fig=None, rect=111, label='Reference', srange=(0.0, 1.6)):
        """
        Initializes the Taylor diagram axes.
        """

        from matplotlib.projections import PolarAxes
        import mpl_toolkits.axisartist.floating_axes as FA
        import mpl_toolkits.axisartist.grid_finder as GF

        self.refstd = refstd
        self.tmax = np.pi / 2

        rlocs = np.array([0, 0.2, 0.4, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99, 1])
        tlocs = np.arccos(rlocs)
        gl1 = GF.FixedLocator(tlocs)
        tf1 = GF.DictFormatter(dict(zip(tlocs, map(str, rlocs))))

        self.smin = srange[0]
        self.smax = srange[1]

        # Standard deviation axis ticks (modified)
        slocs = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6])
        gl2 = GF.FixedLocator(slocs)
        tf2 = GF.DictFormatter(dict(zip(slocs, map(str, slocs))))

        ghelper = FA.GridHelperCurveLinear(
            PolarAxes.PolarTransform(),
            extremes=(0, self.tmax, self.smin, self.smax),
            grid_locator1=gl1, tick_formatter1=tf1,
            grid_locator2=gl2, tick_formatter2=tf2)

        if fig is None:
            fig = plt.figure()

        ax = FA.FloatingSubplot(fig, rect, grid_helper=ghelper)
        fig.add_subplot(ax)

        ax.axis["top"].set_axis_direction("bottom")
        ax.axis["top"].toggle(ticklabels=True, label=True)
        ax.axis["top"].major_ticklabels.set_axis_direction("top")
        ax.axis["top"].label.set_axis_direction("top")
        ax.axis["top"].label.set_text("Correlation")

        ax.axis["left"].set_axis_direction("bottom")
        ax.axis["left"].label.set_text("Normalized Standard deviation")

        ax.axis["right"].set_axis_direction("top")
        ax.axis["right"].toggle(ticklabels=True)
        ax.axis["right"].major_ticklabels.set_axis_direction("left")

        ax.axis["bottom"].set_visible(False)

        self._ax = ax
        self.ax = ax.get_aux_axes(PolarAxes.PolarTransform())

        self.ax.plot([0], 1, 'ko', ls='', ms=10, label=label, fillstyle='none')
        t = np.linspace(0, self.tmax)
        r = np.ones_like(t)
        self.ax.plot(t, r, 'k--')

        self.samplePoints = []

    def add_sample(self, stddev, corrcoef, *args, **kwargs):
        """Adds a sample with normalized stddev."""
        if corrcoef >= 0:
            normalized_stddev = stddev / self.refstd
            line, = self.ax.plot(np.arccos(corrcoef), normalized_stddev, *args, **kwargs)
            self.samplePoints.append(line)
            return line
        return None

    def add_grid(self, *args, **kwargs):
        """Adds a grid."""
        self._ax.grid(*args, **kwargs)

    def add_contours(self, levels=5, **kwargs):
        """Adds RMS difference contours."""
        rs, ts = np.meshgrid(np.linspace(self.smin, self.smax),
                             np.linspace(0, self.tmax))
        rms = np.sqrt(1 + rs**2 - 2 * rs * np.cos(ts))
        contours = self.ax.contour(ts, rs, rms, levels, **kwargs)
        return contours

def sample():
    """Example usage."""
    stdref = 48.491
    stats = [
        [25.939, 0.385, "ARC NWS"], [29.593, 0.509, "ARC SPG"],
        [33.125, 0.585, "MED EAST"], [35.807, 0.609, "MED WEST"]
    ]

    fig = plt.figure()
    dia = TaylorDiagram(stdref, fig=fig, label='Reference')
    ref_line = dia.ax.plot([0], 1, 'ko', ls='', ms=10, label='Reference', fillstyle='none')[0]
    dia.samplePoints.append(ref_line)
    dia.samplePoints[0].set_color('r')

    for i, (stddev, corrcoef, name) in enumerate(stats):
        dia.add_sample(stddev, corrcoef, marker=f'${i+1}$', ms=10, ls='',
                       mfc='k', mec='k', label=name)

    contours = dia.add_contours(levels=5, colors='0.5')
    plt.clabel(contours, inline=1, fontsize=10, fmt='%.0f')

    dia.add_grid()
    dia._ax.axis[:].major_ticks.set_tick_out(True)

    fig.legend(dia.samplePoints,
               [p.get_label() for p in dia.samplePoints],
               numpoints=1, prop=dict(size='small'), loc='upper right')
    fig.suptitle("Nitrate 400m", size='x-large')

    return dia

if __name__ == '__main__':
    dia = sample()
    plt.show()
