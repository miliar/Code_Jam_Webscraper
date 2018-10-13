def allHappy(order):
    for letter in order:
        if letter == '-':
            return 0
    return 1

def toggle(order, offset):
    orderlist = list(order)
    if orderlist[offset] == '+':
        orderlist[offset] = '-'
    else:
        orderlist[offset] = '+'
    order2 = ''.join(orderlist)
    return(order2)

# Open file
filepath = "A-small-attempt0.in"
f = open(filepath, 'r')

pancakes = []

# Read input
i = 0
for line in f:
    # First line: Number of cases
    if i == 0:
        cases = int(line)
        i = i + 1
        continue
    # Next lines
    sp = line.split()
    if len(sp) > 1:
        pancakes += [[sp[0], int(sp[1])]]
    i = i + 1

# Take each case
solutions = []
caseNumber = 0
for case in pancakes:
    order = case[0]
    size  = case[1]

    # First attempt
    print ('Original:' + order)
    attempts = 0
    for i in range (1, 1000): # UNNECESSARY
        if allHappy(order):
            solutions += [attempts]
            break
        # If last one is not happy...
        print (-i)
        if (order[-i]) == '-':
            if i + size > len(order) + 1:
                break
            # Flip last three
            for j in range(0, size):
                order = toggle(order, -i - j)
            attempts = attempts + 1
            print (order)
    if not allHappy(order):
        solutions += ["IMPOSSIBLE"]
    caseNumber = caseNumber + 1
    #order = toggle(order, 2)


# Output
i = 1
for s in solutions:
    print "Case #" + str(i) + ": " + str(s)
    i = i + 1

# Code recycling bin
#binary = order.replace ('+', '1')
#binary = binary.replace('-', '0')
#binary = int(binary, 2)
#print bin(binary)
#toggleBit(binary, 2)
#print bin(binary)

#def toggleBit(int, offset):
#    mask = 1 << offset
#    return(int ^ mask)
