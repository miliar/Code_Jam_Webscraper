# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
def main():
  t = int(input())  # read a line with a single integer
  for i in range(1, t + 1):
    n = input().split(" ")[0]  # read a list of integers, 2 in this case
    print("Case #{}: {}".format(i, tide(n)))
    # check out .format's specification for more formatting options
 

def non_decreasing(number_str):
  if len(number_str) == 1:
    return True
  for i in range(len(number_str)): 
    if i == len(number_str)-1:
      return True
    else:
      if number_str[i] > number_str[i+1]:
        return False

def tide(number_str):
  while non_decreasing(number_str) is False:
    number_str = str(int(number_str)-1)
  return number_str

main()
