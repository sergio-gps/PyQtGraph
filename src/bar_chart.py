import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np

win = pg.plot()
win.setWindowTitle('pyqtgraph example: BarGraphItem')

X = np.arange(15)
Y1 = np.sin(X)
Y2 = 1.1 * np.sin(X+1)
Y3 = 1.2 * np.sin(X+2)

bg1 = pg.BarGraphItem(x=X, height=Y1, width=0.3, brush='r')
bg2 = pg.BarGraphItem(x=X+0.33, height=Y2, width=0.3, brush='g')
bg3 = pg.BarGraphItem(x=X+0.66, height=Y3, width=0.3, brush='b')

win.addItem(bg1)
win.addItem(bg2)
win.addItem(bg3)


# Final example shows how to handle mouse clicks:
class BarGraph(pg.BarGraphItem):
    def mouseClickEvent(self, event):
        print("clicked")


bg = BarGraph(x=X, y=Y1*0.3, height=0.4+Y1*0.2, width=0.1)
win.addItem(bg)

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()