import os


def parse_input(input_string):
    lines = input_string.split("\n")
    number_of_inputs = int(lines[0])

    cases = []
    for line in lines[1:]:
        input = line.split(" ")
        pancakes = [1 if i == '+' else 0 for i in input[0]]
        flipper_size = int(input[1])
        cases.append((tuple(pancakes), flipper_size))
    return cases


def flip(pancakes):
    return [1-p for p in pancakes]


def permutations(pancakes, flipper_size):
    perms = []
    for i in xrange(len(pancakes)):
        start = i
        end = i + flipper_size
        if end <= len(pancakes):
            if not all(p==1 for p in pancakes[start:end]):
                perms.append((start, end))
    return perms


def get_new_pancakes(pancakes, start, end):
    sub_pancakes = pancakes[start:end]
    flipped_sub_pancakes = flip(sub_pancakes)
    new_pancakes = list(pancakes)
    new_pancakes[start:end] = flipped_sub_pancakes
    return tuple(new_pancakes)


def flip_pancakes(pancakes, flipper_size):
    seen_states = {pancakes}

    to_try = [(0, pancakes)]
    for flips, pp in to_try:
        if all(p==1 for p in pp):
            return flips

        for s,e in permutations(pp, flipper_size):
            new_pancakes = get_new_pancakes(pp, s, e)
            if new_pancakes not in seen_states:
                to_try.append((flips+1, new_pancakes))
                seen_states.add(new_pancakes)
    return "IMPOSSIBLE"


def main():
    with open('data.txt', 'r') as f:
        input = f.read()

    cases = parse_input(input)

    total_output = ""
    for i, case in enumerate(cases):
        result = flip_pancakes(*case)
        output = "Case #{i}: {result}\n".format(result=result, i=i+1)
        print output
        total_output += output

    with open('out.txt', 'w') as f:
        f.write(total_output)


if __name__ == "__main__":
    main()
