#!/usr/bin/python

import sys, getopt

def flipPancakes(pancakes, size, index):
    newPancakes = [i for i in pancakes]
    for i in xrange(size):
        if newPancakes[index+i] == "+":
            newPancakes[index+i] = "-"
        else:
            newPancakes[index+i] = "+"
    return "".join(newPancakes)

class Node:
    def __init__(self, state, flips):
        self._state = state
        self._flips = flips
        
    def done(self):
        return len(self._state) == sum([ 1 for i in self._state if i == "+"])

    def state(self):
        return self._state

    def flips(self):
        return self._flips
        
def bfs(pancakes, size):
    queue = []
    visited = dict()
    queue.append(Node(pancakes, 0))
    visited[pancakes] = True
    while(len(queue)!=0):
        current = queue.pop(0)
        if current.done():
            return current.flips()
        for neighbor in [flipPancakes(current.state(), size, i) for i in xrange(len(pancakes)-size+1)]:
            if neighbor not in visited:
                queue.append(Node(neighbor, current.flips()+1))
                visited[neighbor] = True
    return "IMPOSSIBLE"
        
def main(argv):
    inputfile = None
    try:
        opts, args = getopt.getopt(argv, "hi:", ["ifile="])
    except getopt.GetoptError:
        print 'flipPancakes.py -i <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'flipPancakes.py -i <inputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
    f = open(inputfile, 'r')
    numTestCases = int(f.readline())
    for i in xrange(numTestCases):
        [pancakes, size] = f.readline().split(" ")
        size = int(size)
        print "Case #"+str(i+1)+":", bfs(pancakes, size)

if __name__ == "__main__":
    main(sys.argv[1:])
