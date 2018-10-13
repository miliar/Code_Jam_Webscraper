import psyco

f = open("input.txt")

numcases = int(f.readline())

for case in xrange(numcases):
    line = f.readline()
    line = line.split(" ")

    numrules = int(line[0])

    rules = {}
    for rulestr in line[1:numrules+1]:
        ch1 = rulestr[0]
        ch2 = rulestr[1]
        ch3 = rulestr[2]
        rules.setdefault(ch1,{ch2:ch3})
        rules.setdefault(ch2,{ch1:ch3})

    line = line[numrules+1:]
    numoppose = int(line[0])
    oppose = {}
    for opposestr in line[1:numoppose+1]:
        ch1 = opposestr[0]
        ch2 = opposestr[1]
        oppose.setdefault(ch1,set(ch2))
        oppose.setdefault(ch2,set(ch1))

        oppose[ch1].add(ch2)
        oppose[ch2].add(ch1)
        
    instring = line[-1][:-1]
##    print instring

    stack = []
    for char in instring:
        stack.append(char)
        if len(stack) < 2:
            continue

        edited = True
        while(edited):
            edited = False
            try:
                comb = rules[stack[-1]][stack[-2]]
##                print "Rule %s%s%s" % (stack[-1], stack[-2], comb)
                stack = stack[:-2]
                stack.append(comb)
                edited = True
                continue
            except KeyError:
                pass
            
            try:
                bad = oppose[stack[-1]]
                test = set(stack[:-1])
                if len(test.intersection(bad)) > 0:
                    stack = []
                continue
            except KeyError:
                pass

##        print stack

    result = "["
    for char in stack:
        result += char + ", "
    result = result[:-2] + "]"
    
    if len(stack) == 0:
        result = "[]"
    
    print "Case #%d: %s" %(case + 1, result)

f.close()
