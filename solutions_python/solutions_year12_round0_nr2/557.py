import sys

scores = [29, 20, 8, 18, 18, 21]
surprises = 2
p = 8

def numyes(surprises, goal, scores):
    minyes = max(goal, goal * 3 - 2)
    minmaybe = max(goal, goal * 3 - 4)
    yes, maybe, no = 0, 0, 0
    for s in scores:
        if s >= minyes:
            yes += 1
        elif s >= minmaybe:
            maybe += 1
        else:
            no += 1
    yes += min(maybe, surprises)
    return yes

lines = sys.stdin.readlines()
idx = 0
for l in lines[1:]:
    nums = map(int, l.split())
    N = nums[0]
    surprises = nums[1]
    goal = nums[2]
    scores = nums[3:]
    idx += 1
    print "Case #{}: {}".format(idx, numyes(surprises, goal, scores))


