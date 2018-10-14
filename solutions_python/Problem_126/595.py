import sys
import itertools

def find_consecutive_consonants(substrings, n):
    vowels = ['a', 'e', 'i', 'o', 'u']
    counter = 0
    for string in substrings:
        strings = [string]
        for vowel in vowels:
            strings = [sub.split(vowel) for sub in strings]
            strings = list(itertools.chain(*strings))
        has_sub = False
        for sub in strings:
            if len(sub) >= n:
                has_sub = True
                break
        if has_sub: counter += 1

    return counter


def find_n_value(name, n):
    n_value = 0
    substrings = [name[start:end] for start in range(0, len(name) + 1)
                  for end in range(start + 1, len(name) + 1)
                  if (end - start) >= n]
    n_value += find_consecutive_consonants(substrings, n)

    return n_value

input = open(sys.argv[1], 'r')
output = open('output.txt', 'w+')

num_tests = int(input.readline())

for case in range(1, num_tests + 1):
    line = input.readline().strip().split()
    name = line[0]
    n = int(line[1])
    n_value = find_n_value(name, n)
    message = "Case #{0}: {1}\n".format(case, n_value)
    output.write(message)
