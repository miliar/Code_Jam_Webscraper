mapping = {'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', \
           'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b', \
           'o':'k', 'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j', \
           'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q'}

def decode(line):
    answer = []
    for char in line:
        if char == ' ':
            answer.append(' ')
        else:
            answer.append(mapping[char])
    return ''.join(answer)

def run():
    f = open('A-small-attempt1 (1).in', 'r')
    lines = f.readlines()
    f.close()
    data = [line.rstrip() for line in lines]
    cases = int(lines[0])
    counter = 1

    g = open('Aanswers.txt', 'w')

    for i in range(cases):
        line = data[counter]
        g.write('Case #' + str(counter) + ': ' + str(decode(line)) + '\n')
        counter += 1

    g.close()
