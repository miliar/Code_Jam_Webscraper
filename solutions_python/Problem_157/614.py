T = int(raw_input())

def mul(a, b, neg):
    if a == "1":
        return (b, neg)
    if b == "1":
        return (a, neg)
    if a == "i":
        if b == "i":
            return ("1", not neg)
        if b == "j":
            return ("k", neg)
        if b == "k":
            return ("j", not neg)
    if a == "j":
        if b == "i":
            return ("k", not neg)
        if b == "j":
            return ("1", not neg)
        if b == "k":
            return ("i", neg)
    if a == "k":
        if b == "i":
            return ("j", neg)
        if b == "j":
            return ("i", not neg)
        if b == "k":
            return ("1", not neg)


for _case_ in xrange(T):
    L, X = [int(_) for _ in raw_input().split()]
    inp = raw_input()
    string = inp*X
    l = L*X
    no = False
    i = 0;
    ans = "YES"
    for term in ["i", "j", "k"]:
        val = "1"
        neg = False
        while val != term or neg:
            if i == l:
                ans = "NO"
                break
            val, neg = mul(val, string[i], neg)
            i += 1
    val = "1"
    neg = False
    while i < l:
        val, neg = mul(val, string[i], neg)
        i += 1
    if val != "1" or neg:
        ans = "NO"
    print "Case #"+str(_case_+1)+": "+ans



