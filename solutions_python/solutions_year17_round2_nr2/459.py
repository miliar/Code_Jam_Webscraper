def is_legal(c1, c2):
    l = [("r", "y"), ("r", "b"), ("r", "g"),
         ("b", "y"), ("y", "v"),
         ("b", "o")]
    l = map(lambda x:tuple(sorted(x)), l)
    if tuple(sorted([c1, c2])) in l:
        return True
    return False

def unicorn(n, r, o, y, g, b, v):
    cnt = {"r":r, "o":o, "y":y, "g":g, "b":b, "v":v}
    def red(s):
        g, b, y = cnt["g"], cnt["b"], cnt["y"]
        if g > 0:
            cnt["g"] -= 1
            return "G"
        if not is_legal(s[0].lower(), "y") and not is_legal(s[0].lower(), "b"):
            if b > y:
                cnt["b"] -= 1
                return "B"
            if y > 0:
                cnt["y"] -= 1
                return "Y"   
        if y > 0 and not is_legal(s[0].lower(), "y"):
            cnt["y"] -= 1
            return "Y"
##        print b, y
        if y > b:
            cnt["y"] -= 1
            return "Y"
        if b > 0:
            cnt["b"] -= 1
            return "B"        
        return False

    def yellow(s):
        v, b, r = cnt["v"], cnt["b"], cnt["r"]
        if v > 0:
            cnt["v"] -= 1
            return "V"
        if not is_legal(s[0].lower(), "r") and not is_legal(s[0].lower(), "b"):
            if b > r:
                cnt["b"] -= 1
                return "B"
            if r > 0:
                cnt["r"] -= 1
                return "R"
        if r > 0 and not is_legal(s[0].lower(), "r"):
            cnt["r"] -= 1
            return "R"
        if b > r:
            cnt["b"] -= 1
            return "B"
        if r > 0:
            cnt["r"] -= 1
            return "R"
        return False

    def blue(s):
        o, y, r = cnt["o"], cnt["y"], cnt["r"]
        if o > 0:
            cnt["o"] -= 1
            return "O"
        if not is_legal(s[0].lower(), "r") and not is_legal(s[0].lower(), "y"):
            if y > r:
                cnt["y"] -= 1
                return "Y"
            if r > 0:
                cnt["r"] -= 1
                return "R"
        if r > 0 and not is_legal(s[0].lower(), "r"):
            cnt["r"] -= 1
            return "R"
        if y > r:
            cnt["y"] -= 1
            return "Y"
        if r > 0:
            cnt["r"] -= 1
            return "R"
        return False
    
    def green(s):
        r = cnt["r"]
        if r > 0:
            cnt["r"] -= 1
            return "R"
        return False

    def violet(s):
        y = cnt["y"]
        if y > 0:
            cnt["y"] -= 1
            return "Y"
        return False

    def orange(s):
        b = cnt["b"]
        if b > 0:
            cnt["b"] -= 1
            return "B"
        return False

    if r > 0:
        s = "R"
    elif y > 0:
        s = "Y"
    elif b > 0:
        s = "B"
    elif g > 0:
        s = "G"
    elif v > 0:
        s = "V"
    elif o > 0:
        s = "O"

    cnt[s[-1].lower()] -= 1
    d = {"R":red, "Y":yellow, "B":blue, "G":green, "V":violet, "O":orange}
    for i in xrange(n-1):
        c = d[s[-1]](s)
        if not c:
##            print s, cnt
            return "IMPOSSIBLE"
        s += c
    if is_legal(s[0].lower(), s[-1].lower()):
        return s
    print s
    return "IMPOSSIBLE"
        
def main(fname):
    in_fd = open(fname, "rb")
    out_fd = open(fname + ".out", "wb")
    t = int(in_fd.readline().strip())
    for i in xrange(t):
        n, r, o, y, g, b, v = map(int, in_fd.readline().strip().split(" "))        
        result = unicorn(n, r, o, y, g, b, v)
        out_fd.write("Case #%d: %s\n" % (i+1, result))
    in_fd.close()
    out_fd.close()
