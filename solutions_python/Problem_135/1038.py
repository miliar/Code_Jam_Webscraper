__author__ = 'ezequiel'
from manager import Manager


class MagicTrick(Manager):

    def main(self):
        for t in range(self.testcases):
            self.output.write("Case #%s: " % (t + 1))
            answer1 = int(self.input.readline().strip())
            cards1 = [[int(x) for x in self.input.readline().strip().split(' ')] for i in range(4)]
            answer2 = int(self.input.readline().strip())
            cards2 = [[int(x) for x in self.input.readline().strip().split(' ')] for i in range(4)]

            possibleCards1 = set(cards1[answer1 - 1])
            possibleCards2 = set(cards2[answer2 - 1])
            possibleCards = possibleCards1 & possibleCards2

            if len(possibleCards) == 1:
                self.output.write(str(possibleCards.pop()) + "\n")
            elif len(possibleCards) == 0:
                self.output.write("Volunteer cheated!" + "\n")
            else:
                self.output.write("Bad magician!" + "\n")
        self.output.close()

program = MagicTrick('/home/ezequiel/Descargas/A-small-attempt0.in')
program.main()
