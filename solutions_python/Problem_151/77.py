infile = open("D-small-attempt0.in", "rU")
outfile = open("D.out", "w")

from collections import defaultdict

ncases = int(infile.readline())

def trie_size(strings):
    trie = set([])

    for s in strings:
        for i in xrange(0, len(s)+1):
            trie.add(s[:i])

    return len(trie)

def solve(strings, trie_scores, servers):
    if len(strings) == 0:
        score = 0

        for i in servers:
            score += trie_size(i)

        trie_scores[score] += 1
        return
    
    s = strings.pop()

    for a in xrange(len(servers)):
        server_copy = []

        for j in xrange(len(servers)):
            server_copy.append(servers[j][:])

        server_copy[a].append(s)

        strings_copy = strings[:]        

        solve(strings_copy, trie_scores, server_copy)

for case in xrange(1, ncases + 1):
    m, n = [int(x) for x in infile.readline().strip().split(" ")]

    strings = []
    for i in xrange(m):
        strings.append(infile.readline().strip())

    trie_scores = defaultdict(int)
    servers = []

    for i in xrange(n):
        servers.append([])

    solve(strings, trie_scores, servers)

    scores = []

    for i in trie_scores:
        scores.append((i, trie_scores[i]))

    scores.sort()
    scores.reverse()

    outfile.write("Case #%d: %d %d\n" % (case, scores[0][0], scores[0][1] % 1000000007))
    
infile.close()
outfile.close()
