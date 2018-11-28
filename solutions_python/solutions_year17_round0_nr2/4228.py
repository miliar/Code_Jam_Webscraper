

def tidy(x):
    i = x % 10
    x //= 10
    while x != 0:
        if i < (x % 10):
            return False
        i = x % 10
        x //= 10
    return True


def answer(x):
    i = 1
    answer = 1
    while i <= x:
        if tidy(i):
            answer = i
        i += 1
    return answer



# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  x = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
  print("Case #{}: {}".format(i, answer(x[0])))
  # check out .format's specification for more formatting options


