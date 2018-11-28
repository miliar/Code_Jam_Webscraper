
cache = {}


def solve(spaces, people):
    if (spaces, people) in cache:
        return cache[spaces, people]
    odd_people = people % 2 == 1
    odd_spaces = spaces % 2 == 1
    if odd_spaces:
        sleft = spaces / 2
        sright = spaces / 2
    else:
        sleft = spaces / 2 - 1
        sright = spaces / 2
    if people == 1:
        answer = (sleft, sright)
    elif odd_spaces:
        if odd_people:
            # One will sit in the middle, no extra guys
            answer = solve(sright, people / 2)
        else:
            # One will sit in the middle, the "extra" guy will sit on the left
            answer = solve(sleft, people / 2)
    else:
        if odd_people:
            # One will sit in the middle, so both sides are equal, left has less spaces so last guy will sit there
            answer = solve(sleft, people / 2)
        else:
            # One will sit in the middle, so one group is more, right has more spaces so last guy will sit there
            answer = solve(sright, people / 2)
    cache[spaces, people] = answer
    return cache[spaces, people]

cases = int(raw_input())
for ctr in xrange(cases):
    sss = raw_input().split(" ")
    spaces, people = int(sss[0]), int(sss[1])
    sleft, sright = solve(spaces, people)
    print "Case #{}: {} {}".format(ctr + 1, max(sleft, sright), min(sleft, sright))
