import copy
import random


class Pancake:
    def __init__(self, orrientation):
        #String, + for happy side up, - for happy side down
        self.orrientation = orrientation

    def flip(self):
        if self.orrientation == '+':
            self.orrientation = '-'
        else:
            self.orrientation = '+'

    def __str__(self):
        return self.orrientation

class PancakeLine(list):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return str([str(cake) for cake in self])

class K_Flipper():
    def __init__(self, size):
        self.size = size
        self.times_used = 0

    def flip_at(self, idx, pancakes):
        self.times_used += 1
        for i in range(k):
            try:
                pancakes[i + idx].flip()
            except:
                print("idx: {}, list size: {}".format(i+idx, len(pancakes)))

class Case():
    def __init__(self, number, pancakes_str, k):
        self.number = number
        self.pancakes = PancakeLine()
        self.k = k
        self.flipper = K_Flipper(k)
        self.solution_pancakes = None
        self.last_possible_solution_pancakes = None

        for an_orrient in pancakes_str:
            pancake = Pancake(an_orrient)
            self.pancakes.append(pancake)

    def left_to_right_solve(self):
        self.solution_pancakes = copy.deepcopy(self.pancakes)
        for a_pancake in self.solution_pancakes:
            left_most_pancake_idx_to_flip = self.solution_pancakes.index(a_pancake)
            if a_pancake.orrientation == '-' and left_most_pancake_idx_to_flip <= len(self.solution_pancakes) - self.k:
                self.flipper.flip_at(self.solution_pancakes.index(a_pancake), self.solution_pancakes)

    def random_solve(self, num_solution_attempts, num_flip_attempts):

        possible_solutions = []
        self.solution_pancakes = copy.deepcopy(self.pancakes)
        if self.was_possible():
            self.flipper.times_used = 0
        else:
            for attempt in range(num_solution_attempts):
                self.solution_pancakes = copy.deepcopy(self.pancakes)
                self.flipper = K_Flipper(self.k)
                for flip_attempt in range(num_flip_attempts):
                    random_idx = random.randrange(0, len(self.solution_pancakes) - self.k + 1, 1)
                    # print("flipping at idx {} of {}".format(random_idx, len(self.solution_pancakes)-1))
                    self.flipper.flip_at(random_idx, self.solution_pancakes)

                    if self.was_possible():
                        possible_solutions.append(self.flipper.times_used)
                        self.last_possible_solution_pancakes = copy.deepcopy(self.solution_pancakes)
                        break

            if len(possible_solutions) == 0:
                pass
            else:
                self.flipper.times_used = min(possible_solutions)
                self.solution_pancakes = self.last_possible_solution_pancakes



    def was_possible(self):
        result = True
        i = 0
        while(result == True and i < len(self.solution_pancakes)):
            if self.solution_pancakes[i].orrientation == '-':
                result = False
            i += 1

        return result

    def __str__(self):
        if self.was_possible():
            return "Case #{}: {}".format(self.number, self.flipper.times_used)
        else:
            return "Case #{}: {}".format(self.number, "IMPOSSIBLE")



import sys
sys.stdin = open('A-small-attempt0.in.txt', 'r')
sys.stdout = open('A-small-attempt0.out.txt', 'w')

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
t = int(input())  # read a line with a single integer
cases = []
num_impossibilities = 0
num_total_flips = 0
for i in range(1, t + 1):
  s, k_string = [str(a_string) for a_string in input().split(" ")]  # read a list of strings, 2 in this case
  k = int(k_string)

  case = Case(i, s, k)

  # case.left_to_right_solve()
  # if case.was_possible() == False:
  case.random_solve(4000, 15)

  print(case)

  if case.was_possible() == False:
      num_impossibilities += 1
  else:
      num_total_flips += case.flipper.times_used
  # check out .format's specification for more formatting options

print("Impossibilities: {}, Total Flips: {}".format(num_impossibilities, num_total_flips))




