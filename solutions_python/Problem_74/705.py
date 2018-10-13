#!/usr/bin/python

import sys

# Store their locations.
orange = None
blue = None

# Let's do this properly.
class RobotAction:
    def __init__(self, bot, button):
        self.bot = bot
        self.button = int(button)

# This will be useful to look ahead.
def findNextAction(bot, list, current):
    amount = len(list)

    current += 1
    while current < amount:
        currentAction = list[current]

        if currentAction.bot == bot:
            return currentAction

        current += 1

    return None

# Let's not type these constants over and over.
def oppositeBot(bot):
    if bot == "O":
        return "B"
    elif bot == "B":
        return "O"

def move(bot, amount):
    global orange, blue

    if bot == "O":
        orange += amount
    elif bot == "B":
        blue += amount

def getDirection(currentAction):
    global orange, blue

    bot = currentAction.bot
    button = currentAction.button
    loc = 0

    if bot == "O":
        loc = orange
    elif bot == "B":
        loc = blue

    if loc == button:
        return 0
    elif loc < button:
        return 1
    elif loc > button:
        return - 1

# Read the input file.
f = open(sys.argv[1], "r")
fo = open(sys.argv[1].replace("in", "out"), "w")
lines = f.readlines()
f.close()

testCases = int(lines.pop(0).strip())

i = 0
while i < testCases:
    orange = 1
    blue = 1

    i += 1

    line = lines.pop(0).strip()
    chars = line.split(' ')
    amount = int(chars[0])

    actions = []

    # We need to look ahead, so first gather the actions.
    j = 0
    while j < amount:
        bot = chars[1 + j * 2]
        button = chars[1 + j * 2 + 1]

        actions.append(RobotAction(bot, button))

        j += 1

    # As they are now gathered, we can let our robots walk.
    t = 0
    j = 0
    while j < amount:
        currentAction = actions[j]
        opp = oppositeBot(currentAction.bot)

        direction = getDirection(currentAction)

        while direction != 0:
            move(currentAction.bot, direction)

            oppAction = findNextAction(opp, actions, j)
            if oppAction != None:
                oppDirection = getDirection(oppAction)
                move (oppAction.bot, oppDirection)

            t += 1
            direction = getDirection(currentAction)

        oppAction = findNextAction(opp, actions, j)
        if oppAction != None:
            oppDirection = getDirection(oppAction)
            move (oppAction.bot, oppDirection)

        t += 1

        j += 1

    fo.write("Case #" + str(i) + ": " + str(t) + "\n")

fo.close()
