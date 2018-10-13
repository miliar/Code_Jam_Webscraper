
T = int(raw_input())

def remove_dups(s):
    cur = ''
    ret = ''
    for c in s:
        if c != cur:
            ret += c
            cur = c
    return ret

def count(s):
    cur = s[0]
    ret = []
    cur_count = 1
    for c in s[1:]:
        if c != cur:
            ret.append(cur_count)
            cur_count = 1
            cur = c
        else:
            cur_count += 1
    ret.append(cur_count)
    return ret

def min_moves(nums):
    ret = 1000
    for i in range(min(nums), max(nums) + 1):
        ret = min(ret, sum([abs(n-i) for n in nums]))
    return ret

for i in range(1, T+1):
    N = int(raw_input())
    strings = []
    for j in range(N):
        strings.append(raw_input())
    
    base = remove_dups(strings[0])
    possible = True
    for s in strings[1:]:
        if remove_dups(s) != base:
            possible = False
    if not possible:
        print "Case #{}: Fegla Won".format(i)
        continue
            
    nums = [count(s) for s in strings]
    moves = 0
    for j in range(len(base)):
        moves += min_moves([n[j] for n in nums])    

    print "Case #{}: {}".format(i, moves)
