# Ladybug: A Plugin for Environmental Analysis (GPL)
# This file is part of Ladybug.
#
# Copyright (c) 2020, Ladybug Tools.
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Apply an analysis period to a data collection.
-

    Args:
        _data: A Ladybug data collection object.
        _period: A Ladybug analysis period.
    
    Returns:
        data: The data collection with the analysis period applied to it.
"""

ghenv.Component.Name = 'LB Apply Analysis Period'
ghenv.Component.NickName = 'ApplyPer'
ghenv.Component.Message = '0.1.1'
ghenv.Component.Category = 'Ladybug'
ghenv.Component.SubCategory = '1 :: Analyze Data'
ghenv.Component.AdditionalHelpFromDocStrings = '2'

try:
    from ladybug.analysisperiod import AnalysisPeriod
    from ladybug.datacollection import BaseCollection
except ImportError as e:
    raise ImportError('\nFailed to import ladybug:\n\t{}'.format(e))

try:
    from ladybug_rhino.grasshopper import all_required_inputs
except ImportError as e:
    raise ImportError('\nFailed to import ladybug_rhino:\n\t{}'.format(e))


if all_required_inputs(ghenv.Component):
    assert isinstance(_data, BaseCollection), \
        '_data must be a Data Collection. Got {}.'.format(type(_data))
    assert isinstance(_period, AnalysisPeriod), '_period must be an Analysis' \
        ' Period. Got {}.'.format(type(_period))
    data = _data.filter_by_analysis_period(_period)