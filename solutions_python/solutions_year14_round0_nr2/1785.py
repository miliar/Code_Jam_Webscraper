import sys
from decimal import *

infile, outfile = sys.argv[1], sys.argv[2]

f = open(infile)
contents = [line.strip() for line in f]
f.close()
count = contents[0]

games = range(1,(int(count) + 1))
o = open(outfile, "a")

for i in games:
  params =map(Decimal, contents[i].split(" "))
  c = params[0]
  f = params[1]
  x = params[2]
  farm_range = range(1, int(x))
  prev_best = x/Decimal(2.0000000)
  fastest_to_farm = [Decimal(0.0000000)]
  for j in farm_range:
    previous_farm_time = sum(fastest_to_farm)
    time_to_next_farm = c / ((j - 1) * f + 2)
    fastest_to_farm.append(time_to_next_farm)
    time_left_to_finish = x / (j * f + 2)
    time_with_i_farms = previous_farm_time + time_to_next_farm +time_left_to_finish
    if(time_with_i_farms < prev_best):
      prev_best = time_with_i_farms
    else:
      break
  o.write("Case #{0}: {1}".format(str(i), str(prev_best)))
  if i != count:
    o.write("\n")
o.close()