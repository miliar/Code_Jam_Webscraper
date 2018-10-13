import sys

def sign(x):
    if x == 0: return 0
    return abs(x) // x

def bot_trust(colors, distances):
    time = 0
    O = 1
    B = 1
    finished = False
    while finished == False:
        if 'O' in colors:
            if 'B' in colors:
                cO = colors.index('O')
                cB = colors.index('B')
                O_target = distances[cO]
                B_target = distances[cB]
            else:
               cO = colors.index('O')
               cB = -1
               O_target = distances[cO]
               B_target = -1
        else:
            if 'B' in colors:
                cO = -1
                cB = colors.index('B')
                O_target = 0
                B_target = distances[cB]
            else: return str(time)
        if cO == 0:
            if O == O_target:
                colors = colors[1:]; distances = distances[1:]
                B += sign(B_target - B)
            else:
                O += sign(O_target - O)
                B += sign(B_target - B)
        elif cB == 0:
            if B == B_target:
                colors = colors[1:]; distances = distances[1:]
                O += sign(O_target - O)
            else:
                O += sign(O_target - O)
                B += sign(B_target - B)
        if colors == []: finished == True
        time += 1
    return str(time)

def main(filename):
    Input = open(filename, 'r').read().split('\n')
    Output = ""
    for i in range(int(Input[0])):
        t = Input[i+1].split(' ')[1:]
        colors = [t[2*j] for j in range(len(t) // 2)]
        distances = [int(t[2*j + 1]) for j in range(len(t) // 2)]
        result = bot_trust(colors, distances)
        Output += "Case #" + str(i + 1) + ": " + result + "\n"
    open(filename[:-3] + ".out", 'w').write(Output)

if __name__ == "__main__":
    main(sys.argv[1])
