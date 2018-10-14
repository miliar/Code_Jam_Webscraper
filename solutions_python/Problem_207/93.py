

f = open("2.in")

num_test = int(f.readline())

for iter_test in xrange(num_test):
    line = f.readline()
    n, r, o, y, g, b, v = map(int, line.split())
    def solve(r, o, y, g, b, v):
        r, g, sr = cc(r, g, "R", "G")
        y, v, sy = cc(y, v, "Y", "V")
        b, o, sb = cc(b, o, "B", "O")
        #print sr, sy, sb
        if sr is None or sy is None or sb is None:
            print "FUCK"
            return False
        #print r, g, y, v, b, o
        if r == 0 and y == 0 and b == 0:
            if sr == "" and sy == "" and sb != "":
                return sb
            elif sr == "" and sy != "" and sb == "":
                return sy
            elif sr != "" and sy == "" and sb == "":
                return sr
            else:
                return False
            
        if (b > r + y) or (r > b + y) or (y > r + b):
            return False
        t = max(r, y, b)
        if t == r:
            s = "R"
        elif t == y:
            s = "Y"
        elif t == b:
            s = "B"
        ans = dd(r, y, b, "R", "Y", "B", s, "")
        ans = ans.replace("R", "R" + sr,1)
        ans = ans.replace("Y", "Y" + sy,1)
        ans = ans.replace("B", "B" + sb,1)
        return ans

    def dd(a, b, c, A, B, C, s, t):
        #print a, b, c
        if a + b + c == 1:
            if a == 1:
                return A
            if b == 1:
                return B
            if c == 1:
                return C
        if a == b == 1 and c == 0:
            if s != B and t != A:
                return A+B
            else:
                return B+A
        if a == c == 1 and b == 0:
            if s != C and t != A:
                return A+C
            else:
                return C+A
        if c == b == 1 and a == 0:
            if s != B and t != C:
                return C+B
            else:
                return B+C
        if a == b == c == 1:
            if t != A and s != B:
                return A + C + B
            if t != B and s != A:
                return B + C + A
            if t != C and s != A:
                return C + B + A
            if t != A and s != C:
                return A + B + C
            if t != B and s != C:
                return B + A + C
            if t != C and s != B:
                return C + A + B
        x = max(a, b, c)
        if x == a:
            y = max(b, c)
            if y == b:
                return A + B + dd(a-1, b-1, c, A, B, C, s, B)
            elif y == c:
                return A + C + dd(a-1, b, c-1, A, B, C, s, C)
        elif x == b:
            y = max(a, c)
            if y == a:
                return B + A + dd(a-1, b-1, c, A, B, C, s, A)
            elif y == c:
                return B + C + dd(a, b-1, c-1, A, B, C, s, C)
        elif x == c:
            y = max(a, b)
            if y == a:
                return C + A + dd(a-1, b, c-1, A, B, C, s, A)
            elif y == b:
                return C + B + dd(a, b-1, c-1, A, B, C, s, B)
         
        

    def cc(a, b, A, B):
        #print a, b, A, B
        if b <= a:
            return a - b, 0, (B+A) * b
        else:
            return 0, 0, None

    def bb(a, b, A, B):
        if a == b:
            return (A + B) * a
        else:
            return False
    def mm(r, o, y, g, b, v):
        """
        if (r == y == g == v == 0):
            return bb(b, o, "B", "O")
        if (r == g == b == o == 0):
            return bb(y, v, "Y", "V")
        if (y == v == b == o == 0):
            return bb(r, g, "R", "G")
        """
        return solve(r, o, y, g, b, v)

    ans = mm(r, o, y, g, b, v)
    print "Case #%d:"%(iter_test + 1),
    if ans == False:
        print "IMPOSSIBLE"
    else:
        print ans
