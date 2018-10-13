t = int(raw_input())

case = 1
while t > 0:
    s = raw_input().split(' ')
    invited = 0
    standing = 0
    for index, num in enumerate(s[1]):
        if standing + invited >= index:
            standing += int(num)
        else:
            invited += int(index) - (standing + invited)
            standing += int(num)

    print 'Case #{0}: {1}'.format(case, invited)
    t -= 1
    case += 1
