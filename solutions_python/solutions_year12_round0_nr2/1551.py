def test( p,score, diff ):
    for a in range(0,11):
        for b in range(0,11):
            c = score-a-b
            if c>=0 and c <= 10:
                if abs(a-b) <= diff and abs(b-c) <= diff and abs(a-c) <= diff:
                    if a >= p or b >= p or c >= p:
                        return True
    return False
    

T = int(input())
for tc in range(1,T+1):
    inp = [int(s) for s in input().split(" ")]
    N = inp[0]
    S = inp[1]
    p = inp[2]
    sc = []
    for i in range(3,len(inp)):
        sc.append(inp[i])
    res = 0
    use = 0
    for score in sc:        
        if test(p,score,1):
            res = res+1
        else:
            if test(p,score,2) and use < S:
                use = use + 1
                res = res + 1
        #print("score is {} p is {} res is {}".format(score,p,res))
    print("Case #{}: {}".format(tc,res))