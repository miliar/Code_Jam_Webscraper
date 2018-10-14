from functools import lru_cache

def reverse(N):
    return int(''.join(reversed(list(str(N)))))

@lru_cache(maxsize = None)  # Memoization.
def naiveSolve(N):
    if N == 1:
        return 1
    s1 = naiveSolve(N-1) + 1
    if N % 10 != 0:
        rN = reverse(N)
        if rN < N:
            s2 = naiveSolve(rN) + 1
            return min(s1, s2)
    return s1

def solve(strN):
    l = len(strN)
    if l <= 4:
        return d[int(strN)]

    if strN == '1' + '0'*(l-1):
        return getAllNine(l-1) + 1
    
    firstHalf = strN[:l//2]
    secondHalf = strN[l//2:]

    if int(secondHalf) == 0:
        intFirstHalf = int(firstHalf) - 1
        intSecondHalf = int('1' + secondHalf)
    else:
        intFirstHalf = int(firstHalf)
        intSecondHalf = int(secondHalf)

    reversedIntFristHalf = reverse(intFirstHalf)
    
    if reversedIntFristHalf == 1:
        return intSecondHalf + reverse(intFirstHalf) + getAllNine(l-1)
    else:
        return intSecondHalf + reverse(intFirstHalf) + getAllNine(l-1) + 1

@lru_cache(maxsize = None)  # Memoization.
def getAllNine(length):
    if length == 1:
        return 9
    l1 = length // 2
    l2 = length - l1
    return getAllNine(length-1) + 10**l1 + 10**l2 - 1

d = {}
for i in range(1, 10**4+1):
    d[i] = naiveSolve(i)

fin = open('A-large.in')

caseNum = int(fin.readline())

for caseNo in range(caseNum):
    N = fin.readline().strip()
    print('Case #%d: %d' % (caseNo+1, solve(N)))
fin.close()
