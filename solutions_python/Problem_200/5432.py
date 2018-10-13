# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
def maketidy(num):
    test = 10
    a = num
    while(test >= 10):
        test = checktidy(a)
        if test >= 10:
            a -= 1

    return a

def checktidy(num):
    if num < 10:
        return num
    else:
        if (num%10) >= checktidy(num / 10):
            return num%10
        else:
            return num+10


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n = int(input())  # read a list of integers, 2 in this case
  m = maketidy(n)

  print("Case #{}: {}".format(i, m))
  # check out .format's specification for more formatting options
