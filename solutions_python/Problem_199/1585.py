def flip(bit):
    if bit == "+":
        return "-"
    else:
        return "+"

def flip_pancakes(pancakes, k):
    i_list = list(pancakes)
    changes = 0

    if('-' in i_list):
        while(True):
            try:
                pos = i_list.index('-')
            except:
                break

            if(pos <= len(i_list)-k):
                for j in range(k):
                    i_list[pos+j] = flip(i_list[pos+j])
                #print(i_list)
                changes += 1
            else:
                changes = "IMPOSSIBLE"
                break

    return changes
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  pancakes, k = input().split(" ")
  print("Case #{}: {}".format(i, flip_pancakes(pancakes, int(k))))
  # check out .format's specification for more formatting options
