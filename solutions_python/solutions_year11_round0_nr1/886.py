# pp@myelin.co.nz
# bot trust
# code jam 2011 qual A

NOISY = 0

n_cases = int(raw_input())
for case in range(n_cases):
    moves = raw_input().strip().split()
    count = int(moves.pop(0))
    assert count * 2 == len(moves)
    if NOISY: print moves

    min_time = 0
    bots = {
        'B': {
            'pos': 1,
            'time': 0,
            },
        'O': {
            'pos': 1,
            'time': 0,
            },
        }

    for m in range(count):
        botid = moves[m*2]
        button = int(moves[m*2+1])
        bot = bots[botid]

        dist = abs(button - bot['pos'])
        earliest = bot['time'] + dist
        if NOISY: print "bot %s needs to get to %d; currently at %d at time %d; will take %d, earliest %d, sync %d" % (botid, button, bot['pos'], bot['time'], dist, earliest, min_time)

        # can get into place early
        if earliest > min_time: min_time = earliest
        # and then press the button
        min_time += 1

        bot['time'] = min_time
        bot['pos'] = button
        if NOISY: print "  ", min_time, bot

    print "Case #%d: %d" % (case+1, min_time)
