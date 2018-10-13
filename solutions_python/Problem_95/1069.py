mapping = [['a', 'y'], ['b', 'h'], ['c', 'e'], ['d', 's'], ['e', 'o'], ['f', 'c'], ['g', 'v'], ['h', 'x'], ['i', 'd'], ['j', 'u'], ['k', 'i'], ['l', 'g'], ['m', 'l'], ['n', 'b'], ['o', 'k'], ['p', 'r'], ['q', 'z'], ['r', 't'], ['s', 'n'], ['t', 'w'], ['u', 'j'], ['v', 'p'], ['w', 'f'], ['x', 'm'], ['y', 'a'], ['z', 'q']]

f = open('C:/Users/SACHIN/Desktop/A-small-attempt0.in', 'r')
g = open('C:/Users/SACHIN/Desktop/ouput.txt', 'w')
inp = f.readlines()

for i in range(1, len(inp)):
    line = inp[i]
    string = ""
    for j in range(len(line) - 1):
        if line[j] == " ":
            string += " "
        else:
            index = ord(line[j]) - 97
            string += mapping[index][1]
    output_str = "Case #" + str(i) + ": " + string + "\n"
    g.write(output_str)
