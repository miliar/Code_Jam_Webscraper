unicorns = {'R': 0, 'O': 0, 'Y': 0, 'G': 0, 'B': 0, 'V': 0}
order = []
numUnicorns = 0

def add(colour):
    if (not unicorns[colour]):
        return False
    order.append(colour)
    unicorns[colour] -= 1
    return True

numCases = int(input())
for i in range(1, numCases+1):
    numUnicorns, unicorns['R'], unicorns['O'], unicorns['Y'], unicorns['G'], unicorns['B'], unicorns['V'] = [int(s) for s in raw_input().split(" ")]
    if (unicorns['R']):
        add('R')
    elif (unicorns['Y']):
        add('Y')
    elif (unicorns['B']):
        add('B')
    elif (unicorns['O']):
        add('O')
    elif (unicorns['G']):
        add('G')
    elif (unicorns['V']):
        add('V')

    valid = False
    for n in range(1, numUnicorns):
        prev = order[n-1]
        if (prev == 'O'):
            valid = add('B')
        elif (prev == 'G'):
            valid = add('R')
        elif (prev == 'V'):
            valid = add('Y')
        elif (prev == 'R'):
            if(unicorns['G']):
                valid = add('G')
            elif(unicorns['O']):
                valid = add('B')
            elif(unicorns['V']):
                valid = add('Y')
            elif(unicorns['B'] and (unicorns['B'] >= unicorns['Y'])):
                valid = add('B')
            elif(unicorns['Y']):
                valid = add('Y')
            else:
                valid = False
        elif (prev == 'B'):
            if(unicorns['O']):
                valid = add('O')
            elif(unicorns['G']):
                valid = add('R')
            elif (unicorns['V']):
                valid = add('Y')
            elif(unicorns['R'] and (unicorns['R'] >= unicorns['Y'])):
                valid = add('R')
            elif(unicorns['Y']):
                valid = add('Y')
            else:
                valid = False
        elif(prev == 'Y'):
            if(unicorns['V']):
                valid = add('V')
            elif(unicorns['O']):
                valid = add('B')
            elif(unicorns['G']):
                valid = add('R')
            elif(unicorns['R'] and (unicorns['R'] >= unicorns['B'])):
                valid = add('R')
            elif(unicorns['B']):
                valid = add('B')
            else:
                valid = False

        if(not valid):
            break

    if (len(order) == numUnicorns and valid):
        n = numUnicorns-1
        if (order[0] == order[n]):
            valid = False
        elif (order[0] == 'O' and (order[n] == 'R' or order[n] == 'Y')):
            valid = False
        elif (order[0] == 'G' and (order[n] == 'B' or order[n] == 'Y')):
            valid = False
        elif  (order[0] == 'V' and (order[n] == 'R' or order[n] == 'B')):
            valid = False
        else:
            valid = True

    output = 'IMPOSSIBLE'
    if (valid):
        output = ''.join(order)

    order = []

    print("Case #{}: {}").format(i, output)
