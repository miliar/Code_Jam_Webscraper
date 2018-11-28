import sys


def remaining_sum(l, index):
    i = index
    res = 0
    while(i < len(l)):
        res += abs(l[i])
        i+=1
    return  res

def flip(l, index, k):
    total = 0
    while(total + abs(l[index]) <k):
        l[index] = -l[index]
        total += abs(l[index])
        index +=1
    if l[index] < 0:
        l.insert(index, k-total)
        l[index+1] = l[index+1] + (k-total)
    else:
        l.insert(index, -(k - total))
        l[index+1] = l[index+1] - (k-total)
    while( 0 in l):
        l.remove(0)
    i = index
    while i < len(l)-1:
        if l[i] < 0 and l[i+1] < 0:
            l[i+1] = l[i] + l[i+1]
            l.pop(i)
        elif l[i] > 0 and l[i + 1] > 0:
            l[i + 1] = l[i] + l[i + 1]
            l.pop(i)
        else:
            i = i+1

name = "A-large"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

for testCase in range(1, testCases + 1):
    line = raw_input()
    line = line.split()
    inputs = line[0]
    k = int(line[1])

    cakes = []
    last = None
    current_count = 0
    res =0
    for c in inputs:
        if last is None:
            last = c
            current_count +=1
        elif last != c:
            if last == "-":
                cakes.append(-current_count)
            else:
                cakes.append(current_count)
            last = c
            current_count = 1
        else:
            current_count += 1
    if last == "-":
        cakes.append(-current_count)
    else:
        cakes.append(current_count)
    #print cakes

    if len(cakes) == 1 and cakes[0] < 0:
        if abs(cakes[0]) % k == 0:
            print("Case #" + str(testCase) + ": " + str(abs(cakes[0])/k))
        else:
            print("Case #" + str(testCase) + ": " + "IMPOSSIBLE")
    elif len(cakes) == 1 and cakes[0] > 0:
        print("Case #" + str(testCase) + ": 0")
    else:
        i = 0
        res = 0
        #remaining = 0
        possible = True
        while i < len(cakes):
            #print cakes, cakes[i]
            if cakes[i] < 0:
                res += (abs(cakes[i])) / k
                #remaining = (remaining + abs(cakes[i])) % k
                remaining = (abs(cakes[i])) % k
                if remaining != 0:
                    if remaining + remaining_sum(cakes, i+1) < k:
                        possible = False
                        break
                    else:
                        flip(cakes, i+1, k-remaining)
                        res += 1
            i += 1


                    # if i == len(cakes) -2 or i == len(cakes)-1:
                    #     if remaining !=0:
                    #         possible = False
                    #         break
                    # else:
                    #     if (remaining + abs(cakes[i+1])) % k != 0:
                    #         possible = False
                    #         break
                    #     else:
                    #         if ((remaining + abs(cakes[i+1])) / k) % 2 != 0:
                    #             res += (remaining + abs(cakes[i+1]))/k
                    #             remaining = k - remaining
                    #         else:
                    #             res += (remaining + abs(cakes[i + 1])) / k
                    #             remaining = remaining
        if possible:
            print("Case #" + str(testCase) + ": " + str(res))
        else:
            print("Case #" + str(testCase) + ": " + "IMPOSSIBLE")












    # if res>=0:
    #     print("Case #" + str(testCase) + ": " + str(res))
    # else:
    #     print("Case #" + str(testCase) + ": " + "IMPOSSIBLE")
