
test_cases = int(raw_input().strip())

def get_board():
    rows = []
    for i in xrange(4):
        rows.append(map(int, raw_input().strip().split()))
    return rows

for test_case in xrange(test_cases):
    first_answer = int(raw_input().strip()) - 1
    fboard = get_board()
    fset = set(fboard[first_answer])
    second_answer = int(raw_input().strip()) - 1
    sboard = get_board()
    sset = set(sboard[second_answer])

    mage_options = fset.intersection(sset)

    if len(mage_options) == 1:
        print "Case #%s: %d" % (repr(test_case + 1), mage_options.pop())
    elif len(mage_options) == 0:
        print "Case #%s: Volunteer cheated!" % repr(test_case + 1)
    else:
        print "Case #%s: Bad magician!" % repr(test_case + 1)

