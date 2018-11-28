#!/usr/bin/python

infile = 'A-small-attempt1.in'

lines = []
with open(infile, 'r') as f:
    lines = f.readlines()

cases = int(lines[0])
lines = lines[1:]

class Grid:

    def __init__(self, r, c, grid):
        self.r = r
        self.c = c
        self.grid = grid

    def is_valid_zone(self, r1, r2, c1, c2, row, col):
        for i in xrange(r1, r2+1):
            for j in xrange(c1, c2+1):
                if i == row and j == col:
                    continue
                if self.grid[i][j] != '?':
                    return False
        return True

    def flood_zones(self, elem, row, col):
        move_set = []
        # Optimization for finding neighbors
        for r1 in xrange(0, row+1):
            for r2 in xrange(row, self.r):
                for c1 in xrange(0, col+1):
                    for c2 in xrange(col, self.c):
                        # Loop through boundaries
                        if self.is_valid_zone(r1, r2, c1, c2, row, col):
                            move_set.append( (r1,r2,c1,c2) )
        return move_set

    def get_zones(self):
        zones = {}
        for row in xrange(self.r):
            for col in xrange(self.c):
                elem = self.grid[row][col]
                if elem != '?':
                    zones[elem] = self.flood_zones(elem, row, col)

        return zones

    def check_state(self, zones, choice_list, choices):
        visited = set()
        for i, zone_choice in enumerate(choice_list):
            zone = zones[choices[i][0]][zone_choice]
            r1, r2, c1, c2 = zone
            for j in xrange(c1, c2+1):
                for i in xrange(r1, r2+1):
                    val = j * self.r + i
                    if val in visited:
                        return -1
                    visited.add(val)

        if len(visited) == (self.r * self.c):
            return 1
        return 0

    def solve(self):
        zones = self.get_zones()
        choices = [(i, len(zones[i])) for i in zones.keys()]
        choices = sorted(choices, key=lambda x: x[1])

        agenda = [[]]
        while len(agenda) > 0:
            choice_list = agenda.pop(0)
            cur_ind_choice = len(choice_list)

            if cur_ind_choice == len(choices):
                continue

            for j in xrange(choices[cur_ind_choice][1]):
                new_choice_list = choice_list[:] + [j]
                out_val = self.check_state(zones, new_choice_list, choices)
                if out_val == 1:
                    return self.paint_grid(zones, new_choice_list, choices)
                if out_val == -1:
                    continue

                agenda.append(new_choice_list)

    def paint_grid(self, zones, new_choice_list, choices):
        grid = [[None for j in xrange(self.c)] for i in xrange(self.r)]

        for i, choice in enumerate(choices):
            initial = choice[0]
            zone_id = new_choice_list[i]
            zone = zones[initial][zone_id]

            r1, r2, c1, c2 = zone
            for x in xrange(r1, r2+1):
                for y in xrange(c1, c2+1):
                    grid[x][y] = initial

        grid_str = ''
        for i in xrange(self.r):
            grid_str += ''.join(grid[i]) + '\n'
        return grid_str[:-1]

for num in xrange(cases):
    r, c = lines[0].strip().split()
    r, c = int(r), int(c)
    grid = lines[1:1+r]
    grid = [list(i.strip()) for i in grid]
    lines = lines[1+r:]
    g = Grid(r,c,grid)
    solution = g.solve()
    print 'Case #{}:\n{}'.format(num+1, solution)