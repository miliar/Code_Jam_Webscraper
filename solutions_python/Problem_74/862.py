import sys

sequences = []
ORANGE = 0
BLUE = 1
'''
sequence = [(0, 2), # Orange 2
            (1, 1),
            (1, 2),
            (0, 4)]

sequence = [(BLUE, 2), (BLUE, 1)]

sequence = [(ORANGE, 5), (ORANGE, 8), (BLUE, 100)]

LEFT = 0
RIGHT = 1
'''

class Bot:
    pop = 0
    def __init__(self, color):
        self.position = 1
        self.color = color

    def move(self, where):
        if where == LEFT:
            self.position = self.position - 1
        elif where == RIGHT:
            self.position = self.position + 1
        else:
            pass

    def __str__(self):
        if self.color == ORANGE:
            name = "Orange"
        else:
            name = "Blue"
        return "[" + name + "] at " + str(self.position)

    def move_closer_to_button(self, button):
        if self.position - button < 0:
            self.position = self.position + 1
            #print self.get_color() + " move to button" + str(self.position)
        elif self.position - button > 0:
            self.position = self.position - 1
            #print self.get_color() + " move to button" + str(self.position)
        else:
            #print self.get_color() + " stays at " + str(self.position)
            pass

    def play(self):
        if sequence == []:
            return

        (color, button) = sequence[0]
        if color == self.color:
            if button == self.position:
                #print self.get_color() + " pushed button" + str(button)
                #global pop
                Bot.pop = 1
            else:
                self.move_closer_to_button(button)
        else:
            for e in sequence:
                (a, b) = e
                if a == self.color:
                    self.move_closer_to_button(b)
                    break
            else:
                #print self.get_color() + " stays at button " + str(self.position)
                return

    def get_color(self):
        if self.color == ORANGE:
            return "Orange"
        else:
            return "Blue"

def parse_input():
    data = sys.stdin.readlines()
    n_test = int(data.pop(0))
    while data != []:
        test = data.pop(0)
        a = test.split()
        current_sequence = []
        a.pop(0)
        for i in range(0, len(a)/2):
            if a[2*i] == 'O':
                bot = ORANGE
            elif a[2*i] == 'B':
                bot = BLUE
            else:
                print "Error " + a[2*i]
                sys.exit(1)
            button = int(a[2*i+1])
            current_sequence.append((bot, button))
        sequences.append(current_sequence) 


def solve_one(sequence):
    OrangeBot = Bot(ORANGE)
    BlueBot = Bot(BLUE)

    n = 0
    while sequence != []:
        n = n +1
    #    print "==> Time : " + str(n)
        OrangeBot.play()
        BlueBot.play()
        if Bot.pop == 1:
            sequence.pop(0)
            Bot.pop = 0

    return n
    
if __name__ == '__main__':
    parse_input()
    for i, sequence in enumerate(sequences):
        n = solve_one(sequence)
        print "Case #" + str(i+1) + ": " + str(n)
    sys.exit(0)
