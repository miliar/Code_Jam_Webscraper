t = input()

# partition generator from online
def k_subset(s, k):
    if k == len(s):
        return (tuple([(x,) for x in s]),)
    k_subs = []
    for i in range(len(s)):
        partials = k_subset(s[:i] + s[i + 1:], k)
        for partial in partials:
            for p in range(len(partial)):
                k_subs.append(partial[:p] + (partial[p] + (s[i],),) + partial[p + 1:])
    return k_subs
    
from string import ascii_uppercase

def make_trie():
    return {}
    
def insert(trie, word):
    if word:
        le = word[0]
        if le in trie:
            insert(trie[le], word[1:])
        else:
            trie[le] = dict()
            insert(trie[le], word[1:])
    
def count(trie):
    k = len(trie.keys())
    total = k
    for key in trie:
        total += count(trie[key])
    return total
    
def num_nodes(strs):
    t = make_trie()
    for w in strs:
        insert(t, w)
    return count(t)

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
    
def uniq_subsets(s):
    u = set()
    for x in s:
        t = []
        for y in x:
            y = list(y)
            y.sort()
            t.append(tuple(y))
        t.sort()
        u.add(tuple(t))
    return u
    
def scores(strs):
    ss_gen = uniq_subsets(k_subset(strs, n))
    scores = {}
    b = 0
    for ss in ss_gen:
        t = 0
        for s in ss:
            t += num_nodes(s)
        if t not in scores:
            scores[t] = 1
        else:
            scores[t] += 1
        b = max(t, b)
    return b+n, scores[b]*fact(n)
    
for case in xrange(1, t+1):
    m, n = map(int, raw_input().split())
    strs = []
    for _ in xrange(m):
        strs.append(raw_input())
    q, w = scores(strs)
    print "Case #%d: %d %d" % (case, q, w)