

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
    return (plt,)


@app.cell
def _(plt):
    fig, ax = plt.subplots()             # Create a figure containing a single Axes.
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
    plt.show()                           # Show the figure.
    return


if __name__ == "__main__":
    app.run()
