

import marimo

__generated_with = "0.13.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""# Simple Marimo demonstration""")
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt

    fs=1e3
    num_of_samples=512

    # Define time array
    samples=np.arange(num_of_samples)
    t=(1/fs)*samples
    return np, num_of_samples, plt, t


@app.cell
def _(mo):
    # Define frequency as adjustable value
    frequency = mo.ui.slider(10, 700, value=10, step=10, label='frequency')

    mo.md(
        f"""
        **Set signal frequency.**

        {frequency}
        """
    )
    return (frequency,)


@app.cell
def _(frequency, np, num_of_samples, t):
    # Define complex signal1: sin 50Hz, amplitude=5, imag part is zero
    sig1=np.zeros(num_of_samples, dtype=complex)
    sig1.real=5*np.sin(2*np.pi*frequency.value*t)
    return (sig1,)


@app.cell
def _(plt, sig1):
    fig1,ax1 = plt.subplots()
    ax1.plot(sig1.real)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Signal Spectrum

        Based on [this link](https://docs.marimo.io/guides/working_with_data/plotting/#marimo.ui.altair_chart.apply_selection) following below needs to be added for `matplotlib` plots to make them interactive.
        """
    )
    return


@app.cell
def _(mo, np, plt, sig1):
    sig1_spectr=np.fft.fft(sig1)
    plt.plot(np.absolute(sig1_spectr))

    # plt.gcf() gets the current figure
    mo.mpl.interactive(plt.gcf())
    return


if __name__ == "__main__":
    app.run()
