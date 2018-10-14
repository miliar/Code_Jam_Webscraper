
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  # n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
  #print("starting",i)
  starting_number = int(input())

  for current_number in range(starting_number ,0, -1):
    tidy = 1
    current_digit_index = len(str(current_number))-1
    current_digit = str(current_number)[current_digit_index]
    #print("current number/dig" ,current_number ,current_digit)
    while current_digit_index > 0 and tidy == 1:
      next_digit_index = current_digit_index - 1
      current_digit = int(str(current_number)[current_digit_index])
      next_digit = int(str(current_number)[next_digit_index])
      #print("current number/dig/dig", current_number, current_digit,next_digit)
      if (current_digit < next_digit):
          tidy = 0
      current_digit_index = next_digit_index
    if tidy == 1:
        print("Case #{}: {}".format(i, current_number))
        break



  # check out .format's specification for more formatting options
