filename = 'large'

second = None
action = None

class Robo(object):
    def __init__(self, actions, buttons):
        self.actions = actions
        self.buttons = buttons
        self.position = 1
    
    def done(self):
        return len(self.actions) == 0
    
    def step(self):
        if self.done():
            return False
        global second
        global action
        if self.position != self.buttons[0]:
            if self.position < self.buttons[0]:
                self.position += 1
            else:
                self.position -= 1
        elif action == self.actions[0]:
            self.actions.pop(0)
            self.buttons.pop(0)
            return True
        return False

def solve(moves):
    Ba = []
    Bb = []
    Oa = []
    Ob = []
    i = 1
    while moves != []:
        tmp = moves.pop(0)
        if tmp == 'B':
            Ba.append(i)
            Bb.append(int(moves.pop(0)))
        elif tmp == 'O':
            Oa.append(i)
            Ob.append(int(moves.pop(0)))
        i += 1
    B = Robo(Ba, Bb)
    O = Robo(Oa, Ob)
    global second
    global action
    second = 0
    action = 1
    while not B.done() or not O.done():
        second += 1
        tmp1 = B.step()
        tmp2 = O.step()
        if tmp1 or tmp2:
            action += 1
    return second

def main():
    file_in = open('A-%s.in' % filename)
    file_out = open('A-%s.out' % filename, 'w')
    cases = int(file_in.readline().strip())
    for case in xrange(1, cases + 1):
        result = solve(file_in.readline().strip().split(' ')[1:])
        file_out.write('Case #%d: %s\n' % (case, result))
    file_out.close()
    file_in.close()
    return

if __name__ == '__main__':
    main()
    import sys
    sys.exit(0)
