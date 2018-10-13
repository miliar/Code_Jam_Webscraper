#!/usr/bin/python

import Queue

class Graph:
    
    def __init__(self, s, k):
        self.s = s
        self.k = k
        self.states = {}

    def add_state(self, state_hash, state):
        self.states[state_hash] = state

    def create_links(self):
        for state in self.states.values():
            flip_states = state.get_flip_states(self.k)
            link_states = [self.states[i] for i in flip_states]
            state.links = link_states

    def solve(self, start):
        agenda = Queue.PriorityQueue()
        agenda.put((0, (self.states[start], [self.states[start].state_hash])))
        visited = set()
        scheduled = set()

        while not agenda.empty() > 0:
            path_size, state_tuple = agenda.get()
            current_state, path = state_tuple[0], state_tuple[1]
            visited.add(current_state)

            if current_state.end == True:
                return path_size

            for link in current_state.links:
                if link not in visited and link not in scheduled:
                    agenda.put( (path_size+1, (link, path[:] + [current_state.state_hash])) )
                    scheduled.add(link)
        return -1
# exit()
class State:
    
    def __init__(self, state_hash, state):
        self.state_hash = state_hash
        self.state = state
        self.links = []
        self.length = len(self.state)
        
        if sum(self.state) == self.length:
            self.end = True
        else:
            self.end = False

    def get_flip_states(self, k):
        flip_states = []
        for i in xrange(0, self.length-k+1):
            new_state = self.state[:]
            for j in xrange(0,k):
                new_state[i+j] = (self.state[i+j]+1)%2
            flip_states.append(''.join([str(i) for i in new_state]))
        return flip_states


# def generate_graphs():
#     graphs = {}
#     graphs[(8,3)] = generate_graph(8,3)
#     graphs[(5,4)] = generate_graph(5,4)
#     # graphs[(8,3)] = generate_graph(5,4)
#     return graphs

def generate_graph(s,k):
    graph = Graph(s,k)

    for i in xrange(0,2**s):
        state_hash = str(bin(i))[2:].zfill(s)
        state_str_list = to_state(state_hash)
        graph.add_state(state_hash, State(state_hash, state_str_list))

    graph.create_links()
    return graph

def get_state_hash(state_str):
    return ''.join([str(i) for i in state_str])

def to_state_str_list(pattern):
    pattern = pattern.replace('-','0')
    pattern = pattern.replace('+','1')
    str_list = list(pattern)
    return str_list

def to_state(state_str_list):
    return [int(i) for i in state_str_list]

graphs = {}

filename = 'a_small_attempt3.in'
with open(filename, 'r') as f:
    lines = f.readlines()

count = int(lines[0])
for j in xrange(count):
    line = lines[j+1]
    pattern, flipper = line.strip().split()
    start = to_state_str_list(pattern)
    s = len(start)
    k = int(flipper)
    
    if (s,k) not in graphs:
        graph = generate_graph(s,k)
        graphs[(s,k)] = graph
    graph = graphs[(s,k)]
    
    result = graph.solve(get_state_hash(start))
    out_str = str(result)
    if result == -1:
        out_str = "IMPOSSIBLE"

    print "Case #{}: {}".format(j+1, out_str)
