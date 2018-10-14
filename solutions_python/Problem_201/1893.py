import math
infile = open('C-small-1-attempt1.in','r')
t = infile.readline()
outfile = open('q1outsmall.txt','w')
line = str(infile.readline().strip())
count = 1
def determine(strin):
    global bathroom
    splitted = strin.strip().split()
    n = int(splitted[0])
    k = int(splitted[1])
    bathroom = [0,n+1]
    for i in range(k):
        bathroom.append(nextMid(bathroom))
        if i == k - 1:
            pos = bathroom[len(bathroom)-1]
        bathroom.sort()
    return mx(bathroom,pos) + ' '+mn(bathroom,pos)
def mx(bathroom,pos):
    for i in range(len(bathroom)):
        if bathroom[i] == pos:
            if i == 0:
                l = 0
            else:
                l = bathroom[i] - bathroom[i-1]-1
            if i == len(bathroom)-1:
                r = 0
            else:
                r = bathroom[i+1] - bathroom[i]-1
            break
    return str(max(l,r))
def mn(bathroom,pos):
    for i in range(len(bathroom)):
        if bathroom[i] == pos:
            if i == 0:
                l = 0
            else:
                l = bathroom[i] - bathroom[i-1]-1
            if i == len(bathroom)-1:
                r = 0
            else:
                r = bathroom[i+1] - bathroom[i]-1
            break
    return str(min(l,r))
def nextMid(bath):
    diffs = []
    for d in range(len(bath)-1):
        diffs.append(bath[d+1]-bath[d])
    maxDiff = diffs[0]
    left = bath[0]
    for diff in range(len(diffs)):
        if diffs[diff] > maxDiff:
            maxDiff = diffs[diff]
            left = bath[diff]
    #print(left)
    #print(maxDiff)
    return left + math.floor(maxDiff/2)
#for i in range(15):
#   print('15 '+str(i+1)+': '+determine('15 '+str(i+1)))
while line != "":
    outfile.write("Case #"+str(count)+": "+str(determine(line))+"\n")
    print("just done "+str(line))
    line = str(infile.readline())
    count += 1
outfile.close()
print('done')
