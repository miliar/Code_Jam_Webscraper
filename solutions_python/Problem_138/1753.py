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
  offset = (i - 1) * 3
  num_blocks = contents[offset + 1]
  naomi_blocks = map(Decimal, contents[offset + 2].split(" "))
  naomi_blocks.sort()
  naomi_blocks_war = list(naomi_blocks)
  naomi_blocks_war.sort()
  ken_blocks = map(Decimal, contents[offset + 3].split(" "))
  naomi_points_deceitful = 0
  ken_blocks.sort()
  ken_blocks_war = list(ken_blocks)
  ken_blocks_war.sort()

  while (len(naomi_blocks) > 0):
    if(naomi_blocks[0] < ken_blocks[0]):
      naomi_blocks.pop(0)
      ken_blocks.pop()
    else:
      naomi_points_deceitful += 1
      naomi_blocks.pop(0)
      ken_blocks.pop(0)

  naomi_points_war = 0
  while (len(naomi_blocks_war) > 0):
    naomi_play = naomi_blocks_war[-1]
    ken_play = ken_blocks_war[-1]
    if(ken_blocks_war[-1] < naomi_play):
      ken_play = ken_blocks_war[0]
      naomi_points_war += 1
    else:
      for j in range(len(ken_blocks_war) - 1, -1, -1):
        if(ken_blocks_war[j] > naomi_play):
          ken_play = ken_blocks_war[j]
    ken_blocks_war.remove(ken_play)
    naomi_blocks_war.remove(naomi_play)


  o.write("Case #{0}: {1} {2}".format(str(i), str(naomi_points_deceitful), str(naomi_points_war)))
  if(i != count):
    o.write("\n")
o.close()