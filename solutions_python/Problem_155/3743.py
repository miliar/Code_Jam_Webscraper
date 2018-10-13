def solve_input(lst):
    needed = 0
    people_up = 0
    for i in range(len(lst)):
        if (people_up + needed) < i:
            needed += i - (people_up + needed)
        people_up += lst[i]
    return needed

with open('A-small-attempt0.in') as input_file:
    input_list = input_file.read().splitlines()[1:]
    with open('out.txt', 'w') as output_file:
        for idx, case in enumerate(input_list):
            output = solve_input([int(val) for val in case[2:]])
            output_file.write("Case #{}: {}\n".format(idx+1, output))
