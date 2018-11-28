import bisect
def main():
    T = int(raw_input())
    res = []
    palindromic_squares = [1,4,9,121,484]
    #palindromic_squares = palindromic_squares[::-1]
    for i in xrange(T):
        p = 0
        q = 0
        a,b = map(int, raw_input().split())
        p = bisect.bisect_left(palindromic_squares, a)
        q = bisect.bisect_left(palindromic_squares, b)
        #print p,q,palindromic_squares[p],palindromic_squares[q]
        if p < len(palindromic_squares):
            if q == len(palindromic_squares):
                q = len(palindromic_squares)
            elif q < len(palindromic_squares):
                #print p,q
                if a == palindromic_squares[p] and b == palindromic_squares[q]:
                    p = p-1
                elif a != palindromic_squares[q] and b == palindromic_squares[q]:
                    q = q+1
        else:
            p = 0
            q = 0
        
        #print p,q
        res.append(q-p)
    for i in xrange(1,T+1):
        print "Case #%d:"%i,res[i-1]
if __name__  == "__main__":
    main()

