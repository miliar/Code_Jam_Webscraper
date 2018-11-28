def remove_first_level(chars):
    output = []
    #0
    for i in range(chars["Z"]):
        output.append(0)
        chars["Z"] -= 1
        chars["E"] -= 1
        chars["R"] -= 1
        chars["O"] -= 1
    #2
    for i in range(chars["W"]):
        output.append(2)
        chars["T"] -= 1
        chars["W"] -= 1
        chars["O"] -= 1

    #4
    for i in range(chars["U"]):
        output.append(4)
        chars["F"] -= 1
        chars["O"] -= 1
        chars["U"] -= 1
        chars["R"] -= 1


    #6
    for i in range(chars["X"]):
        output.append(6)
        chars["S"] -= 1
        chars["I"] -= 1
        chars["X"] -= 1

    #8
    for i in range(chars["G"]):
        output.append(8)
        chars["E"] -= 1
        chars["I"] -= 1
        chars["G"] -= 1
        chars["H"] -= 1
        chars["T"] -= 1
    return chars, output

def remove_second_level(chars):
    output = []
    #1
    for i in range(chars["O"]):
        output.append(1)
        chars["O"] -= 1
        chars["N"] -= 1
        chars["E"] -= 1
    #3
    for i in range(chars["H"]):
        output.append(3)
        chars["T"] -= 1
        chars["H"] -= 1
        chars["R"] -= 1
        chars["E"] -= 2

    #5
    for i in range(chars["F"]):
        output.append(5)
        chars["F"] -= 1
        chars["I"] -= 1
        chars["V"] -= 1
        chars["E"] -= 1


    #7
    for i in range(chars["V"]):
        output.append(7)
        chars["S"] -= 1
        chars["E"] -= 2
        chars["V"] -= 1
        chars["N"] -= 1
    return chars, output

def remove_third_level(chars):
    output = []
    #9
    for i in range(chars["N"]/2):
        output.append(9)
        chars["N"] -= 2
        chars["I"] -= 1
        chars["E"] -= 1
    return chars, output

def main(s):
    chars = dict.fromkeys(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 0) 
    for c in s:
        if c in chars:
            chars[c] += 1


    chars, out1 = remove_first_level(chars)
    chars, out2 = remove_second_level(chars)
    chars, out3 = remove_third_level(chars)
    outs = out1 + out2 + out3
    outs.sort()
    return "".join([str(x) for x in outs])

n_cases = int(raw_input().strip())

for case_n in range(1, n_cases + 1):
    inp = raw_input().strip()
    print "Case #%s: %s" % (case_n, main(inp))
