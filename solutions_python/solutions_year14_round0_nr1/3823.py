def get_arrangement():
    arrangement = []
    for i in xrange(1,5):
        l = raw_input()
        l = map(int,l.split(' '))
        arrangement.append(l)
    return arrangement

if __name__ == '__main__':
    no_inp = int(raw_input())
    for i in xrange(1,no_inp+1):
        ans_1 = int(raw_input())
        first_arrangement = get_arrangement()
        ans_2 = int(raw_input())
        second_arrangement = get_arrangement()
        intersect = set(first_arrangement[ans_1-1]) &  set(second_arrangement[ans_2-1])
        intersect_len = len(intersect)
        if intersect_len == 0:
            print 'Case #%d: Volunteer cheated!'%i
        elif intersect_len == 1:
            print 'Case #%d: %d'%(i,list(intersect)[0])
        else:
            print 'Case #%d: Bad magician!'%i
