import sys

goal = "welcome to code jam"
chars = sorted(list(set(goal)))
index = dict([(c,i) for (i,c) in enumerate(chars)])
goalIndices = [index[c] for c in goal]

count = 0

def offsets(s):
    offsets = [list() for _ in range(len(chars))]
    for o,c in enumerate(s):
        if index.has_key(c):
            offsets[index[c]].append(o)
    return offsets

def after(i, o):
    return [filter(lambda x:x>i, l) for l in o]

def find_subseqs(s, o):
    global count
    if not s:
        count += 1
        return
    else:
        for i in o[s[0]]:
            find_subseqs(s[1:], after(i,o))

def count_string_subseqs(s):
    global count
    o = offsets(s)
    if not all(o):
        return 0
    count = 0
    find_subseqs(goalIndices, o)
    return count

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    lines = sys.stdin.readlines()

    for n, line in enumerate(lines):
        k = count_string_subseqs(line.strip())
        print "Case #%d: %04d" % (n+1, k%10000)
