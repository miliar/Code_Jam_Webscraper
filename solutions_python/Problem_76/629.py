from tools import *
import sys

def sean_sum(lst):
    return sum(lst)

def patrick_sum(lst):
    ret = lst[0]
    for i in lst[1:]:
        ret = ret ^ i
    return ret

def divide(l, n):
    return [l[:n], l[n:]]

def do(lst):
    lst.sort(reverse=True)
    ret = []
    for i in xrange(1, len(lst)):
        tmp = divide(lst, i)
        if sum(tmp[1]) <= sum(tmp[0]) and patrick_sum(tmp[1]) == patrick_sum(tmp[0]):
            ret.append(sum(tmp[0]))
    if ret != []:
        return str(max(ret))
    else:
        return "NO"

lines = read_file(sys.argv[1]) 
del lines[0]
ret = []
for i in xrange(1, len(lines), 2):
    ret.append(do(map(int, lines[i].split(" "))))
write_file(insert_case(ret), "out")
