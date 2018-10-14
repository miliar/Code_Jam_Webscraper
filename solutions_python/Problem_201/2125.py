data = open('c.in', 'r').readlines()
data = data[1:]
import math

output = ""


def get_slices(num):
    # import pdb; pdb.set_trace()
    return [int(math.floor((num-1) / 2.0)), int(math.ceil((num -1) / 2.0))]


for i in range(len(data)):
    stall_spaces = []
    stalls, people = map(int, data[i].split())
    if people == 1:
        result = get_slices(stalls)
    else:
        stall_spaces.append(stalls)
        for j in range(people-1):
            next_space = stall_spaces.pop()
            stall_spaces += get_slices(next_space)
            stall_spaces = list(sorted(stall_spaces))
        next_space = stall_spaces.pop()
        result = get_slices(next_space)
    output += "Case #{}: {} {}\n".format(i + 1, max(result), min(result))

f = open('c.out', 'w')
f.write(output)
