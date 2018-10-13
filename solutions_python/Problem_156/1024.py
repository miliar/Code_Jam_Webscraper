for test in range(int(input())):

    skip = int(input())
    Pancakes = list(map(int, input().split()))

    currAns = max(Pancakes)
    sp = 2
    
    while sp < currAns:
        currAns = min(currAns, sum([(i-1)//sp for i in Pancakes]) + sp)
        sp = sp+1

    print('Case #%d: %s' % (test+1, currAns))