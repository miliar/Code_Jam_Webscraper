#!python3.4
import sys

def main():
  rawlines = sys.stdin.read(-1).splitlines(False)
  NumTests = int(rawlines.pop(0)) #pop header

  for testcase in enumerate(rawlines):
    totalStanding = 0
    numToInvite = 0
    spiltistr = testcase[1].split()
    maxlvl = int(spiltistr[0])
    people = spiltistr[1]
    #print(maxlvl, people)
    for p in enumerate(people):
      
      S = int(p[0]) #level of shiness
      N = int(p[1]) #number of people
      if(S==0):
        totalStanding += N
        continue
      if totalStanding < S:
        diff = S - totalStanding
        numToInvite += diff #invite enought freinds to fix this offet
        totalStanding += diff #friends are now standing too

      totalStanding+= N #all people of this shinness now standing
    print ("Case #"+str(testcase[0]+1)+":", numToInvite)

if __name__ == "__main__":
    main()
