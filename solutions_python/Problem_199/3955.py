import collections
intab = "+-"
outtab = "-+"
trantab = ''.maketrans(intab, outtab)

def flip(S, K):
    flipped = collections.deque()
    states = set()
    flipped.append((S, 0))
    minAns = -1
    while flipped:
        S, moves = flipped.popleft()
        states.add(S)
        if '-' not in S:
            return moves
        for i in range(0, len(S) - K + 1):
            newS = S[:i] + S[i:i+K].translate(trantab) + S[i+K:]
            if newS not in states:
                ans = flipped.append((newS, moves+1))
    return minAns

t = int(input())
for i in range(1, t + 1):
    S, K = [s for s in input().split(" ")]  # read a list of integers, 2 in this case
    ans = flip(S, int(K))
    if ans == -1:
        ans = 'IMPOSSIBLE'
    print("Case #{}: {}".format(i, ans))
