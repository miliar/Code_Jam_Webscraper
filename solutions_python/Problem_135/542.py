def get_items():
    x = raw_input()
    return x.split(' ')

def get_item():
    return get_items()[0]

def get_nums():
    return [int(x) for x in get_items()]

def get_num():
    return int(get_item())

def solve():
    arr1, arr2 = [], []
    r1 = get_num() - 1
    for i in xrange(4): arr1.append(get_nums())
    r2 = get_num() - 1
    for i in xrange(4): arr2.append(get_nums())
    ans = set(arr1[r1]) & set(arr2[r2])
    if len(ans) == 1:
        return list(ans)[0]
    elif ans:
        return "Bad magician!"
    else:
        return "Volunteer cheated!"
    
for tc in xrange(1, get_num() + 1):
    print "Case #{}: {}".format(tc, solve())
    