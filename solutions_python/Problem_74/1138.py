class Robot:
    def __init__(self, order):
        self.order = order
        self.step = 0
        self.door = [1, 1]

    def getNext(self, inactive):
        if inactive == 0:
            inc = 'O'
        else:
            inc = 'B'

        for a in self.order[self.step:]:
            if a[0] == inc:
                return a[1]
        return None

    def go(self):
        current = self.order[self.step]

        if current[0] == 'O':
            active = 0
            inactive = 1
        else:
            active = 1
            inactive = 0

        _next = self.getNext(inactive)

        if self.door[active] == int(current[1]):
            self.step = self.step + 1
        elif self.door[active] > int(current[1]):
            self.door[active] = self.door[active] - 1
        else:
            self.door[active] = self.door[active] + 1

        if _next is not None:
            if self.door[inactive] > int(_next):
                self.door[inactive] = self.door[inactive] - 1
            elif self.door[inactive] < int(_next):
                self.door[inactive] = self.door[inactive] + 1


        if self.step >= len(self.order):
            return True

        return False

def getInput():
    l = []

    line = raw_input()
    sp = line.split()
    num = int(sp[0])

    for x in range(num):
        l.append((sp[x * 2 + 1], sp[x * 2 + 2]))

    return l


num = int(raw_input())

for x in range(num):
    order = getInput()
    bot = Robot(order)

    count = 0
    done = False

    while not done:
        done = bot.go()
        count = count + 1

    print "Case #" + str(x + 1) + ": " + str(count)
