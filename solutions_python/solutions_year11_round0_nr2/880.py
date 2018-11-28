import sys

'''
combine = {'Q' : {'F' : 'T'},
           'F' : {'Q' : 'T'}}
oppose = {'Q' : ['F'],
          'F' : ['Q']}

in_letters = ['F']

last_letter = 'F'
seq = ['F']
'''

combine = {}
oppose = {}
in_letters = []

def do_combine(a, b):
    has = combine.get(a)

    if not has:
        return None

    return has.get(b)

def do_oppose(a):
    for letter in in_letters:
        l = oppose.get(letter)
        if l:
            if a in l:
                return True
    return False

def pretty_print(i, l):
    print 'Case #' + str(i) + ': [' + ', '.join(l) + ']'

def clear_dict(d, value):
    for l in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if value == {}:
            d[l] = {}
        else:
            d[l] = []

if __name__ == '__main__':
    #print do_combine('Q', 'X') 
    #print do_oppose('Q')

    data = sys.stdin.readlines()[1:]
    for p, line in enumerate(data):
        clear_dict(combine, {})
        clear_dict(oppose, [])
        in_letters = []
        sp = line.split()
        C = int(sp.pop(0))
        for i in range(C):
            x = sp.pop(0)
            combine[x[0]][x[1]] = x[2]
            combine[x[1]][x[0]] = x[2]

        D = int(sp.pop(0))
        for i in range (D):
            x = sp.pop(0)
            oppose[x[0]].append(x[1])
            oppose[x[1]].append(x[0])

        sp.pop(0)
        for letter in sp.pop(0):
            if in_letters == []:
                in_letters.append(letter)
                continue
            x = do_combine(in_letters[-1], letter)
            if x:
                in_letters[-1] = x
            elif do_oppose(letter):
                in_letters = []
            else:
                in_letters.append(letter)


        pretty_print(p+1, in_letters)

    sys.exit(0)
