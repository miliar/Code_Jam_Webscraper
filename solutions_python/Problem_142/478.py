def decompose(s):
    res = [[s[0], 1]]
    for c in s[1:]:
        last = res[-1]
        if c == last[0]:
            last[1] += 1
            continue
        res.append([c,1])
    return res
    
def num_changes(a,b):
    if a == b:
        return 0
    a = decompose(a)
    b = decompose(b)
    if len(a) != len(b):
        return None
    count = 0
    for i in range(len(a)):
        xa = a[i]
        xb = b[i]
        ca = xa[0]
        cb = xb[0]
        if ca != cb:
            return None
        count += abs(xa[1]-xb[1])
    return count

def solve(strings):
    min_num = None
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            a = strings[i]
            b = strings[j]
            c = num_changes(a,b)
            if c is None:
                return "Fegla Won"
            if min_num is None or c < min_num:
                min_num = c
    return str(min_num)

if __name__ == "__main__":
    T = int(raw_input())
    for i in range(1, T+1):
        N = int(raw_input())
        strings = []
        for j in range(N):
            strings.append(raw_input().strip())
        print "Case #%d: %s" % (i, solve(strings))
        
