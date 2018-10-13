__author__ = 'Glen'
from collections import deque

numCases = int(input().strip())
for caseNum in range(numCases):
    numBlocks = int(input().strip())
    blocksN = sorted(map(float, input().strip().split()))
    blocksK = sorted(map(float, input().strip().split()))
    # Calc war outcome
    bn = deque(blocksN)
    bk = deque(blocksK)
    warScore = 0
    while len(bn) > 0:
        n = bn.pop()
        k = bk.pop()
        if n > k:
            bk.append(k)
            bk.popleft()
            warScore += 1
    # Calc deceitful war outcome
    bn = deque(blocksN)
    bk = deque(blocksK)
    dWarScore = 0
    while len(bn) > 0:
        n = bn.pop()
        k = bk.pop()
        if n > k:
            dWarScore += 1
        else:
            bn.append(n)
            bn.popleft()
    print('Case #{}: {} {}'.format(caseNum+1, dWarScore, warScore))