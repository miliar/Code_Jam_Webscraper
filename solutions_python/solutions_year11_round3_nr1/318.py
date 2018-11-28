problem = 'SquareTiles'
t = 'l'
debug = True

middle = {'t': 'ex', 's': 'small', 'l': 'large'}[t]

input_file = open('{problem}-{middle}.in'.format(**globals()))
output_file = open('{problem}-{middle}.out'.format(**globals()), 'w')

# Helper functions
def split_to_ints(s):
    return [i for i in map(int, s.split())]

def list_to_index_tuple(l, base=0):
    return [(i + base, l[i]) for i in range(len(l))]

class Solution:
    format = '\n{0}' # The format string for solutions
    
    def __init__(self, get):
        # Read in the entire solution
        self.R, self.C = split_to_ints(get())
        self.floor = []
        for l in range(self.R):
            self.floor.append([{'.':0, '#':-1}[tile] for tile in get()[:-1]])

    def weight(self):
        # Return the value that determines the weight of the solution (for timing)
        return self.R * self.C

    def floor_left(self, line, tile):
        if tile > 0:
            return self.floor[line][tile-1]
        else:
            return None

    def floor_top(self, line, tile):
        if line > 0:
            return self.floor[line-1][tile]
        else:
            return None

    def solve(self):
        # Return the solution dictionary for this case
        floor = self.floor
        floor_left = self.floor_left
        floor_top = self.floor_top
        for f in range(self.R):
            for t in range(self.C):
                if floor[f][t] == 0:
                    if floor_left(f, t) in [1, 3] or floor_top(f, t) in [1, 2]:
                        return 'Impossible'
                if floor[f][t] == -1:
                    if floor_left(f, t) in [1, 3]:
                        floor[f][t] = floor_left(f, t) + 1
                    if floor_top(f, t) in [1, 2]:
                        if floor[f][t] not in [-1, 4]:
                            return 'Impossible'
                        if floor[f][t] == -1:
                            floor[f][t] = floor_top(f, t) + 2
                    if floor[f][t] == -1: floor[f][t] = 1

        tiles_used = [0] * 5
        for f in range(self.R):
            for t in range(self.C):
                tiles_used[floor[f][t]] += 1
                floor[f][t] = {1:'/', 2:'\\', 3:'\\', 4:'/', 0:'.'}[floor[f][t]]

        if len(set(tiles_used[1:])) > 1:
            return 'Impossible'

        return '\n'.join([''.join([tile for tile in line]) for line in floor])

if debug: from time import clock
    
if __name__ == '__main__':
    get = input_file.readline
    n = int(get())
    durations = []
    for i in range(n):
        s = Solution(get)
        if debug:
            print ('Case {} started'.format(i))
            start = clock()
        o = s.format.format(s.solve())
        if debug:
            duration = clock() - start
            durations += [(duration, s.weight())]
            print ('Case {} solved in {}'.format(i, durations[-1][0]))
            print ('Weight {}, so: {}'.format(durations[-1][1], durations[-1][0] / durations[-1][1]))
        output_file.write('Case #{}: {}\n'.format(i+1, o))
    if debug:
        mean = sum(x[0] for x in durations) / len(durations)
        maxdiff = 0
        for x in durations:
            maxdiff = max(maxdiff, abs(mean-x[0]))
        if maxdiff/mean < .25: print('O(1)')
        else: print('> O(1)')
        mean = sum(x[0]/x[1] for x in durations) / len(durations)
        maxdiff = 0
        for x in durations:
            maxdiff = max(maxdiff, abs(mean-(x[0]/x[1])))
        if maxdiff/mean < .25: print('O(N)')
        else: print('> O(N)')
        