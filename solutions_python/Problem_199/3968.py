
s = int(raw_input(''))

for case in range(s):
    row = raw_input('')
    ch,k = str.split(row,' ')
    k = int(k)
    
    combs = []
    combs.append(list(ch))
    steps = []
    steps.append(0)

    solution = -1

    if str.find(ch,'-') < 0:
        solution = 0
        k = len(ch)+1

    for i in range(len(ch) - k + 1):
        todo = len(combs)
        for c in range(todo):
            this = combs[c][:]
            step = steps[c] + 1
            for j in range(k):
                if this[i+j] == '+':
                    this[i+j] = '-'
                elif this[i+j] == '-':
                    this[i+j] = '+'

            if str.find(''.join(this),'-') < 0:
                solution = step
                break
            else:
                if not this in combs:
                    combs.append(this)
                    steps.append(step)
    if solution == -1:
        print("Case #" + str(case+1) + ": IMPOSSIBLE")
    else:
        print("Case #" + str(case+1) + ": " + str(solution))

