def read_one_config():
    row = int(raw_input()) - 1
    bd = [map(int, raw_input().split()) for i in xrange(4)]
    return (row, bd)


def main():
    num_cases = int(raw_input())
    for case in xrange(num_cases):
        row1, bd1 = read_one_config()
        row2, bd2 = read_one_config()
        commons = [i for i in xrange(1, 17)
                   if i in bd1[row1] and i in bd2[row2]]
        print "Case #%d:" % (case + 1),
        if not commons:
            print "Volunteer cheated!"
        elif len(commons) > 1:
            print "Bad magician!"
        else:
            print commons[0]


if __name__ == '__main__':
    main()
