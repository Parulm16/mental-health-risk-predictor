%matplotlib inline:
This is a Jupyter magic command.
It tells Jupyter to render matplotlib plots inside the notebook itself (instead of opening a new window).
Without this, your plots might not show up inline after plt.plot() or sns.histplot()
-----------------------------------------------------

sns.set_context("talk"):
This is a Seaborn styling function.
It adjusts the scale of labels, fonts, and lines depending on your intended output:
"paper" → small (for publications)
"notebook" → default (balanced for interactive work)
"talk" → larger fonts/lines (good for presentations)
"poster" → very large (for posters/conference slides)
So sns.set_context("talk") makes your plots easier to read and present — bigger labels, clearer visuals.
-----------------------------------------------------



