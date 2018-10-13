#!/usr/bin/env python3
data = open('robots.in')
class robot(object):
    time = 0
    pos = 1

for i in range(1, int(data.readline())+1):
    orange = robot()
    blue = robot()
    act = 0
    actions = data.readline().split(' ')
    while act < int(actions[0]):
        act+=1
        bot = orange if actions[2*act-1] == 'O' else blue
        to = int(actions[2*act])
        bot.time += abs(to-bot.pos) + 1
        bot.pos = to
        other = orange if bot is blue else blue
        if other.time >= bot.time: bot.time = other.time+1
    print('Case #%d: %d' % (i, max(orange.time, blue.time)))

