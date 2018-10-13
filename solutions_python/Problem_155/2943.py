import os
import sys

def standing_ovation(line):
    Smax, S = line.split(' ')
    Smax = int(Smax)
    current_standing = 0
    friends_needed = 0
    for Si in range(Smax + 1):
        folks = int(S[Si])
        if not folks:
            continue

        if current_standing > Smax:
            break

        if current_standing < Si:
            friends = Si - current_standing
            friends_needed += friends
            current_standing += friends

        current_standing += folks
    return friends_needed

def read_input(filename):
    with open(filename) as f:
        no_lines = int(f.readline())
        for l in range(no_lines):
            line = f.readline().strip('\r\n')
            out = standing_ovation(line)
            print('Case #%d: %d' % (l + 1, out))

def main():
    if len(sys.argv) != 2:
        print('No input file')
        sys.exit()
    read_input(sys.argv[1])

if __name__ == '__main__':
    main()
