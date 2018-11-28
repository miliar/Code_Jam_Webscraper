import os.path

with open(os.path.expanduser('~/Downloads/A-large.in'), 'r') as f:
    lines = f.read().strip().split('\n')

def nl(): return lines.pop(0).split()

T = int(nl()[0])

for case in range(T):
    s_max, s_tally = nl()
    s_max = int(s_max)
    s_tally = list(map(int, list(s_tally)))
    
    needed = 0
    have = 0
    for s, c in enumerate(s_tally):
        if have < s:
            needed += s-have
            have = s
        have += c
    
    print('Case #{}: {}'.format(case+1, needed))