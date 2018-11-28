from collections import deque

fin = open('A-large.in','r')
fout = open('output', 'w')

case =  fin.readlines()

size = case[0]

case = deque(case)

case.popleft()

# print case

def fliper(case, size):
    counter = 0
    case = list(case)
    # print case
    for i in range(len(case)):
        if case[i] == "-":
            if len(case) - i < size:
                return "IMPOSSIBLE"
            else:
                j = i
                while j - i + 1 <= size:
                    if case[j] == "+":
                        case[j] = "-"
                    else:
                        case[j] = "+"
                    j += 1
                counter += 1
    return str(counter)

counter = 1
while len(case) != 0:
    cur = case.popleft().strip().split()
    # print cur[0]
    fout.write("Case #" + str(counter) + ": " + fliper(cur[0], int(cur[1])) + "\n")
    counter += 1
fout.close()
fin.close()












