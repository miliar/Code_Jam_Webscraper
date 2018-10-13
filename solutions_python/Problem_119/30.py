import glob, pprint, pickle, os, time, sys
from copy import copy

""" global variables """
state_set = None
chests = None

""" classes """
class Chest:
    ktype = -1 # key that opens it
    ktypes = None # key types of keys inside
    num = -1

    def __init__(self, num, ktype, ktypes):
        self.num, self.ktype, self.ktypes = num, ktype, ktypes

    def __repr__(self):
        return "Chest {}".format(self.num)

class State:
    ktypes = None
    opened_chests = 0

    def __init__(self, ktypes):
        self.ktypes = ktypes

    def openChest(self, chest):
        #assert chest.ktype in self.ktypes, 'could not open chest {} (ktype={}) with keys={}'.format(chest.num, chest.ktype, self.ktypes)
        #assert self.opened_chests & (1<<chest.num) == 0
        self.opened_chests += 1<<chest.num
        self.ktypes.remove(chest.ktype)
        self.ktypes += chest.ktypes

    def closeChest(self, chest):
        #assert self.opened_chests & (1<<chest.num)
        self.opened_chests -= 1<<chest.num
        for k in chest.ktypes:
            self.ktypes.remove(k)
        self.ktypes.append(chest.ktype)

    def openableChests(self):
        return [c for c in chests if (self.opened_chests & (1<<c.num) == 0) and (c.ktype in self.ktypes)]

    def ended(self):
        return self.opened_chests == (1<<len(chests)) - 1

""" function """
def deepsearch(state, trail):
    for c in state.openableChests():
        ## hash pruning
        h = state.opened_chests + (1<<c.num)
        if h in state_set:
            continue
        state_set.add(h)
        ## open chest
        state.openChest(c)
        trail.append(c.num)
        ## check end condition
        if state.ended():
            return trail, True
        ## deep-search new state
        trail, done = deepsearch(state, trail)
        if done:
            return trail, True
        ## close ches
        state.closeChest(c)
        trail.pop()
    return trail, False

def check_num_keys(begin_state):
    def add_key(dic, k):
        if k in dic:
            dic[k] += 1
        else:
            dic[k] = 1
    available_keys = {}
    for k in begin_state.ktypes:
        add_key(available_keys, k)
    for c in chests:
        for k in c.ktypes:
            add_key(available_keys, k)
    chest_keys = {}
    for c in chests:
        add_key(chest_keys, c.ktype)
    for key, available_numkeys in chest_keys.items():
        if not key in available_keys:
            return False
        if available_keys[key] < available_numkeys:
            return False
    return True

def check_connectivity(begin_state):
    ## begin with begin_state keys in set
    available_keys = set()
    for k in begin_state.ktypes:
        available_keys.add(k)
    ## check if solvable with reusable keys
    chests_opened = []
    changed = True
    while changed:
        changed = False
        for c in chests:
            if not c.num in chests_opened:
                if c.ktype in available_keys:
                    chests_opened.append(c.num)
                    for key in c.ktypes:
                        available_keys.add(key)
                        changed = True
    return len(chests_opened) == len(chests)

def solve(begin_state):
    ## check if solvable: check num keys
    if not check_num_keys(begin_state):
        print "detected too few keys"
        return "IMPOSSIBLE"
    ## check if solvable: check connectivity
    if not check_connectivity(begin_state):
        print "detected lack of connectivity"
        return "IMPOSSIBLE"

    ## DEBUG
    # print
    # print
    # print
    # print
    # print "begin state: ", begin_state.ktypes
    # print
    # print "chests"
    # for c in chests:
    #     print "chest (key={}): {}".format(c.ktype, c.ktypes)
    # print
    # print
    ## DEBUG

    ## solve in classical way
    global state_set
    state_set = set()
    result, done = deepsearch(begin_state, [])
    if not done:
        print "did not detect impossible"
        return "IMPOSSIBLE"
    else:
        return " ".join([str(x+1) for x in result])

""" parse input """
output = ""
tic = time.time()
with open(sys.argv[1]) as p:
    def read_ints():
        return [int(x) for x in p.readline().strip().split(' ')]
    numquestions, = read_ints()
    for questionindex in xrange(numquestions):
        K, N = read_ints() # K=#begin_keys, N=#chests
        begin_ktypes = read_ints()
        begin_state = State(ktypes=begin_ktypes)
        #assert len(begin_ktypes) == K
        chests = []
        for chest_num in range(N):
            ints = read_ints()
            T_i, K_i = ints[:2] # T_i=key type, K_i=num keys
            ktypes = ints[2:]
            #assert len(ktypes) == K_i
            chests.append(Chest(chest_num, T_i, ktypes))
        # if not questionindex in (5,):
        #     continue
        answer = solve(begin_state)
        answer_str = "Case #{}: {}".format(1+questionindex, answer)
        output += answer_str + '\n'
        print answer_str
ofile = open('output', 'w').write(output)
toc = time.time()
print "done in {} s".format(toc-tic)