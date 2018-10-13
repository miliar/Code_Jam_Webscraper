from sys import stdin

def is_goal(plates):
    return len(plates) == 0

def successors(plates):
    succ = []
    seenfrom = set()
    seenstates = set()
    seenstates.add(tuple(sorted(plates)))
    succ.append(tuple(p-1 for p in plates if p > 1))
    for i, p in enumerate(plates):
        if p in seenfrom: continue
        seenfrom.add(p)
        seento = set()
        for j, q in enumerate(plates):
            if i == j: continue
            if q in seento: continue
            if p <= q: continue
            seento.add(q)
            for npancakes in range(1, p-q+1):
                newplates = list(plates)
                newplates[i] -= npancakes
                newplates[j] += npancakes
                newplates = tuple(sorted([pl for pl in newplates if pl > 0]))
                if newplates not in seenstates:
                    seenstates.add(newplates)
                    succ.append(newplates)
        for npancakes in range(1, p):
            newplates = list(plates)
            newplates[i] -= npancakes
            newplates.append(npancakes)
            newplates = tuple(sorted(newplates))
            if newplates not in seenstates:
                seenstates.add(newplates)
                succ.append(newplates)
    #print plates, succ
    return succ
        

def solve(plates):
    explored = set()
    frontier = [ [plates] ]
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for state in successors(s):
            if state not in explored:
                explored.add(state)
                path2 = path + [state,]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)

if __name__ == '__main__':
    T = int(stdin.readline())
    for case in range(1, T+1):
        D = int(stdin.readline())
        plates = tuple(int(x) for x in stdin.readline().split())
        answer = solve(plates)
        print "Case #%d: %s" % (case, len(answer)-1)
