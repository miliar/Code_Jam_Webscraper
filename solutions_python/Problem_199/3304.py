import queue

class State:

    def __init__(self,value,parent):
        self.value = value
        self.parent = parent

    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            return self.value == other.value
        return NotImplemented

    def __ne__(self, other):
        """Define a non-equality test"""
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        """Override the default hash behavior (that returns the id or the object)"""
        return hash(self.value)

    def get_flips(self, K):
        flips = []
        for k in range(len(self.value)-K+1):
            flipped = ""
            for j in range(len(self.value)):
                if j >= k and j <= k+K-1:
                    if self.value[j] == '+':
                        flipped += '-'
                    else:
                        flipped += '+'
                else:
                    flipped += self.value[j]
            flips.append(State(flipped, self))
        return flips

    def is_end_state(self):
        return self.value == "+"*len(self.value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

f = open('./A-small-attempt0.in', 'r')
w = open('./A-small-attempt0.out', 'w')
T = int(f.readline())
for i in range(T):
    line = f.readline()
    info = line.split(' ')
    S = info[0]
    K = int(info[1])
    initial_state = State(S,None)
    states = queue.Queue()
    states.put(initial_state)
    end_state = None
    visited_flips = set([initial_state])
    while not states.empty():
        next_state = states.get()
        if next_state.is_end_state():
            end_state = next_state
            break
        flips = next_state.get_flips(K)
        for flip in flips:
            if flip not in visited_flips:
                states.put(flip)
                visited_flips.add(flip)
    if end_state is None:
        result = "IMPOSSIBLE"
    else:
        result = -1
        current = end_state
        while current is not None:
            result+=1
            current = current.parent
    w.write("Case #%i: %s\n" % (i+1,result))