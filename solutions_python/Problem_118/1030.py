import math

def palindrome(n):
    s = str(n)
    rs = s[::-1]
    for i in range(len(s)):
        if rs[i] != '0':
            break
    rs = rs[i:]
    if rs == s:
        return True
    else:
        return False

def main():
    T = int(raw_input())
    for ti in xrange(T):
        AB = [int(x) for x in raw_input().split()]
        A = AB[0]
        B = AB[1]
        ans = 0
        for i in xrange(int(math.sqrt(A)), int(math.sqrt(B))+1):
            square = i*i
            if A<=square<=B and palindrome(i) and palindrome(square):
                ans += 1
        print "Case #{0}: {1}".format(ti+1, ans)
    pass

if __name__ == "__main__":
    main()
