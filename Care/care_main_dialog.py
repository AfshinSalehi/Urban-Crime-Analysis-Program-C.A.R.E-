# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CareDialog
                                 A QGIS plugin
 Crime analysis using radial effectiveness
                             -------------------
        begin                : 2017-09-17
        git sha              : $Format:%H$
        copyright            : (C) 2017 by Afshin Salehi
        email                : Salehi@consultant.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
import sys
from PyQt4 import QtGui, uic
sys.path.append(os.path.dirname(__file__))

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'care_main_dialog_base.ui'))


class CareDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(CareDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
