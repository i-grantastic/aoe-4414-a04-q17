# ymdhms_to_jd.py
#
# Usage: python3 ymdhms_to_jd.py year month day hour minute second
#   converts SEZ coordinates to ECEF coordinates

# Parameters:
#   year: int
#   month: int
#   day: int
#   hour: int
#   minute: int
#   second: float

# Output:
#   Julian date in days
#
# Written by Grant Chapman
# Other contributors: None

# import Python modules
import math # math module
import sys # argv

# initialize script arguments
year   = float('nan')
month  = float('nan')
day    = float('nan')
hour   = float('nan')
minute = float('nan')
second = float('nan')

# parse script arguments
if len(sys.argv) == 7:
  year   = int(sys.argv[1])
  month  = int(sys.argv[2])
  day    = int(sys.argv[3])
  hour   = int(sys.argv[4])
  minute = int(sys.argv[5])
  second = float(sys.argv[6])
else:
  print(\
    'Usage: '\
    'python3 ymdhms_to_jd.py year month day hour minute second'\
  )
  exit()

### script below this line ###

# julian date
jd = day - 32075 + 1461*(year + 4800 + (month - 14)/12)/4\
+ 367*(month - 2 - (month - 14)/12*12)/12\
- 3*((year + 4900 + (month - 14)/12)/100)/4

# fractional julian date
jd_midnight = int(jd) - 0.5
d_frac = (second + 60*(minute + 60*hour))/86400
jd_frac = jd_midnight + d_frac

# print
print(jd_frac)
