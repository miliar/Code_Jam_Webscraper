import sys

sys.setrecursionlimit(1500)

val = {
        'i':'i',
        'j':'j',
        'k':'k',
        '-i':'-i',
        '-j':'-j',
        '-k':'-k',
        '1':'1',
        '-1':'-1',
        '1i':'i',
        '1j':'j',
        '1k':'k',
        '-1i':'-i',
        '-1j':'-j',
        '-1k':'-k',
        'ii':'-1',
        'ij':'k',
        'ik':'-j',
        '-ii':'1',
        '-ij':'-k',
        '-ik':'j',
        'ji':'-k',
        'jj':'-1',
        'jk':'i',
        '-ji':'k',
        '-jj':'1',
        '-jk':'-i',
        'ki':'j',
        'kj':'-i',
        'kk':'-1',
        '-ki':'-j',
        '-kj':'i',
        '-kk':'1'
    }

def solve(string, start=0, search='i'):
    ans = ''
    while start < len(string):
        ans += string[start]
        if len(ans) == 2 or len(ans) == 3:
            ans = val[ans]
        if ans == search and search != 'k':
            break
        start += 1

    if start == len(string) and ans != search:
        return False

    return True if search == 'k' else solve(string, start + 1, 'j' if search == 'i' else 'k')


T = int(raw_input())
for t in range(1, T+1):
    ans = 'NO'
    L, X = [ int(x) for x in str(raw_input()).lstrip().rstrip().split(' ')]
    string = str(raw_input()).lstrip().rstrip()
    string = string * X
    if len(string) < 3:
        ans = 'NO'
    else:
        ans = 'YES' if solve(list(string)) else 'NO'

    print 'Case #%d: %s' % (t, ans)
