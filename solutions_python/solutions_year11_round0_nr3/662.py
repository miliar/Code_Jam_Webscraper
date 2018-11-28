def subsets(s):
    l = list(s)
    for i in range(1, 2**len(s)-1):
        res = []
        for j in range(len(s)):
            if 1<<j & i != 0:
                res.append(l[j])
        yield res

def list_sub(l1, l2):
    res = l1[:]
    for element in l2:
        res.remove(element)
    return res

def sumxor(s):
    try:
        return reduce(lambda a,b: a^b, s)
    except TypeError:
        return 0

def solve(s):
    m = -1
    for s1 in subsets(s):
        s2 = list_sub(s, s1)
        sum1 = sumxor(s1)
        sum2 = sumxor(s2)
        if sum1 == sum2 and sum(s1) > m:
            m = sum(s1)
    if m == -1:
        return False
    return m

if __name__ == "__main__":
    T = int(raw_input())
    for i in range(1, T+1):
        raw_input()
        numbers = map(int, raw_input().split())
        a = solve(numbers)
        print "Case #%d:"% i, 
        if a:
            print a
        else:
            print "NO"

        
