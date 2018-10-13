#!/usr/bin/python2.7

import sys

class Robot(object):
    def __init__(self, destinations):
        self.position = 1
        self.destinations = destinations
        self.next_order()

    def advance(self):
        if self.destination > self.position:
            self.position += 1
        elif self.destination < self.position:
            self.position -= 1

    def at_position(self):
        return self.position == self.destination

    def next_order(self):
        self.destination = self.destinations.pop(0) if self.destinations else self.position
        

def solve(nof_orders, orders):
    robots = {}
    for color in ['O', 'B']:
        robo_orders = [int(orders[index + 1]) for index in xrange(0, 2 * nof_orders, 2) if orders[index] == color]
        robots[color] = Robot(robo_orders)

    moves = orders[::2]

    time = 0
    while len(moves) > 0:
        next_robot = robots[moves.pop(0)]

        while not next_robot.at_position():
            for robo in robots.values():
                robo.advance()
            time += 1

        # Advance all robots while button is being pressed
        for robo in robots.values():
            robo.advance()
        time += 1

        # Give pusher a new order
        next_robot.next_order()
    
    return time

with open(sys.argv[1]) as input_file:
    input_file.readline() # ignore the first line
    for case, line in enumerate(input_file):
        fields = line.split()
        nof_orders = int(fields[0])
        orders = fields[1:]

        answer = solve(nof_orders, orders)

        print "Case #%d: %d" % (case + 1, answer)

# vim: ts=4:sw=4:expandtab
