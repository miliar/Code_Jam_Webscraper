import sys

text = sys.stdin.read().strip()
lines = text.split('\n')

test_case_count = int(lines.pop(0))
assert test_case_count == len(lines)

def sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0

case_n = 0
for line in lines:
    case_n += 1
    seq = []

    parts = line.split()
    button_count = int(parts.pop(0))
    assert button_count * 2 == len(parts)
    
    for i in xrange(0, len(parts), 2):
        seq.append([parts[i], int(parts[i+1])])

    bot_loc = {'O': 1, 'B': 1}
    time_passed = 0
    while len(seq) > 0:
        time_passed += 1
        who, btn = seq[0]
        #print time_passed, " ",
        for bot in ('O', 'B'):
            next_bot_btn = None
            for _who, _btn in seq:
                if _who == bot:
                    next_bot_btn = _btn
                    break
            if next_bot_btn is None:
                #print "do nothing", " ",
                continue
            if bot_loc[bot] == btn and who == bot:
                #print "push button", btn, " ",
                seq.pop(0)
            elif bot_loc[bot] == next_bot_btn:
                #print "stay at button", bot_loc[bot], " ",
                pass
            else:
                bot_loc[bot] += sign(next_bot_btn - bot_loc[bot])
                #print "move to button", bot_loc[bot], " ",
        #print
    print("Case #%i: %i" % (case_n, time_passed))
