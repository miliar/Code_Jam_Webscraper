import copy
import sys
import math
from pprint import pprint
from copy import deepcopy

input = file(sys.argv[1])
count = int(input.readline())
testcase = 1

bla = 0

class BTree(object):
    def __init__(self, teams, price, left, right):
        self.teams = teams
        self.price = price
        self.left = left
        self.right = right
        self.cached_results = {}
        self.zero_cost = [1000 for x in teams]

    def cheapest(self, constraints):
        globals()['bla'] += 1
        if not self.left:
            for team in self.teams:
                if not constraints[team]:
                    return self.price
            return 0
        cache_key = 0
        zero_cost = True
        for i, team in enumerate(self.teams):
            cache_key += constraints[team] << (10 * 1)
            if self.zero_cost[i] > constraints[team]:
                zero_cost = False
        if cache_key in self.cached_results:
            return self.cached_results[cache_key]
        price_one = self.price
        price_one += self.left.cheapest(constraints)
        price_one += self.right.cheapest(constraints)
        if price_one == 0:
            for i, team in enumerate(self.teams):
                self.zero_cost[i] = min(self.zero_cost[i], constraints[team])
            new_constraints = deepcopy(constraints)
            new_constraints[self.teams[0]] = 0
        else:
            new_constraints = deepcopy(constraints)
        for team in self.teams:
            if new_constraints[team]:
                new_constraints[team] -= 1
            else:
                self.cached_results[cache_key] = price_one
                return self.cached_results[cache_key]
        price_two = self.left.cheapest(new_constraints)
        price_two += self.right.cheapest(new_constraints)
        self.cached_results[cache_key] = min(price_two, price_one)
        return self.cached_results[cache_key]

if __name__ == '__main__':
    try:
        while testcase <= count:
            globals()['bla'] = 0
            mod_teams = int(input.readline())
            teams = mod_teams ** 2
            constraints = {}
            for team, max_miss in enumerate(map(int, input.readline().split())):
                constraints[team] = max_miss
            last_matches = []
            for i, price in enumerate(map(int, input.readline().split())):
                last_matches.append(BTree([i*2, i*2+1], price, None, None))
            for i in range(mod_teams-1):
                new_last_matches = []
                for i, price in enumerate(map(int, input.readline().split())):
                    left, right = [last_matches[i * 2], last_matches[i * 2 + 1]]
                    teams = left.teams + right.teams
                    new_last_matches.append(BTree(teams, price, left, right))
                last_matches = new_last_matches
            final = last_matches[0]
            result = str(final.cheapest(constraints))
            print 'Case #%i: %s' % (testcase, result)
            testcase += 1
    except Exception, e:
        print e
        import pdb;pdb.post_mortem()
