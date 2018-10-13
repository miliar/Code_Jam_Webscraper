import sys
import math

path = "/Users/yongc0916/Downloads/"
testFile = open(path + "D-small.in", 'r')
fil = open(path+"D-small.out", 'w+')
rlist = testFile.readlines()
rlist = rlist[1:]

def war(naomi, ken, wins):
   a = -1
   for x in range(len(ken)):
      if (naomi[0] < ken[x]):
         a = x
         break
   if (a == -1):
      return (len(naomi))
   else:
      return war(naomi[1:], ken[:a]+ken[a+1:], 0)

def d_war(naomi, ken, wins):
   if (len(naomi) < 1):
      return wins
   elif (naomi[0] < ken[0]):
      return d_war(naomi[1:], ken[:-1], wins)
   else:
      return d_war(naomi[1:], ken[1:], wins+1)

n = 3
split_list = [rlist[i:i+n] for i in range(0, len(rlist), n)]
for num in range(len(split_list)):
   [blocks, naomi, ken] = split_list[num]
   naomi = [float(x) for x in naomi]
   ken = [float(x) for x in ken]
   d_war_wins = d_war(naomi, ken, 0)
   war_wins = war(naomi, ken, 0)
   fil.write("Case #" + str(num+1) + ": " + str(d_war_wins) + " " + str(war_wins) + "\n")


