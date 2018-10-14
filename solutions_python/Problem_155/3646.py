#!/usr/bin/env python3

def all_clap(max_shyness, people, extras=0):
    num_clapping = 0
    for level, num_with_level in enumerate(people):
        if level == 0:
            num_clapping = num_with_level
        elif level <= num_clapping:
            num_clapping += num_with_level
    if num_clapping >= max_shyness:
        return extras
    else:
        extras += 1
        people[0] = people[0] + 1
        return all_clap(max_shyness, people, extras)

if __name__ == '__main__':
    num_cases = int(input())
    for x in range(num_cases):
        line = input()
        max_shyness = int(line[0])
        people = list(map(int, list(line[2:])))
        extras = all_clap(max_shyness, people)
        print("Case #" + str(x + 1) + ": " + str(extras))
