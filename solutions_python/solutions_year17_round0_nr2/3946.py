import sys


def tidy(x):
    if len(x) == 1:
        return x

    gt_successor = None
    for i in range(len(x)-2, -1, -1):
        if x[i] > x[i+1]:
            gt_successor = i
            break
    if gt_successor == None:
        return x
    
    pre = x[:gt_successor]
    dec = str(int(x[gt_successor]) - 1)
    post = (len(x) - 1 - gt_successor) * '9'
 
    full = pre + dec + post
    return tidy(full)

first = True
case = 0
for val in sys.stdin:
    val = val.rstrip()
    if first:
        first = False
        continue
    case += 1
    print "Case #" + str(case) + ": " + str(int(tidy(val)))
