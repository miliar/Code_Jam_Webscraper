#!/usr/bin/env python

class Bot():
    def __init__(self):
        self.time = 0
        self.loc = 1

    def curloc(self,t):
        return self.loc + (t - self.time)

    def there(self, button):
        # time to get there
        return self.time + abs(self.loc - button)
        
    
cases = int(raw_input())
for case in range(cases):
    t=0
    inp = raw_input().split(' ')
    #print inp
    n = int(inp.pop(0))
    assert (2*n == len(inp))
    bots = {'O':Bot(), 'B':Bot()}
    while inp:
        botcolor = inp.pop(0)
        button = int(inp.pop(0))
        #print botcolor, button

        if t < button:
            t = button
        bot = bots[botcolor]
        # see if the bot is already there
        if bot.there(button) <= t:
            # bot is there, push btton
                t += 1
        else:
            # get there
            t = bot.there(button)
            # push button
            t+=1
        bot.loc = button
        bot.time = t
      
    print "Case #%d: %d" % (case + 1, t-1)
