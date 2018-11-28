h = {}

def alphabet(strr):
    s = [h[y] for y in strr[:-1]]
    return "".join(s)

if __name__ == "__main__":
    src = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv qz"
    des = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up zq"
    for j in range(len(src)):
        h[src[j]] = des[j]
    fn = open("A-small-attempt0.in","r")
    tcase = int(fn.readline())
    for x in range(tcase):
        print "Case #%d: %s" % (x+1, alphabet(fn.readline()))
