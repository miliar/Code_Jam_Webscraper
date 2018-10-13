import sys

def get_non_decrease(s):
    if len(s) <= 1:
        return s
    cur = int(s[-1])
    cnt_9 = 0
    replace = -1
    for i in range(2, len(s) + 1):
        check = int(s[len(s) - i])
        if check <= cur:
            cur = check
        else:
            cur = int(s[len(s) - i]) - 1
            replace = cur
            cnt_9 = i - 1

    if replace == -1:
        return s
    #print "{} {}".format(cur, cnt_9)    
    nines = "".ljust(cnt_9, '9')
    #print nines
    #print s[0 : len(s) - cnt_9 - 1]
    s = s[0 : len(s) - cnt_9 - 1] + str(replace) + nines
    #print s
    if (s[0] == '0'):
        return s[1:]
    return s

t = int(raw_input())
for i in xrange(1, t + 1):
  s = raw_input()
  
  s = get_non_decrease(s)
  print ("Case #{}: {}".format(i, s))

