import sys

cin = sys.stdin
cin.next() # skip line saying number of cases

case = 0
for line in cin:
    case += 1
    line = line.strip()
    orange = [0, 1] # time, pos
    blue = [0, 1] # time, pos
    moves = line.split(' ')[1:]

    for i in range(0, len(moves), 2):
        bot, other = (orange, blue) if moves[i] == 'O' else (blue, orange)
        dest = int(moves[i+1])
        time_for_move = abs(dest - bot[1])
        bot[1] = dest
        bot[0] = max(bot[0] + time_for_move + 1, other[0] + 1)
    print("Case #%d: %d" % (case, max(blue[0], orange[0])))


