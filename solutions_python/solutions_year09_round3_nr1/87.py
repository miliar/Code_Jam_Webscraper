def find_num_symbols(s):
    sym = 0
    for i, c in enumerate(s):
        if c not in s[i+1:]:
            sym = sym + 1
    return sym

def assign_vals(s):
    vals = {}
    vals[s[0]] = 1
    avail = [i for i in range(16) if i != 1]
    avail.reverse()
    for c in s:
        if not vals.has_key(c):
            vals[c] = avail.pop()
    return vals

def evaluate(s, vals, base):
    val = 0
    mul = 1
    for c in range(len(s)-1, -1, -1):
        val = val + mul * vals[s[c]]
        mul = mul * base
    return val
        

T = int(raw_input())

for t in range(T):
    s = raw_input()
    basemin = find_num_symbols(s)
    if basemin <= 1: basemin = 2
    vals = assign_vals(s)
    out = min([evaluate(s, vals, b) for b in range(basemin, 17)])
    print "Case #%d: %d" % (t+1, out)

