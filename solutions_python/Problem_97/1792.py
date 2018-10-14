import sys

N = sys.stdin.readline()

def allsame(n):
    last = str(n)[0]
    for i in range(1, len(str(n))):
        if str(n)[i] != last:
            return True
        last = str(n)[i]
    return False

def go(n):
    ctr = 0
    s = str(n)
    for i in range(0, len(str(n)) + 1):
        s = s[1:] + s[0:1]
        str2 = str(n) + " " + str(int(s))
        str3 = str(int(s)) + " " + str(n)
        if (int(s) != n and allsame(s) and len(str(int(s))) == len(s) \
                and int(s) >= int(a) and int(s) <= int(b) \
                and not st.__contains__(str2) \
                and not st.__contains__(str3)):
            ctr += 1
            str1 = str(n) + " " + str(int(s))
            str4 = str(int(s)) + " " + str(n)
            st.add(str1)
            st.add(str4)
    return ctr;

for i in range(0, int(N)):
    string = sys.stdin.readline()
    global a
    global b
    global st
    st = set([])
    a = string[:string.find(' ')]
    b = string[string.find(' ') + 1:]
    out = 0
    for x in range(int(a), int(b) + 1):
        out += go(x)
    print "Case #%d:" % (i + 1),
    print out
