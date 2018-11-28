__author__ = 'Javi'


def main():
    lines = tuple(open('A-large.in', 'r'))
    num_inputs = int(lines[0])
    num_lines_read = 0

    f = open('A.out', 'w')

    for i in xrange(num_inputs):
        s_max, audience = lines[1 + i].split(' ')
        s_max = int(s_max) + 1
        friends = 0
        up_people = 0

        for j in xrange(s_max):
            s = int(audience[j])
            if s > 0 and up_people < j:
                new_friends = j - up_people
                up_people += new_friends
                friends += new_friends
            up_people += s

        print >> f, 'Case #%d: %d' % ((i + 1), friends)


if __name__ == "__main__":
    main()