# look for the first minus sign
# flip()
# go to the next minus sign
# etc
# if everything has been flipped we are good, otherwise print IMPOSSIBLE

for T in range(1, int(raw_input()) + 1):
    # we will be printing "Case #T: Answer
    a, b = raw_input().split()
    signs = list(a) # string input of pluses and minuses
    flipperLen = int(b)
    
    i = 0
    timesChanged = 0
    while i < len(signs) - flipperLen + 1:
        if signs[i] == '-':
            # change to happy
            for count in range(flipperLen):
                if signs[i+count] == '-':
                    signs[i+count] = '+'
                elif signs[i+count] == '+':
                    signs[i+count] = '-'
            # remember how many times we became happy
            timesChanged += 1
            #print("changed to: " + str(signs))
        i+=1
    successful = True
    # now search for a minus sign
    for sign in signs:
        if sign == '-':
            successful = False
    if successful:
        print("Case #" + str(T) + ": " + str(timesChanged))
    else:
        print("Case #" + str(T) + ": IMPOSSIBLE")