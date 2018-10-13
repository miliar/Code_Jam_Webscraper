import sys, re

def solve(line, casenum):
    l = line[2:]
    steps = {'O' : [], 'B' : []}
    q = []
    t = 0
    robots = {'O' : 1, 'B' : 1}
    items = re.findall(r'([OB] \d+)', l)
    for item in items:
        robot, button = item.split(' ')
        button = int(button)
        q.append((robot, button))
        steps[robot].append(button)
    while q:
        pushed = False
        t += 1
        for k in robots.keys():
            if q:
                stepbot, stepbutton = q[0]
                if not steps[k]:
                    continue
                nextbutton = steps[k][0]
                curbutton = robots[k]
                if curbutton == nextbutton:
                    if k == stepbot and (not pushed):
                        q = q[1:] # press button
                        steps[k] = steps[k][1:]
                        pushed = True
                    else:
                        pass # stay
                else: 
                    if int(curbutton) > int(nextbutton):
                        robots[k] -= 1
                    elif int(curbutton) < int(nextbutton):
                        robots[k] += 1
    print "Case #%d: %d" % (casenum+1, t)

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        cases = int(lines[0])
        lines = lines[1:]
        for i in xrange(0, len(lines)):
            solve(lines[i], i)
