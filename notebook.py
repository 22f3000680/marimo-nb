# notebook.py

# 22f3000680@ds.study.iitm.ac.in
# Marimo notebook demonstrating reactive variables, slider widget, and dynamic markdown

import marimo

__generated_with = "0.3.0"
app = marimo.App()


@app.cell
def __():
    import marimo as mo
    return mo,


# Cell 1: Define an interactive slider widget
@app.cell
def __(mo):
    # Slider widget for user to select a number
    slider = mo.ui.slider(start=1, stop=10, step=1, label="Select a number")
    slider
    return slider,


# Cell 2: Compute a square of the selected number
@app.cell
def __(slider):
    # Compute square based on slider value
    selected_value = slider.value
    squared = selected_value ** 2

    # Dependency: This cell depends on the slider widget above
    # Whenever `slider.value` changes, this cell re-computes

    squared
    return selected_value, squared


# Cell 3: Show dynamic markdown output
@app.cell
def __(mo, selected_value, squared):
    # This markdown output is reactive — it updates based on the slider
    mo.md(f"""
    ### Result
    You selected **{selected_value}**

    The square of that number is **{squared}**
    """)
    return
