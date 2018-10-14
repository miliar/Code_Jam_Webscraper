def readFile(filename):
    result = []
    with open(filename) as file:
        for line in file:
            s = line.strip()
            result.append(s)
    return result

def countFlips(state):
    state, k = state.split(" ")
    state = list(state)
    k = int(k)
    left = 0
    right = len(state) - 1
    count = 0
    for i in range(0, len(state) - k + 1):
        #print(state)
        #print(i)
        if state[i] == "-":
            count += 1
            for j in range(i, i + k):
                if state[j] == "-":
                    state[j] = "+"
                else:
                    state[j] = "-"
    for i in state:
        if i != "+":
            return "IMPOSSIBLE"
    return str(count)
def pancake():
    states = readFile("A-large.txt")
    states = states[1:]
    for i in range(0, len(states)):
        print("Case #" + str(i + 1) +": " + countFlips(states[i]))
pancake()
