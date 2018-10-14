#!/usr/bin/python
import sys
def get_time(num):
    """docstring for get_time"""
    nums = list("0123456789abcdefghijklmnopqrstuvwxyz !\"#$%&'()*+,./:;<=>?@[\]^_`{|}~")
    syms = list(num)
    map = {}
    map[syms[0]] = '1'
    nums.remove('1')
    for sym in syms:
        if sym not in map:
            new = nums[0]
            map[sym] = new
            nums.remove(new)
    newsym = ""
    print map
    for sym in syms:
        newsym = newsym + map[sym]
    base = len(map)
    if base == 1:
        base = 2

    return  int(newsym, base)


def main():
    """docstring for main"""
    f = file(sys.argv[1])
    lines = f.readlines()
    n = int(lines[0].strip())
    f2 = file(sys.argv[1] + ".out", "w")
    lno = 1
    for case in range(n):
        l = lines[lno].strip()
        lno = lno + 1
        ans = get_time(l)
        print "Case #%d: %d" % (case+1, ans)
        f2.write("Case #%d: %d\n" % (case+1, ans))

    f2.close()
if __name__ == '__main__':
    main()  
