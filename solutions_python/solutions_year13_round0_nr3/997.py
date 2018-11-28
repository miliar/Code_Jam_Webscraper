def pal(i):
    return i == int(str(i)[::-1])
from math import sqrt,pow

data = open(r"C:\Users\Eric\Desktop\data.txt").readlines()[1:]
trialnum = 1
for trial in data:
    start,end = trial.split()
    start,end = int(start),int(end)
    matches = 0
    for i in range(start,end+1):
        if pal(i) and int(sqrt(i))**2==i and pal(int(sqrt(i))):
            matches += 1
    print "Case #%d: %d"%(trialnum,matches)
    trialnum+=1
