import string

def AreHappy(pancakes, num_pancakes):
    return pancakes == "+" * num_pancakes

def GetFirstUnhappy(pancakes):
    return string.find(pancakes, "-")

def IsPossible(first_unhappy, flipper_size, num_pancakes):
    return first_unhappy + flipper_size <= num_pancakes

def Flip(pancakes):
    result = ""
    for c in pancakes:
        if c == "+":
            result += "-"
        else:
            result += "+"
    return result

def DoOneFlip(pancakes, num_pancakes, first_unhappy, flipper_size):
    pancakes_to_flip = pancakes[first_unhappy:first_unhappy + flipper_size]
    flipped_pancakes = Flip(pancakes_to_flip)
    return pancakes[:first_unhappy] + flipped_pancakes + pancakes[first_unhappy + flipper_size:]

def Solve(pancakes, flipper_size):
    solution = 0
    num_pancakes = len(pancakes)
    while not AreHappy(pancakes, num_pancakes):
        first_unhappy = GetFirstUnhappy(pancakes)
        if not IsPossible(first_unhappy, flipper_size, num_pancakes):
            return "IMPOSSIBLE"
        pancakes = DoOneFlip(pancakes, num_pancakes, first_unhappy, flipper_size)
        solution += 1
    return solution

num_cases = int(raw_input())
for case_num in xrange(1, num_cases + 1):
    pancakes, flipper_size = raw_input().split(" ")
    solution = Solve(pancakes, int(flipper_size))
    print "Case #{}: {}".format(case_num, solution)