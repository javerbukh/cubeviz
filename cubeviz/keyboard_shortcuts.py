from qtpy import QtCore, QtWidgets, QtGui, compat
from qtpy.QtWidgets import QApplication
from glue.config import keybindings
import pyperclip
from tkinter import Tk
# import clipboard
# from .layout import CubeVizLayout
# from glue.config import viewer_tool
# from glue.viewers.common.qt.data_viewer import DataViewer
# from glue.core import Data


@keybindings(QtCore.Qt.Key_1, ["None"])
def get_coordinates(session):
    """
    Cycle through all active windows within the current tab and returns the
    new order of windows to the GlueApplication Session.
    """

    print("Hello from CubeViz!")
    # for idx in range(session.application.tab_count):
    #     if isinstance(session.application.tab(idx), CubeVizLayout):
    #         lay = session.application.tab(idx)
    lay = session.application.current_tab
    for w in lay.views:
        civ = w._widget
        if civ.is_mouse_over:
            civ.statusBar().showMessage("Works")
            coords_status = civ.get_coords()

    if coords_status:
        print(coords_status)
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(coords_status, mode=cb.Clipboard)

@keybindings(QtCore.Qt.Key_2, ["None"])
def toggle_coordinates(session):
    """
    Cycle through all active windows within the current tab and returns the
    new order of windows to the GlueApplication Session.
    """

    print("in toggle function")
    lay = session.application.current_tab
    for w in lay.views:
        civ = w._widget
        if civ.is_mouse_over:
            civ.statusBar().showMessage("Works")
            civ.toggle_hold_coords()
            print(civ.hold_coords)
