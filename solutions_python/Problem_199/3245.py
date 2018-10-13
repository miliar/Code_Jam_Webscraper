filename = "A-small-attempt0.in"

stacks=[]
sizes= []

def get_input(filename):
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:] :
            line = line.split()
            stack = ''
            for c in (line[:-1]):
                 stack += c
            sizes.append(int(line[-1]))
            stacks.append(list(stack))

def diff(a,b):
    count = 0
    for i in range(len(a)):
        count += (1 if a[i] != b[i] else 0)
    return count

def get_min_f(ls):
    minV = 10000000
    ret = None
    for i in range(0,len(ls)):
        if ls[i][0] < minV:
            ret = i
            minV = ls[i][0]
    return ret

def h(a,goal,K):
    return diff(a,goal)/K

def get_all_flips(stack,K):
    flips = []
    for i in range(0,len(stack) - K+1):
        for j in range(i, i+K):
            stack[j] = '+' if stack[j] == '-' else '-'

        flips.append(list(stack))
        for j in range(i,i+K):
            stack[j] = '+' if stack[j] == '-' else '-'

    return flips


def solve(stack, K):
    goal = ['+'] * len(stack)
    queue = []
    queue.append( (h(stack,goal,K) + 0 , 0,  h(stack,goal,K), stack) )
    explored = set(''.join(stack))

    iterCount = 0

    while True:
        #
        # print(queue)
        # c=input()

        minEntry = get_min_f(queue)
        if minEntry == None: # or queue[minEntry][1] > len(stack)*10000:
            return "IMPOSSIBLE"
        nxt = queue[minEntry]
        del queue[minEntry]

        if nxt [2] == 0:   #h == 0
            return nxt[1]

        g = nxt[1]

        flips = get_all_flips(nxt[3], K)
        for flip in flips:
            ex = [i for i, v in enumerate(queue) if v[3] == flip]
            newEntry = ( g + 1 + h(flip,goal,K), g+1, h(flip,goal,K) , flip)
            ex = ex.pop() if ex else None
            if ex and queue[ex] != None and queue[ex][0] > newEntry[0]:
                queue[ex] = newEntry
            else:
                if ''.join(flip) not in explored:
                    queue.append(newEntry)
                    explored.add(''.join(flip))
        iterCount += 1












get_input(filename)

for i in range(0,len(stacks)):
    print("Case #", i+1 , ": ", solve(stacks[i],sizes[i]), sep="")
