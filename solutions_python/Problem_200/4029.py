import sys


def is_tidy(num):
    n_str = str(num)
    s = list(sorted(n_str))

    if '0' in s:
        return False

    num_sorted = int(''.join(s))
    #num_sorted = ''.join(s)
    return num_sorted == num

with open(sys.argv[1], 'r') as f:
    next(f)
    case = 1
    for line in f:
        num = int(line)
        for i in range(num,0,-1):
            #print("verifying %d" % (i,))
            if is_tidy(i):
                print ("Case #%d: %d" % (case,i))
                break

        case = case + 1

