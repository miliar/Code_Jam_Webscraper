def bathroom_stalls(rooms, people):
    if rooms == 1 and people == 1:
        return 0, 0
    elif rooms > 1 and people == 1:
        if rooms % 2 == 0:
            ls = (rooms / 2) - 1
            return int((rooms - ls - 1)), int(ls)  # max(ls, rs), min(ls, rs)
        else:
            return int((rooms - 1) / 2), int((rooms - 1) / 2)
    elif rooms % 2 == 0 and people % 2 == 0:
        rooms = (rooms / 2)
        return bathroom_stalls(rooms, people / 2)
    elif rooms % 2 == 0 and people % 2 != 0:
        rooms = (rooms / 2) - 1
        return bathroom_stalls(rooms, (people - 1) / 2)
    elif rooms % 2 != 0 and people % 2 == 0:
        rooms = (rooms - 1) / 2
        return bathroom_stalls(rooms, people / 2)
    elif rooms % 2 != 0 and people % 2 != 0:
        rooms = (rooms - 1) / 2
        return bathroom_stalls(rooms, (people - 1) / 2)


if __name__ == '__main__':
    # print(bathroom_stalls(6, 2))
    input_file = open('C-small-2-attempt0.in')
    output_file = open('C-small-2-attempt0-out.in', 'w')
    lines = [line.rstrip('\n') for line in input_file]
    for i, stack in enumerate(lines):
        if i == 0:
            continue
        else:
            stall = int(stack.split()[0])
            people = int(stack.split()[1])
            output_file.write(
                "Case #{}: {} {}\n".format(i, bathroom_stalls(stall, people)[0], bathroom_stalls(stall, people)[1]))

