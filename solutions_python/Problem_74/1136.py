'''
Created on May 7, 2011

@author: admin
'''

class Bot(object):
    def __init__(self, color = 'O', instructions = []):
        self.color = color
        self.pos = 1
        self.index = 0
        self.instructions = instructions
    
    def update(self, step):
        if not self.has_instruction():
            self.wait()
            return False
        time, button = self.get_instruction()
        if button < self.pos:
            self.move_left()
        elif button > self.pos:
            self.move_right()
        else: # button == self.pos
            if time < step:
                raise ValueError
            elif time > step:
                self.wait()
            else: # time == step
                self.press()
                return True
        return False
    
    def move_left(self):
        self.pos -= 1
        print "%s bot moved left to pos %d" % (self.color, self.pos)
    def move_right(self):
        self.pos += 1
        print "%s bot moved right to pos %d" % (self.color, self.pos)
    def wait(self):
        print "%s bot waits at %d" % (self.color, self.pos)
        pass
    def press(self):
        print "%s bot pressed button %d" % (self.color, self.pos)
        self.index += 1
    
    def has_instruction(self):
        return self.index < len(self.instructions)
    def get_instruction(self):
        return self.instructions[self.index]

def read_input():
    fin = open("a-large.in", "r")
    lista = []
    for index, line in enumerate(fin):
        if index is 0:
            continue
        print "caso ", index
        d = {'B': [], 'O': []}
        seq = line.strip().split(" ")[1:]
        for i in xrange(0, len(seq), 2):
            print seq[i], seq[i+1]
            d[seq[i]].append((i/2, int(seq[i+1])))
        lista.append(d)
    fin.close()
    return lista

def write_output(solution):
    fout = open("a.out", "w")
    for index, s in enumerate(solution):
        out_txt = "Case #%d: %d\n" % (index + 1, s)
        print out_txt
        fout.write(out_txt)
    fout.close()

def main():
    print "problem A: Bot Trust"
    lista = read_input()
    print lista
    solution = []
    for test in lista:
        bots = [Bot('O', test['O']),
                Bot('B', test['B'])]
        step = 0
        iteration = 0
        while any([bot.has_instruction() for bot in bots]):
            iteration += 1
            pressed = False
            for bot in bots:
                if bot.update(step):
                    pressed = True
            if pressed:
                step += 1
            print "-"*80
        solution.append(iteration)
    
    print solution
    write_output(solution)
        
                

if __name__ == '__main__':
    main()