import sys
next(sys.stdin) # We don't care about the very first line

shyness = [list(levels) for _, levels in [x.split() for x in sys.stdin]]

for num, case in enumerate(shyness):
    print('Case #{}: '.format(num + 1), end='')
    people = 0
    friends = 0
    for level, people_at_level in enumerate(case):
        while people < level:
            people += 1
            friends += 1
        people += int(people_at_level)
    print(friends)
