# -*- coding: utf-8 -*-

"""
***************************************************************************
    DETransformProvider.py
    ---------------------
    Date                 : March 2015
    Copyright            : (C) 2015 by Giovanni Manghi
    Email                : giovanni dot manghi at naturalgis dot pt
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Giovanni Manghi'
__date__ = 'March 2015'
__copyright__ = '(C) 2015, Giovanni Manghi'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os

from PyQt4.QtGui import *

from processing.core.AlgorithmProvider import AlgorithmProvider
from processing.core.ProcessingConfig import Setting, ProcessingConfig
from processing.tools import system

from ntv2_transformations.VectorGK3ETRS8932NDirInv import VectorGK3ETRS8932NDirInv
from ntv2_transformations.RasterGK3ETRS8932NDirInv import RasterGK3ETRS8932NDirInv


class DETransformProvider(AlgorithmProvider):

    def __init__(self):
        AlgorithmProvider.__init__(self)

        self.activate = False

        self.alglist = [VectorGK3ETRS8932NDirInv(),
                        RasterGK3ETRS8932NDirInv()
                       ]
        for alg in self.alglist:
            alg.provider = self

    def initializeSettings(self):
        AlgorithmProvider.initializeSettings(self)

    def unload(self):
        AlgorithmProvider.unload(self)

    def getName(self):
        return 'ntv2_transformations'

    def getDescription(self):
        return u'NTV2 Datum Transformations'

    def getIcon(self):
        return QIcon(os.path.dirname(__file__) + '/icons/naturalgis_32.png')

    def _loadAlgorithms(self):
        self.algs = self.alglist