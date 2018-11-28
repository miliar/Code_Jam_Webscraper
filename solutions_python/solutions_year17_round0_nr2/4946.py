import sys
sys.setrecursionlimit(115000)
t = int(input())

def calculate(x):
    seq = [int(i) for i in str(x)]
    ans = all(earlier <= later for earlier, later in zip(seq, seq[1:]))
    if ans==True:
        big_no = int("".join(str(i) for i in seq))
        print("Case #%d:" % int(i+1 ), big_no)
        return big_no
    else:
        x = x-1
        calculate(x)




for i in range(t):
    x = int(input())
    calculate(x)
#    if y==None:
#        x = x-1
#        print(x)
#        y = calculate(x)
#    else:
#        print(y)
