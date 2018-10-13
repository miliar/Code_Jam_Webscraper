#!/usr/bin/python

def toPossibleScores(x):
     test = [x/3,x/3,x/3]
     bumpCount = x%3
     for x in range(0,bumpCount):
          test[x] += 1
     return test

fd = open('input.txt','r')
count = int(fd.readline().strip())
iterator = 0
while iterator < count:
    iterator += 1
    input = fd.readline().strip().split(" ")
    trash = input.pop(0)
    supprising = int(input.pop(0))
    threshold = int(input.pop(0))
    passCount = 0
    #First to eliminate the ones already there.
    processed = []
    for x in input:
        processed.append(toPossibleScores(int(x)))
        if processed[-1][0] >= threshold:
            passCount += 1
            trash = processed.pop()
    processed.sort()
    # Proctect against assumption
    if supprising > len(processed):
        supprising = len(processed)
    # Second pass for supprise
    for x in range(0,len(processed)):
        if supprising is 0:
            break
        current = processed[-x-1]
        if current.count(current[0]) is 3:
            if current[0] is 0:
                continue
            if current[0]+1 >= threshold:
                passCount+=1
                supprising -= 1
                continue
        if current.count(current[0]) is 2:
            if current[0]+1 >= threshold:
                passCount += 1
                supprising -= 1
                continue
        if current.count(current[0]) is 1:
            continue
    # Tell us what you found
    output = "Case #%s: %s" % (iterator,passCount)
    print output
