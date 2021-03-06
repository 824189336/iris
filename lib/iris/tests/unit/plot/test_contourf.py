# (C) British Crown Copyright 2014 - 2016, Met Office
#
# This file is part of Iris.
#
# Iris is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Iris is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Iris.  If not, see <http://www.gnu.org/licenses/>.
"""Unit tests for the `iris.plot.contourf` function."""

from __future__ import (absolute_import, division, print_function)
from six.moves import (filter, input, map, range, zip)  # noqa

# Import iris.tests first so that some things can be initialised before
# importing anything else.
import iris.tests as tests

import numpy as np

from iris.tests import mock
from iris.tests.stock import simple_2d
from iris.tests.unit.plot import TestGraphicStringCoord, MixinCoords

if tests.MPL_AVAILABLE:
    import iris.plot as iplt


@tests.skip_plot
class TestStringCoordPlot(TestGraphicStringCoord):
    def test_yaxis_labels(self):
        iplt.contourf(self.cube, coords=('bar', 'str_coord'))
        self.assertPointsTickLabels('yaxis')

    def test_xaxis_labels(self):
        iplt.contourf(self.cube, coords=('str_coord', 'bar'))
        self.assertPointsTickLabels('xaxis')

    def test_yaxis_labels_with_axes(self):
        import matplotlib.pyplot as plt
        fig = plt.figure()
        ax = fig.add_subplot(111)
        iplt.contourf(self.cube, axes=ax, coords=('bar', 'str_coord'))
        plt.close(fig)
        self.assertPointsTickLabels('yaxis', ax)

    def test_xaxis_labels_with_axes(self):
        import matplotlib.pyplot as plt
        fig = plt.figure()
        ax = fig.add_subplot(111)
        iplt.contourf(self.cube, axes=ax, coords=('str_coord', 'bar'))
        plt.close(fig)
        self.assertPointsTickLabels('xaxis', ax)

    def test_geoaxes_exception(self):
        import matplotlib.pyplot as plt
        fig = plt.figure()
        ax = fig.add_subplot(111)
        self.assertRaises(TypeError, iplt.contourf,
                          self.lat_lon_cube, axes=ax)
        plt.close(fig)


@tests.skip_plot
class TestCoords(tests.IrisTest, MixinCoords):
    def setUp(self):
        # We have a 2d cube with dimensionality (bar: 3; foo: 4)
        self.cube = simple_2d(with_bounds=False)
        self.foo = self.cube.coord('foo').points
        self.foo_index = np.arange(self.foo.size)
        self.bar = self.cube.coord('bar').points
        self.bar_index = np.arange(self.bar.size)
        self.data = self.cube.data
        self.dataT = self.data.T
        mocker = mock.Mock(alpha=0, antialiased=False)
        self.mpl_patch = self.patch('matplotlib.pyplot.contourf',
                                    return_value=mocker)
        self.draw_func = iplt.contourf


if __name__ == "__main__":
    tests.main()
