import sys


def solve(num_people_with_shyness):
    s_max = len(num_people_with_shyness) - 1
    ret = 0
    num_people_standing = 0
    for level in xrange(0, s_max + 1):
        num_invitation = 0
        if num_people_standing < level:
            num_invitation = level - num_people_standing
        num_people_standing += num_people_with_shyness[level] + num_invitation
        ret += num_invitation
    return ret


def main():
    num_testcases = int(sys.stdin.readline().strip())
    counter = 0
    for line in sys.stdin:
        counter += 1
        s_max, data = line.strip().split(' ')
        num_people_with_shyness = [int(x) for x in data]
        print 'Case #{counter}: {num}'.format(
            counter=counter,
            num=solve(num_people_with_shyness),
        )


if __name__ == '__main__':
    main()
