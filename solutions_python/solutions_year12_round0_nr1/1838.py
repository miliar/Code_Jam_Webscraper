import case

__author__ = 'dmorgant'

letterMap = { 'a' : 'y',
              'b' : 'h',
              'c' : 'e',
              'd' : 's',
              'e' : 'o',
              'f' : 'c',
              'g' : 'v',
              'h' : 'x',
              'i' : 'd',
              'j' : 'u',
              'k' : 'i',
              'l' : 'g',
              'm' : 'l',
              'n' : 'b',
              'o' : 'k',
              'p' : 'r',
              'q' : 'z',
              'r' : 't',
              's' : 'n',
              't' : 'w',
              'u' : 'j',
              'v' : 'p',
              'w' : 'f',
              'x' : 'm',
              'y' : 'a',
              'z' : 'q',
              ' ' : ' '}


def process(input):
    lines = input.splitlines()
    number = int(lines[0])
    output = ""
    for c in range(1, number + 1):
        solver = TongueSolver(lines[c])
        output += case.Case(c, solver).output()

    return output.strip()


class TongueSolver:
    def __init__(self, text):
        self.text = text

    def solve(self):
        output = ""
        
        for c in self.text:
            output += letterMap[c]

        return output
        