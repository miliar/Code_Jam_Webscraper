def find_max(n):
    found = False
    x = 10
    while not found:
        if ((x-1)*2 + x) > n:
            x -= 1
        else:
            a = [x,x,x]
            pos = 0
            while sum(a) != n:
                a[pos] -= 1
                pos += 1
            return a
        
def count_max(s, p):
    t = 0
    for score in s:
        if max(score) >= p:
            t += 1
    return t

def fix(s):
    if s[0] == s[1] == s[2]:
        return [s[0]-1, s[1], s[2] +1]
    elif s[0] == s[1]:
        return [s[0]-1, s[1]+1, s[2]]
    else:
        return [s[0], s[1]-1, s[2]+1]

def make_special(s, p, S):
    need_fix = True
    n_s = []
    for score in s:
        if S == 0:
            need_fix = False
        if need_fix:
            if max(score) < p:
                if (score[0] + score[1]) > 0:
                    score = fix(score)
                    S -= 1
        n_s.append(score)
    if S == 0:
        return n_s
    s = []
    need_fix = True
    for score in n_s:
        if S == 0:
            need_fix = False
        if need_fix:
            score = fix(score)
            S -= 1
        s.append(score)
    return s
                

def solve(N,S,p,total_scores):
    possible_score = []
    for s in total_scores:
        possible_score.append(find_max(s))
    possible_score.sort(reverse=True)
    scores = make_special(possible_score, p, S)
    return count_max(scores, p)

fin = file('B-large.in', 'r')
fout = file('file.out', 'w')
count = int(fin.readline())
for c in range(count):
    row = fin.readline().strip('\n').split()
    N,S,p = map(int, row[:3])
    total_scores = map(int, row[3:])
    solution = solve(N,S,p,total_scores)
    fout.write('Case #%d: %s\n' % (c+1, solution))
