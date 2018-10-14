# coding: utf-8

def main():

    T = int(raw_input().strip())

    for test_case in xrange(1, T + 1):

        first_answer = int(raw_input().strip()) - 1
        first_order = [set(raw_input().strip().split()) for _ in xrange(4)]

        second_answer = int(raw_input().strip()) - 1
        second_order = [set(raw_input().strip().split()) for _ in xrange(4)]

        intersect = first_order[first_answer] & second_order[second_answer]
        count = len(intersect)

        if count == 1:
            print "Case #%d: %s" % (test_case, intersect.pop())
        elif count == 0:
            print "Case #%d: Volunteer cheated!" % test_case
        elif count > 1:
            print "Case #%d: Bad magician!" % test_case
    

if __name__ == '__main__':
    main()
