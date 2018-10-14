class BotTrustParser(object):

    def parse_case(self, case):
        parsed_case = {
            'O': [],
            'B': [],
            'order': []
        }

        buttons = case.split(' ')[0]
        case = case[case.index(' ') + 1:].split(' ')
        for term in case:
            if term in "OB":
                parsed_case['order'].append(term)
            else:
                parsed_case[parsed_case['order'][-1]].append(int(term))

        assert int(buttons) == len(parsed_case['order']), \
                "Should have %s buttons" % buttons

        return parsed_case

    def parse_game(self, game):
        """Parse the given game and return a list of `dict`, one for each case.

        :game: file like object containing the entire game input

        """
        number_cases = int(game.readline())

        parsed_game = []
        case_num = 1
        for case in game:
            print "Parsing case %d" % case_num
            parsed_game.append(self.parse_case(case.replace('\n', '')))
            case_num += 1

        assert number_cases == len(parsed_game)

        return parsed_game


class BotTrustCaseSolver(object):

    def __init__(self, case):
        self.game = Game(case['order'])
        self.bots = [
                Bot('O', case['O'], self.game),
                Bot('B', case['B'], self.game)
        ]


    def solve_case(self):
        # We're done when there are no more buttons to push
        while not self.game.is_finished():
            pushed = False
            for bot in self.bots:
                if bot.play():
                    pushed = True

            self.game.time += 1
            if pushed:
                self.game.push()

        return self.game.time


class Game(object):

    def __init__(self, order):
        self.order = order
        self.pushed = 0 # index in self.order of the next bot to push
        self.time = 0


    def is_finished(self):
        return self.pushed == len(self.order)


    def next_pusher(self):
        return self.order[self.pushed]

    def push(self):
        self.pushed += 1


class Bot(object):

    def __init__(self, colour, buttons, game):
        self.game = game
        self.colour = colour
        self.buttons = buttons

        self.position = 1
        self.pushed = 0
        # Cache the next button. 0 means nothing to do
        self.next = self.buttons[self.pushed] if self.buttons else 0

    def play(self):
        if not self.next:
            return

        # Move
        # ----
        # If I'm not at the right button
        if self.position < self.next:
            self.position += 1
        elif self.position > self.next:
            self.position -= 1

        # Push
        # ----
        # If it's my turn
        elif self.colour == self.game.next_pusher():
            self.pushed += 1
            if self.pushed < len(self.buttons):
                self.next = self.buttons[self.pushed]
            else:
                # We've pushed all our buttons
                self.next = 0

            return True

        # Wait

def solve(input):
    parser = BotTrustParser()
    with open(input) as input_file:
        cases = parser.parse_game(input_file)

    times = []
    for i, case in enumerate(cases):
        solver = BotTrustCaseSolver(case)
        print "Solving case %d..." % (i + 1)
        time = solver.solve_case()

        times.append("Case #%d: %d\n" % (i + 1, time))

    with open(input.replace(".in", ".out"), 'w') as output:
        output.writelines(times)


if __name__ == "__main__":
    import sys
    solve(sys.argv[1])
