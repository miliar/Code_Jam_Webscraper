import copy
filename = 'B-large.in'
f = open(filename)

cases= []

first = True
for line in open(filename):
    if first:
        first = False
        pass
    else:
        cases.append(line)


counter = 0
output = open('output', 'w')
base = ['Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F']

for case in cases:
    counter += 1
    sp = case.split()
    num_bases = sp.pop(0)
    num_bases = int(num_bases)
    bases = []
    opposed = []
    
    for i in range(num_bases):
        bases.append(sp.pop(0))
    
    num_opposed = sp.pop(0)
    num_opposed = int(num_opposed)
    
    for i in range(num_opposed):
        opposed.append(sp.pop(0))
    
    num_letters = sp.pop(0)
    to_invoke = ([l for l in sp.pop(0)])
    invoked = []
    
    while (to_invoke):
        popped = to_invoke.pop(0)
        invoked.append(popped)
    
        if len(invoked) > 1:
            last_two = invoked[-2] + invoked[-1]
            reversed_two = invoked[-1] + invoked[-2]
            # Check if they can be tansformed and to what
            transformed = None
            for base in bases:
                bases_last_two = base[0] + base[1]
                if bases_last_two == last_two or bases_last_two == reversed_two:
                    transformed = base[2]
                    print 'transformed', transformed
                    break
    
            if transformed:
                invoked.pop()
                invoked.pop()
                invoked.append(transformed)
            else:
                for pair in opposed:
                    cloned_invoked = copy.copy(invoked)
                    if pair[0] in cloned_invoked:
                        cloned_invoked.remove(pair[0])
                        if pair[1] in cloned_invoked:
                            cloned_invoked.remove(pair[1])
                            invoked = []
                            break

    res = '['
    for l in invoked:
        if res == '[':
            res += l
        else:
            res += ', ' + l
    res += ']'

    output.write('Case #'+str(counter)+': '+res+'\n')
output.close()
