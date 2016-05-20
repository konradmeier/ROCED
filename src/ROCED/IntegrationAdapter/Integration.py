# ===============================================================================
#
# Copyright (c) 2010, 2011 by Thomas Hauth and Stephan Riedel
# 
# This file is part of ROCED.
# 
# ROCED is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# ROCED is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with ROCED.  If not, see <http://www.gnu.org/licenses/>.
#
# ===============================================================================

"""
The IntegrationAdapters are responsible for adding and removing cloud machines
to batch servers or other scheduling infrastructure
"""

import abc

from Core import Adapter


class IntegrationAdapterBase(Adapter.AdapterBase, metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def description(self):
        return "IntegrationAdapterBase"

    @abc.abstractmethod
    def init(self):
        pass


class IntegrationBox(Adapter.AdapterBoxBase):
    pass
