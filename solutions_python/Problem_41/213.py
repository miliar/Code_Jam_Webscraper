import sys
filename = sys.argv[1]
f = open(filename)

def filter_zero(avail_list):
    for k,v in avail_list.items():
        if v == 0:
            del avail_list[k]
    
    return avail_list
    
def make_avail_list(inp):
    avail_list = dict([(i, 0) for i in range(10)])
    for i in inp:
        avail_list[int(i)] += 1

    avail_list = filter_zero(avail_list)
    if not avail_list.get(0):
        avail_list[0] = 1

    return avail_list

def check_valid(num, avail_list):
    for c in `num`:
        if c == '0':
            continue
        c = int(c)
        if avail_list.get(c):
            avail_list[c] -= 1
            if avail_list[c] == 0:
                del avail_list[c]
        else:
            return False

    if len(avail_list) != 1:
        return False
    else:
        return True

def find_next(num, avail_list):
    max = 10 ** 7
    num += 1
    while num <= max and not check_valid(num, dict(avail_list)):
        num += 1
    
    return num

T = int(f.readline())
for x in range(T):
    num = int(f.readline().strip())
    print "Case #%d: %s" % (x+1, find_next(num, make_avail_list(`num`)))
