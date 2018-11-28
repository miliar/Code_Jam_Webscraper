import fileinput


def find_dupes(list_a, list_b):
    sets = map(set, [list_a, list_b])
    return sets[0] & sets[1]


def run():
    f = fileinput.input()
    T = int(f.readline())
    for t in xrange(1, T + 1):
        chosen_a = int(f.readline())
        list_a = [[int(i) for i in f.readline().strip().split(' ')] for _ in xrange(4)][chosen_a-1]
        chosen_b = int(f.readline())
        list_b = [[int(i) for i in f.readline().strip().split(' ')] for _ in xrange(4)][chosen_b-1]
        dupes = find_dupes(list_a, list_b)
        if len(dupes) == 1:
            print 'Case #%d: %d' % (t, dupes.pop())
        elif len(dupes) == 0:
            print 'Case #%d: Volunteer cheated!' % t
        else:
            print 'Case #%d: Bad magician!' % t


if __name__ == '__main__':
    run()