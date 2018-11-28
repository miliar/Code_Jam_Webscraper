from bottrust import bot_trust

name_input = raw_input('Input file: ')

entry = open(name_input, 'r').read().split('\n')

T = int(entry.pop(0))

result = []

for case in range(T):
    content = entry[case].partition(' ')
    result.append('Case #%d: %d' % (case+1, bot_trust(int(content[0]),content[2])))

output = file('result.in', 'w')
output.write('\n'.join(result))
output.close()
