class PancakeStream(object):

    def __init__(self, pancakes, flipperSize):
        self.pancakes = [True if currPancake=='+' else False for currPancake in pancakes]
        self.flipperSize = flipperSize if isinstance(flipperSize, int) else int(flipperSize)

    def IsDone(self):
        return all(self.pancakes)

    def FlipPancakes(self, position):
        if position < 0 or position > (len(self.pancakes) - self.flipperSize): raise ValueError()

        for i in range(position, position+self.flipperSize):
            self.pancakes[i] = not self.pancakes[i]

    def ToString(self):
        return ''.join('+' if pancake else '-' for pancake in self.pancakes)

    def FirstUnflipPancake(self):
        for i, value in enumerate(self.pancakes):
            if not value: return i

        return -1

    @staticmethod
    def AutoSolve(pancakes, flipperSize, printMidSteps=False):
        pancakes = PancakeStream(pancakes, flipperSize)

        try:
            flipCount = 0
            while not pancakes.IsDone():
                pos = pancakes.FirstUnflipPancake()
                pancakes.FlipPancakes(pos)
                if printMidSteps: print(pancakes.ToString())
                flipCount += 1

            return str(flipCount)

        except ValueError:
            return 'IMPOSSIBLE'


def solver():
    output = []

    casesToSolve = int(input())
    for i in range(1, casesToSolve+1):
        pancakes, flipperSize = input().split(' ')
        output.append('Case #%s: %s' % (i, PancakeStream.AutoSolve(pancakes, flipperSize)))

    print('\n'.join(output))

solver()

