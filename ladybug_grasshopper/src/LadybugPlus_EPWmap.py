# Ladybug: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Ladybug.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>


"""
Open EPWmap in web browser.
-

    Args:
        _epw_map: Set to "True" to open EPWmap
    Returns:
        report: ...
"""

ghenv.Component.Name = "LadybugPlus_EPWmap"
ghenv.Component.NickName = 'epwMap'
ghenv.Component.Message = 'VER 0.0.04\nSEP_10_2019'
ghenv.Component.Category = "LadybugPlus"
ghenv.Component.SubCategory = '00 :: Ladybug'
ghenv.Component.AdditionalHelpFromDocStrings = "1"

import webbrowser as wb
import os
try:
    from ladybug_rhino.grasshopper import all_required_inputs
except ImportError as e:
    raise ImportError('\nFailed to import ladybug:\n\t{}'.format(e))


# dictonary of accetable browsers and their default file paths.
acceptable_browsers = [
    ['chrome', 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'],
    ['firefox', 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'],
    ['chrome', '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'] # MacOS
    ]

# URL to epwmap.
url = 'http://www.ladybug.tools/epwmap/'

# function for opening a browser page on Mac
def mac_open(url):
    os.system("open \"\" " + url)

if all_required_inputs(ghenv.Component) and _epw_map is True:
    broswer_found = False
    for browser in acceptable_browsers:
        browser_path = browser[1]
        if broswer_found == False and os.path.isfile(browser_path) == True:
            broswer_found = True
            wb.register(browser[0],  None, wb.BackgroundBrowser(browser_path), 1)
            try:
                wb.get(browser[0]).open(url, 2, True)
                print "Opening epwmap."
            except ValueError:
                mac_open(url)
    if broswer_found == False:
       print "An accepable broswer was not found on your machine.\n" \
       "The default browser will be used but epwmap may not display correctly there."
       try:
        wb.open(url, 2, True)
       except ValueError:
        mac_open(url)
else:
    print "Set _epw_map to True."