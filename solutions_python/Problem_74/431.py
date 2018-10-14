import os
import os.path

class robot:
    def __init__(self, colour):
        self.position = 1
        self.colour = colour
        self.target = -1

    def iterate(self, target, sequence):
        if target > self.target:
            self.target = target
            while sequence[self.target][0] != self.colour:
                self.target += 1
                if self.target >= len(sequence):
                    return False
        if self.target >= len(sequence):
            return False
        want = sequence[self.target][1]
        if want > self.position:
            self.position += 1
            return False
        if want < self.position:
            self.position -= 1
            return False
        if target == self.target:
            return True
        return False

def solve(sequence, length):
    target = 0
    orange = robot('O')
    blue = robot('B')
    time = 0
    while target < length:
        press_o = orange.iterate(target, sequence)
        press_b = blue.iterate(target, sequence)

        if press_o or press_b:
            target += 1
        time += 1

    return time

def bottrust(path):
    fin = open(path)
    out_path = os.path.splitext(path)[0] + ".sol"
    fout = open(out_path, "w")

    num_cases = int(fin.readline().strip())

    for i in range(num_cases):
        prob = fin.readline().strip().split()
        length = int(prob[0])
        seq = prob[1:]
        buttons = []
        for j in range(length):
            buttons.append((seq[j*2], int(seq[j*2+1])))
        time = solve(buttons, length)
        fout.write("Case #%i: %i\n" % (i+1, time))
    fout.close()
    fin.close()
