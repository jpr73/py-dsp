

import marimo

__generated_with = "0.13.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
        # Matplotlib Learn
        Based on [Quick Start Guide](https://matplotlib.org/stable/users/explain/quick_start.html#a-simple-example).
        """
    )
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    import numpy as np
    return np, plt


@app.cell
def _(plt):
    fig, ax = plt.subplots()             # Create a figure containing a single Axes.
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
    plt.show()                           # Show the figure.
    return


@app.cell
def _(mo, np, plt):
    x = np.linspace(0, 2, 100)  # Sample data.

    # Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
    fig2, ax2 = plt.subplots(figsize=(5, 2.7), layout='constrained')
    ax2.plot(x, x, label='linear')  # Plot some data on the Axes.
    ax2.plot(x, x**2, label='quadratic')  # Plot more data on the Axes...
    ax2.plot(x, x**3, label='cubic')  # ... and some more.
    ax2.set_xlabel('x label')  # Add an x-label to the Axes.
    ax2.set_ylabel('y label')  # Add a y-label to the Axes.
    ax2.set_title("Simple Plot")  # Add a title to the Axes.
    ax2.legend()  # Add a legend.

    # Make the figure interactive
    mo.mpl.interactive(plt.gcf())
    return


if __name__ == "__main__":
    app.run()
