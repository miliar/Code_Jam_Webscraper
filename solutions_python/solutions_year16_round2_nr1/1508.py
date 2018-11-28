t = int(raw_input())  # read a line with a single integer

def remove(string, d, m):
    for i in string:
        d[i] = d.get(i) - m

def ans(s):
    s = s.lower()
    d = {}
    for a in s:
        d[a] = d.get(a, 0) + 1

    ans = []
    # one, nine

    if d.get("z", 0) > 0:
        ans += d.get("z")*[0]
        remove("zero", d, d.get("z"))
    if d.get("w", 0) > 0:
        ans += d.get("w")*[2]
        remove("two", d, d.get("w"))
    if d.get("u", 0) > 0:
        ans += d.get("u")*[4]
        remove("four", d, d.get("u"))
    if d.get("x", 0) > 0:
        ans += d.get("x")*[6]
        remove("six", d, d.get("x"))
    if d.get("f", 0) > 0:
        ans += d.get("f")*[5]
        remove("five", d, d.get("f"))
    if d.get("v", 0) > 0:
        ans += d.get("v")*[7]
        remove("seven", d, d.get("v"))
    if d.get("g", 0) > 0:
        ans += d.get("g")*[8]
        remove("eight", d, d.get("g"))
    if d.get("h", 0) > 0:
        ans += d.get("h")*[3]
        remove("three", d, d.get("h"))
    if d.get("o", 0) > 0:
        ans += d.get("o")*[1]
        remove("one", d, d.get("o"))
    ans += d.get("i", 0)*[9]

    ans.sort()
    ans = map(str, ans)
    # print s
    # print d

    return "".join(ans)

    # return 0


for i in xrange(1, t + 1):
    s = raw_input()
    res = ans(s)

    print "Case #{}: {}".format(i, res)
