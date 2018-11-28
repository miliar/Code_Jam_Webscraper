s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
p1 = "our language is impossible to understand"
s2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
p2 = "there are twenty six factorial possibilities"
s3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"
p3 = "so it is okay if you want to just give up"

to = ['0'] * 2600

def go(s, p):
    for i in range(len(s)):
        to[ord(s[i])] = p[i]


to[ord(' ')] = ' '
to[ord('q')] = 'z'
to[ord('z')] = 'q'
go(s1, p1)
go(s2, p2)
go(s3, p3)


def trans(s):
    return ''.join(map(lambda x: to[ord(x)], s))

n = input()
for i in range(n):
    print ("Case #" + str(1+i) + ": " + trans(raw_input()))

