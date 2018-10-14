import queue

def debuff(state):
    return (state[0] - max(state[3] - D,0) , state[1], state[2], max(state[3] - D,0))


def attack(state):
    return (state[0] - state[3], state[1], state[2] - state[1], state[3])


def cure(state):
    return (H - state[3], state[1], state[2], state[3])


def buff(state):
    return (state[0] - state[3], state[1] + B, state[2], state[3])


def adj(state):
    return [attack(state), cure(state), buff(state), debuff(state)]

D = 0
B = 0
H = 0
marked = set()

def one_case():
    global D,B,H,marked
    H,Ad,Hk,Ak,B,D = map(int,input().split())
    marked = set()
    state = (H,Ad,Hk,Ak)
    res = bfs(state)
    if res is not None:
        return str(res)
    return "IMPOSSIBLE"



def bfs(state):
    q = queue.deque()
    q.append((state,0))
    while len(q) > 0:
        st, num = q.popleft()
        if st[2] <= 0:
            return num
        if st in marked:
            continue
        marked.add(st)
        for n in adj(st):
            if n[2] <= 0:
                return num+1
            if n[0] <= 0:
                continue
            q.append((n,num+1))
    return None


T = int(input())
for i in range(T):
    print("CASE #"+str(i + 1)+": " + one_case())