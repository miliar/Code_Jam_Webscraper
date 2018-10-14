import sys

def read_input(file):
    res = []
    
    f = open(file, "r")
    
    l = f.readline()
    while l != "":
        ls = l.split()
        i = 1
        while i <= len(ls) - 2:
            res[-1].append((ls[i], int(ls[i + 1])))
            i += 2
        l = f.readline()
        if l != "":
            res.append([])
    f.close()
    
    return res

OTHER = {'O':'B', 'B':'O'}

def find_first(c, input, type):
    for i in range(0, len(input)):
        if input[c] == input[i]:
            break
    for i in range(i + 1, len(input)):
        if input[i][0] == type:
            return input[i]
    
    return None

def solve_case(input):
    res = 0
    pos = {'O': 1, 'B': 1}
    current = 0
    nextother = find_first(current, input, OTHER[input[current][0]])
    while True:
        # try to move other
        if nextother is not None:
            if (nextother[1] - pos[nextother[0]]) > 0:
                pos[nextother[0]] += 1
            elif (nextother[1] - pos[nextother[0]]) < 0:
                pos[nextother[0]] += -1
        
        if pos[input[current][0]] == input[current][1]:
            # can push
            res += 1
            current += 1
            if current >= len(input):
                return res
            else:
                nextother = find_first(current, input, OTHER[input[current][0]])
        else:
            # bring current closer
            if (input[current][1] - pos[input[current][0]]) > 0:
                pos[input[current][0]] += 1
            else:
                pos[input[current][0]] += -1
            
            # add action
            res += 1

def solve_all(all):
    f = open("output", "w")
    for (i, c) in enumerate(all):
        f.write("Case #" + str(i + 1) + ": " + str(solve_case(c)) + "\n")
    f.close()

if __name__ == "__main__":
    i = read_input(sys.argv[1])
    solve_all(i)