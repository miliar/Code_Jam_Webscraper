INPUT = 'A-large.in'
OUTPUT = 'largeOutputA1.txt'
def getInput(filename):
   file = open(filename, 'r')
   stng = file.read().split()
   file.close()
   return stng

def solve(length, trial):
   totalStanding = 0
   invited = 0
   for n in range(length):
      totalStanding+=int(trial[n])
      if n+1>totalStanding:
         x = n+1-totalStanding
         invited+=x
         totalStanding+=x
   return invited
   

def main():
   stng = getInput(INPUT)
   n = int(stng[0])
   f = open(OUTPUT, 'w')
   for i in range(1, n*2+1, 2):
      f.write('Case #'+str(i//2+1)+': ' + str(solve(int(stng[i]), stng[i+1]))+'\n')
main()