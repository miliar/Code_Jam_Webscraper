g = "qz ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
s = "zq our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

d = str.maketrans(g,s)

t, T = 0, int(input())
while t != T:
    t += 1

    print("Case #%d:" % t, input().translate(d))
            
