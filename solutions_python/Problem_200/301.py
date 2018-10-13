T = int(raw_input())

class Fail: pass

def doit(s):
    if len(s)==1:
        return s
    if s[1]>=s[0]:
        try:
            return s[0] + doit(s[1:])
        except Fail:
            if s[1]==s[0]:
                raise Fail
            return s[0] + chr(ord(s[1])-1) + ("9"*(len(s)-2))
    else:
        raise Fail

for ts in range(1,T+1):
    s = "0" + raw_input()
    print "Case #%s: %s" % (ts, int(doit(s)))
