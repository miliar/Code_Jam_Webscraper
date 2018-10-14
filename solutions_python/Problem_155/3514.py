__author__ = 'David'

def break_string(string):
    double_array = string.split()
    array = list(double_array[1])
    return (double_array[1],array)


def solve_problem(input):
    array = break_string(input)
    total = int(array[1][0])
    needed_friends = 0
    for i in range(1,len(array[1])):
        # Add any needed friends
        if total < i and int(array[1][i])!=0:
            needed_friends = needed_friends + (i - total)
            total += needed_friends
        total += int(array[1][i])
    return needed_friends

if __name__ == "__main__":
    with open('A-small-attempt0.in','r') as file:
        count = 0
        for line in file:
            if count > 0:
               print("Case #" + str(count) + ": " + str(solve_problem(line)))
            count +=1