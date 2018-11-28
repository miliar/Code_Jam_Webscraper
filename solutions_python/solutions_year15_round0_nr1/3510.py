cases = int(input())
data = map(lambda x: (int(x.split()[0]), x.split()[1]), [input() for i in range(cases)])
data = list(map(lambda x: (x[0], dict(enumerate(list(map(int, list(x[1])))))), data))

def peopleSitting(state):
    return len(list(filter(lambda x: x != 0, set(state[1].values())))) > 0

def someoneWillgetUp(state, stood):
    sitting = []

    for i in state[1]:
        if state[1][i] > 0:
            sitting.append((i, state[1][i]))

    return len(list(filter(lambda x: x[0] <= stood, sitting))) > 0

def getUp(state, stood):
    newState = state
    newStood = stood
    for i in state[1]:
        if i <= stood and state[1][i] > 0:
            newStood = newStood + newState[1][i]
            newState[1][i] = 0
    return (newState, newStood)

def friendsRequired(state, stood):
    if peopleSitting(state):
        if someoneWillgetUp(state, stood):
            state, stood = getUp(state, stood)
            return friendsRequired(state, stood)
        else:
            newPeople = state[1]
            newPeople[state[0]] = newPeople.setdefault(state[0], 0) + 1
            newState = (state[0], newPeople)

            state, stood = getUp (newState, stood)
            return 1 + friendsRequired(newState, stood + 1)
    else:
        return 0

for i in enumerate(map(lambda x: friendsRequired(x, 0), data)):
    print("Case #%s: %s" % (i[0] + 1, i[1]))
