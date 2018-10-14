# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
F = open("result.in", 'w')
for i in range(1, t + 1):
    pencakes, num = [s for s in input().split(" ")]  # read a list of integers, 2 in this case
    num = int(num)
    pencakes = list(pencakes)
    try:
        left_index = pencakes.index('-')
    except ValueError:
        left_index = -1
    counter = 0
    while left_index >= 0:
        if len(pencakes) - left_index >= num:
            for change in range(num):
                if(pencakes[left_index+change] == '+'):
                    pencakes[left_index + change] = '-'
                else:
                    pencakes[left_index + change] = '+'
            try:
                left_index = pencakes.index('-')
            except ValueError:
                left_index = -1
            counter += 1
        else:
            counter = 'IMPOSSIBLE'
            break
    F.write("Case #{}: {}\n".format(i, counter))
    # check out .format's specification for more formatting options

F.close()



