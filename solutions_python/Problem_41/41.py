#!/usr/bin/python
import sys

def get_d(N):

    d = {}
    for c in N:
        digit = int(c)
        if digit in d:
            d[digit] += 1
        else:
            d[digit] = 1

    return d

def calc_ans(N):

    # Search for first switch:
    str_N = str(N)
    for i in range(len(str_N)-2,-1,-1):
        if int(str_N[i])<int(str_N[i+1]):
            d = get_d(str_N[i:])

            keys = d.keys()
            keys.sort()

            new_str = list(str_N[:i])

            for key in keys:
                if key > int(str_N[i]):
                    new_str.append(str(key))
                    d[key] -= 1
                    break

            for k in keys:
                for times in range(d[k]):
                    new_str.append(str(k))
            return int("".join(new_str))

    d = get_d(str(N))

    keys = d.keys()
    keys.sort()

    # Search a switch
    ret_str = ""
    for k in keys:
        if k != 0:
            ret_str += str(k) *d[k]
    if 0 in keys:
        zeros = 1 + d[0]
    else:
        zeros = 1

    ret_str = ret_str[0] + ("0" * zeros) + ret_str[1:]

    return int(ret_str)

def main():
   handle = file(sys.argv[1])
   lines_no = int(handle.readline())
   for line_no in xrange(1,lines_no+1):
      N = int(handle.readline())
      print "Case #%d: %d" % (line_no, calc_ans(N))

main()
