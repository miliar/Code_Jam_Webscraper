#! usr/bin/python

file_read = open("D-large.in", "r")
file_write = open("D-large-output.out", "w")
num = int(file_read.readline()) #number of cases
for i in range(num):
  blocks = int(file_read.readline())
  naomi_blocks = file_read.readline().split() #deceitful
  naomi_blocks.sort()
  ken_blocks = file_read.readline().split() #deceitful
  ken_blocks.sort()
  naomi_war_blocks = [x for x in naomi_blocks] #regular war
  ken_war_blocks = [x for x in ken_blocks] #regular war
  war_score = 0 #keep track of regular game
  deceit_score = 0 #keep track of deceitful game
  #check WAR
  for block in naomi_war_blocks:
    for ken_block in ken_war_blocks:
      ken_point = False
      if ken_block > block:
        ken_war_blocks.remove(ken_block) #remove Ken's first larger block
        ken_point = True
        break
    if not ken_point:
      del ken_war_blocks[0] #remove Ken's smallest block
      war_score += 1
  #check DECEITFUL WAR
  count = 0
  for block in naomi_blocks:
    if block > ken_blocks[count]:
      count += 1
  deceit_score = count
  file_write.write("Case #{0}: {1} {2}\n".format(i + 1, deceit_score, war_score))

file_read.close()
file_write.close()