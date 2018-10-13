# forgive me for this mess of code, since i'm tired after a long distance hiking

encode = """
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
yeqz
"""

decode = """
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
aozq
"""

encoding = {}
#map(lambda x: encoding.append[x[0]] = x[1], zip(encode, decode))
for i in range(len(encode)):
    encoding[encode[i]] = decode[i]
    
T = int(input())
for t in range(T):
    G = input()
    Gx = list(map(lambda x: encoding[x], G))
    print("Case #%d: %s" %(t + 1, "".join(Gx)))


