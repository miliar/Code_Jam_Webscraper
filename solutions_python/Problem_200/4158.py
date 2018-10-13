def isTidy(n):
    n = map(int, list(str(n)))
    for i in range(len(n) - 1):
        if n[i + 1] < n[i]: return False 
    return True

def solve(n):
    if isTidy(n): return n
    else:
        n_ = map(int, list(str(n)))
        for i in range(len(n_) - 1):
            if n_[i] >= n_[i + 1]:
                n_[i] -= 1
                for j in range(i + 1, len(n_)):
                    n_[j] = 9
                break
    return "".join(map(str, n_)).lstrip("0") or "0"

t = int(raw_input().strip())
for _ in range(1, t + 1):
    n = int(raw_input().strip())
    print "Case #" + str(_) + ":", solve(n)