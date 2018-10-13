# Problem B
import sys, os

T = int(sys.stdin.readline())

for t in range(T):
    nums = list(map(int, sys.stdin.readline().split()))
    waste = nums[0]; #print(n)
    s = nums[1]; #print(s)
    n = nums[2]; #print(p)
    #print ("n={n} s={s}".format(n=n, s=s))
    normal = 3 * n -2
    anomal = 3 * n -4
    total = 0
    for score in nums[3:]:
        if score >= normal:
            total += 1
            #print ("score={s} norm={n} total={t}".format(s=score, n=normal, t=total))
        else:
            if (anomal>0 and score >= anomal):
                total += 1
                s -= 1
             #   print ("score={s} norm={n} s={a} total={t}".format(s=score, n=normal, a=s, t=total))
    if s < 0: total += s 
    print ("Case #{i}: {n}".format(i=1+t, n=total))
