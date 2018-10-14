# -*- coding: utf-8 -*-

with file("A-large-0.in") as inp:
    with file("A-large-0.out", "w") as outp:
        n = int(inp.readline().strip())
        for i in xrange(n):
            raw_seq = inp.readline().strip().split()[1:]
            #if i != 3: continue
            seq = zip(raw_seq[:-1:2], raw_seq[1::2])
            pos = {"O": 1, "B": 1}
            steps_made = {"O": 0, "B": 0}
            steps = 0
            print seq
            for bot, button_s in seq:
                #print "-----"
                button = int(button_s)
                steps_to_make = abs(pos[bot] - button) + 1
                #print bot, button, pos, steps_to_make, steps_made
                other_bot = "O" if bot == "B" else "B"
                if steps_made[other_bot] >= steps_to_make:
                    additional_steps = 1
                else:
                    additional_steps = steps_to_make - steps_made[other_bot]
                steps_made[bot] += additional_steps
                steps_made[other_bot] = 0
                steps += additional_steps
                #print additional_steps
                pos[bot] = button
            print steps
            outp.write("Case #%s: %s\n" % (i+1, steps))

