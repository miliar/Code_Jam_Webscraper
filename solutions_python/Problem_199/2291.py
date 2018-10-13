def panflip(pancake, start, len):
    pc = list(pancake)
    for i in range(start, start + len):
        if(pc[i] == '+'):
            pc[i] = '-'
        else:
            pc[i] = '+'
    return ''.join(pc)

def minimumFlips(pancakes, noflips):
    minflips = 0
    while pancakes.count('-') != 0:
        minflips += pancakes.count('-' * noflips)
        pancakes = pancakes.replace('-' * noflips, '+' * noflips)
        if(pancakes.count('-') == 0):
            return minflips
        elif(len(pancakes) - pancakes.find('-') < noflips):
            return 'IMPOSSIBLE'
        else:
            minflips += 1
            pancakes = panflip(pancakes, pancakes.find('-'), noflips)
    return minflips

T = int(input())
for t in range(1, T + 1):
    sin = input()
    S = sin.split(' ')[0]
    K = int(sin.split(' ')[1])
    print('Case #' + str(t) + ': ' + str(minimumFlips(S, K)))
