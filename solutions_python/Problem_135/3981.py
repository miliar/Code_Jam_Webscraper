import sys
sys.stdin = open("Input.txt")

for t in xrange(int(raw_input())):
    option1, first = int(raw_input()), [
        map(int, raw_input().split()) for i in xrange(4)]
    option2, last = int(raw_input()), [
        map(int, raw_input().split()) for i in xrange(4)]
    result = set(first[option1 - 1]) & set(last[option2 - 1])
    if len(result) == 1:
        print "Case #{}: {}".format(t + 1, list(result)[0])
    elif len(result) == 0:
        print "Case #{}: Volunteer cheated!".format(t + 1)
    else:
        print "Case #{}: Bad magician!".format(t + 1)