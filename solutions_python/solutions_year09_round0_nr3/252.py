goal_str = 'welcome to code jam'
goal_str_len = len(goal_str)

def find(ch, _str):
    return [i for i, s in enumerate(_str) if s==ch]

def build_dict(_str):
    ch_set = set([s for s in goal_str])
    _dict = dict()
    for ch in ch_set:
        _dict[ch] = find(ch, _str)
    return _dict

def substr_count(ind, last, _dict, count):
    if ind<goal_str_len:
        ch = goal_str[ind]
        _next = [x for x in _dict[ch] if x > last]
        if _next==[]:
            return
        else:
            for n in _next:
                substr_count(ind+1, n, _dict, count)
    else:
        count[0]=count[0]+1
        return

def solve(_str):
    _dict = build_dict(_str)
    _r = [0]
    substr_count(0, -1, _dict, _r)
    ans = _r[0] % 10000
    return str(ans).zfill(4)

    
fin = open('C-small-attempt1.in', 'r')
fout = open('out.txt', 'w')
N = int(fin.readline())
for i in range(1, N+1):
    s = solve(fin.readline())
    print('Case #%d: %s'%(i, s))
    fout.write('Case #%d: %s\n'%(i, s))
fout.close()
fin.close()

    
