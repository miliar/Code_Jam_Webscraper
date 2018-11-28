def divideStalls(num_of_stalls, num_of_ppl):
    availableStalls = [num_of_stalls]
    i = 0
    while num_of_ppl - 1:
        biggestStall = max(availableStalls)
        middle = biggestStall / 2
        num_of_ppl -= 1

        availableStalls.remove(biggestStall)

        if biggestStall % 2 == 0:
            availableStalls.append(middle)
            availableStalls.append(middle - 1)
        else:
            availableStalls.append(middle)
            availableStalls.append(middle)
    
    if max(availableStalls) % 2 == 0:
        return [max(availableStalls)/2, (max(availableStalls)/2) - 1]
    else:
        return [max(availableStalls)/2, max(availableStalls)/2]


test_cases = int(raw_input())
occStalls = []

for case in xrange(1, test_cases + 1):
    n, k = [int(n) for n in raw_input().split(" ")]
    occStalls = []
    divided = divideStalls(n, k)
    
    print "Case #{}: {} {}".format(case, divided[0], divided[1])