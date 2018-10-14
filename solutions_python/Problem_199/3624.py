
def solve(S, K):
    
    counter = 0
    x = "".rjust(K, '-')
    y = "".rjust(K, '+')
    for i in range(0, len(S)):
        if S.find("-") == -1:
            return counter
        if S.find("+") == -1 and len(S) % K == 0:
             counter += (len(S) // K)
             return counter

        if S[i] == "+":
            continue
        
        r = ""
        stop = i + K
        if stop > len(S):
            break
        for j in range(i, stop):
            if S[j] == "+":
                r += "-"
            else:
                r += "+"
        S = S[:i] + r + S[i + K:]
        counter += 1
    return "IMPOSSIBLE"


t = int(input())
for i in range(1, t + 1):
    S,K = input().split()
    retval = solve(S, int(K))
    print("Case #{}: {}".format(i, retval))
