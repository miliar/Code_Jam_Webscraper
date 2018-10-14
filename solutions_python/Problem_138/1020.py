def isCoBig(A, B, st):
    for i in range(len(B) - st):
        if B[st+i] <= A[i]:
            return False
    return True

def isCoBigDec(A, B, st):
    for i in range(len(B) - st):
        if A[st+i] <= B[i]:
            return False
    return True

def findCoBig(A, B):
    for i in range(len(A)+1):
        if isCoBig(A, B, i):
            return i 

def findCoBigDec(A, B):
    for i in range(len(A)+1):
        if isCoBigDec(A, B, i):
            return len(B) - i 

N = int(raw_input())
for n in range(N):
    raw_input()
    A = [float(x) for x in raw_input().split()] # Naomi
    B = [float(x) for x in raw_input().split()] # Ken
    dec = findCoBigDec(sorted(A), sorted(B))
    war = findCoBig(sorted(A), sorted(B))
    print("Case #%d: %d %d" % (n+1, dec, war))

