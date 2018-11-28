__author__ = 'klaxon'

class Problem:
    def __init__(self, farm_cost, farm_bonus, goal):
        self.farm_cost = farm_cost
        self.farm_bonus = farm_bonus
        self.goal = goal


def read_problems_from(fileName):
    f = open(fileName, "r")
    #ignore problem count
    f.readline()

    problems = []
    for line in f.readlines():
        values = [float(x) for x in line.split(" ", 3)]
        problems.append(Problem(values[0], values[1], values[2]))

    return problems

initial_cookies_per_sec = 2


def solve(p):
    if p.farm_bonus == 0 or p.farm_cost > p.goal:
        return p.goal / initial_cookies_per_sec

    farm_secs = []

    previous_secs = p.goal / initial_cookies_per_sec
    current_secs = previous_secs

    while previous_secs >= current_secs:
        next_cps = len(farm_secs) * p.farm_bonus + initial_cookies_per_sec
        farm_secs.append(p.farm_cost / next_cps)
        s = sum(farm_secs)

        previous_secs = current_secs
        current_secs = s + p.goal / (next_cps + p.farm_bonus)

    return previous_secs


#Solving
problem_list = read_problems_from("input.txt")
result = ""
for (index, p) in enumerate(problem_list):
    result += "Case #" + repr(index + 1) + ": " + repr(solve(p))
    result += "\n"

result_file = open("result.txt", "w")
result_file.write(result)
result_file.close()
