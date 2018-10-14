# usage:  (python3 a.py < a.in) > a.out
import time, sys, inspect

lineno = lambda: inspect.currentframe().f_back.f_back.f_lineno
print = lambda *a, **k: __builtins__.print(str(lineno())+':', *a, file=sys.stderr, **k)

#---------------------------------------------

'''

'''

def run(data):
    r, c, data = data
    print(data)

    # fill a single row naturally

    for i in range(r):
        if data[i] == '?' * c:
            continue
        default_char = [x for x in data[i] if x != '?'][0]
        for j in range(c):
            if data[i][j] != '?':
                continue
            # find char to place at (i,j)
            prev_char = ([default_char] + [x for x in data[i][:j] if x != '?'])[-1]
            data[i] = data[i][:j] + prev_char + data[i][j+1:]

    # fill in empty rows by dupe-ing neighs
    for i in range(r):
        if data[i] == '?' * c:
            for j in range(i+1, r):
                if data[j] != '?' * c:
                    data[i] = data[j]
                    break
            for j in range(i-1, -1, -1):
                if data[j] != '?' * c:
                    data[i] = data[j]
                    break

    return '\n' + '\n'.join(data)

#---------------------------------------------

def read_case():
    r, c = [int(k) for k in list(input().split())]
    return (r, c, [input() for i in range(r)])

for i in range(int(input())):
    outstr = 'Case #'+str(i+1)+': '+str(run(read_case()))
    print(outstr, ' @ t =', time.clock())
    __builtins__.print(outstr)
