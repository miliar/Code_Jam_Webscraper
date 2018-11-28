import sys

class Bot(object):
    def __init__(self, targets):
        self.position = 1
        self.targets = targets
        if self.targets:
            self.target = targets[0]
        else:
            self.target = 1


    def move(self):
        if self.target > self.position:
            self.position += 1
        elif self.target < self.position:
            self.position -= 1

    def on_target(self):
        if self.target == self.position:
            return True
        else:
            return False
    def next_target(self):
        self.targets = self.targets[1:]
        if self.targets:
            self.target = self.targets[0]


class Game(object):
    def __init__(self, targets):
        self.targets = targets
        self.blue = []
        self.orange = []
        for t in targets:
            if t[0] == 'O':
                self.orange.append(t[1])
            else:
                self.blue.append(t[1])

    def run(self):
        i = 0
        blue = Bot(self.blue)
        orange = Bot(self.orange)
        pushed = False
        while len(self.targets) > 0:
            i += 1
            if blue.on_target() and self.targets[0][0] == 'B':
                pushed = True
                blue.next_target()
            else:
                blue.move()

            if orange.on_target() and self.targets[0][0] == 'O':
                pushed = True
                orange.next_target()
            else:
                orange.move()

            if pushed:
                self.targets = self.targets[1:]
                pushed = False
        return i


if __name__ == "__main__":
    items = sys.stdin.read().split('\n')
    items = filter(lambda x: x, items)
    t = int(items[0])
    items = items[1:]
    for i in range(t):
        line = items[i].split()
        n = int(line[0])
        line = line[1:]
        ts = []
        for j in range(n):
            color = line[2*j]
            position = int(line[2*j+1])
            ts.append((color, position))
        game = Game(ts)
        steps = game.run()
        print "Case #%d: %d" % (i+1, steps)


                                   

