def mod(k):
    r = ""
    for i in range(len(k) - 1):
        if k[i] <= k[i+1]:
            r += k[i]
            continue
        r += str(int(k[i]) - 1) if k[i] != "0" else "0"
        r += "9" * (len(k) - i - 1)
        break
    else:
        r += k[-1]
    return r

for q in range(1, input() + 1):
    k = raw_input()
    r = ""
    while r != k:
        r = k
        k = mod(k)
    r = r.lstrip("0")
    if not r:
        r = "1"
    print "Case #%s: %s" % (q, r)
