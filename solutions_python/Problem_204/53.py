#!/usr/bin/env python3

T = int(input().strip())

for t in range(T):
    print("Case #{}: ".format(t + 1), end="")

    ingredients, packets = map(int, input().strip().split(" "))
    optimalAmounts = [int(i) for i in input().strip().split(" ")]

    packets = [list(map(int, input().strip().split(" "))) for _ in range(ingredients)]
    [ingredient.sort(reverse=True) for ingredient in packets]
    
    made = 0
    
    while len(min(packets, key=len)) > 0:
        servingsUpperBound = min((presentPackets[-1]*100)//(optimal*90) for optimal, presentPackets in zip(optimalAmounts, packets))
        servingsLowerBound = max(-((-presentPackets[-1]*100)//(optimal*110)) for optimal, presentPackets in zip(optimalAmounts, packets))
        #print(list(zip(optimalAmounts, packets)))
        #print([-((-presentPackets[-1]*100)//(optimal*110)) for optimal, presentPackets in zip(optimalAmounts, packets)])
        #print(servingsUpperBound, servingsLowerBound)
        if servingsUpperBound >= servingsLowerBound:
            for presentPackets in packets:
                presentPackets.pop(-1)
            made += 1
        else:
            for optimal, presentPackets in zip(optimalAmounts, packets):
                if (presentPackets[-1]*100)//(optimal*90) == servingsUpperBound:
                    presentPackets.pop(-1)
    print(made)

