def dict_add(d, key, amount):
    if key == 0:
        return
    if key in d:
        d[key] += amount
    else:
        d[key] = amount

def dict_nextgen(kv):
    nkv = {}
    for key in kv:
        val = kv[key]
        dict_add(nkv, (key-1)/2, val)
        dict_add(nkv, key/2, val)
    return nkv

T = int(raw_input())
for t in xrange(1, T+1):
    n, k = map(int, raw_input().split())
    kv = {n:1}
    z = 1
    while k > z:
        kv = dict_nextgen(kv)
        k -= z
        z <<= 1
    maxkey, minkey = max(kv), min(kv)
    ans = maxkey if kv[maxkey] >= k else minkey
    print "Case #%d: %d %d" % (t, ans/2, (ans-1)/2)
