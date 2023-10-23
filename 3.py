# 3. Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

import time
from datetime import date

print(date.today(), time.strftime("%H:%M:%S", time.localtime()))