import sys

def Problem1(num, s, k):
    lst = list(s)
    cnt = 0
    oldStrings = []
    
    while (1):
        index = FindStr(lst, k)
        if index == -1:
            # nothing more to do
            break
        elif index + k > len(lst):
            # make sure you are not past the end of the line
            index = len(lst) - k
            if index < 0:
                cnt = -1
                break
        
        #substitute
        for i in range(index, index+k):
            if i > len(lst) - 1:
                break;
            
            if lst[i] == '+': lst[i] = '-'
            else: lst[i] = '+'
        
        cnt = cnt + 1
        
        # maintain what strings we've already encountered
        oldString = ''.join(lst)
        if oldString in oldStrings:
            cnt = -1
            break;
        else:
            oldStrings.append(oldString)

    if cnt == -1: print("Case #" + str(num) + ": IMPOSSIBLE")
    else: print("Case #" + str(num) + ": " + str(cnt))


def FindStr(lst, k):
    index = -1
    total = 0
    bestIndex = -1
    bestTotal = 0
    
    for i in range(0, len(lst)):
        if lst[i] == '-':
            if index == -1:
                index = i
                total = 1
            else:
                total = total + 1
                if total == k:
                    # found K pancakes
                    bestIndex = index
                    bestTotal = total
                    break
                
            #found <K pancakes
            if total > bestTotal:
                bestTotal = total
                bestIndex = index
                    
        else:
            if total == 0:
                continue
            
            index = -1
            total = 0
            
    return bestIndex



cnt = 0
numCases = 0
for line in sys.stdin:
    if cnt == 0:
        numCases = int(line)
    else:
        if cnt <= numCases:
            split = line.split()
            Problem1(cnt, split[0], int(split[1]))
        else:
            break
        
    cnt = cnt + 1


    
