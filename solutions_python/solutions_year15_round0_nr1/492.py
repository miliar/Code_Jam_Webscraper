file_in = open('A-large.in', 'r')
file_out = open('A-large.out', 'w')

T = int(file_in.readline())

for tid in range(T):
    file_out.write('Case #%d: ' % (tid+1))
    line = file_in.readline()
    line = line.replace('\n', '').split(' ')
    S_max = int(line[0])
    aud = [int(ch) for ch in line[1]]
    standup = aud[0]
    invite = 0
    for i in range(1, len(aud)):
        if i > standup:
            diff = i-standup
            standup += diff
            invite += diff
        standup += aud[i]
    file_out.write(str(invite) + '\n')
