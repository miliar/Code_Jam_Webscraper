T = input()

def get_guess():
    row = input() - 1
    for i in xrange(4):
        if i == row:
            result = set(raw_input().split())
        else:
            raw_input()
    return result

for i in xrange(T):
    result = get_guess().intersection(get_guess())
    print "Case #%d:" % (i + 1),
    if len(result) == 0:
        print "Volunteer cheated!"
    elif len(result) == 1:
        print result.pop()
    else:
        print "Bad magician!"
