#!/opt/local/bin/python3.3
def solve(data):
    with open(data + '.in', 'r') as infile:
        with open(data + '.out', 'w') as outfile:
            cases = int(infile.readline().rstrip())
            for i in range(cases):
                friends = 0
                standing = 0
                _, shy_list = infile.readline().split()
                for shy_level, people in enumerate(shy_list):
                    add = max(0, shy_level - standing)
                    friends += add
                    standing += int(people) + add
                answer = 'Case #%d: %d\n' % (i + 1, friends)
                print(answer, end='')
                outfile.write(answer)

if __name__ == '__main__':
    try:
        solve('A-small-attempt0')
        solve('A-large')
    except FileNotFoundError:
        pass
