#!/usr/bin/env python


class Bot(object):
    def __init__(self):
        # position of last button
        self.pos = 1
        # time of last button push
        self.time = 1

    def move(self, pos, cur_time):
        '''Given the position of the button and the current
        time, return how long it will take to get there and
        update the position/time accordingly.
        '''
        distance = abs(self.pos - pos)
        time_since = cur_time - self.time

        if time_since < distance:
            # we need more time to get to the button
            travel_time = distance - time_since
        else:
            travel_time = 0

        #print "need to go: ", distance
        #print "have this much travel time:", time_since
        #print "need this much travel time:", travel_time

        # push the button
        travel_time += 1
        #print "total time =", travel_time
        self.pos = pos
        self.time = cur_time + travel_time

        return travel_time



def solve(data):
    bots = {'O': Bot(),
            'B': Bot(),
           }
    curr_time = 1
    for (bot, button) in data:
        #print "pushing", bot, button
        curr_time += bots[bot].move(button, curr_time)

    return curr_time - 1


def parse_data(data):
    bot = data[::2]
    button = [int(n) for n in data[1::2]]
    return zip(bot, button)

if __name__ == '__main__':
    import sys

    f = open(sys.argv[1], 'r')

    lines = enumerate(f.readlines())
    lines.next()

    for i, line in lines:
        data = [n for n in line.strip().split()[1:]]
        data = parse_data(data)
        print "Case #%s: %s" % (i, solve(data))
