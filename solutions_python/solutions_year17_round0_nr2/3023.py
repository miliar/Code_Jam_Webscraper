# Imports

# Constants
DEBUG = True

# Filenames
f_name = 'B-large.in'#'test.in'#'B-small-attempt1.in'#
f2_name = 'B.out'

def isTidy(num):
    return "".join(sorted(num)) == num

with open(f_name) as f:
    with open(f2_name,'w') as f2:
        i = 0
        f.readline() # Discard first line
        for line in f:
            i += 1
            result = ''
            # Do the processing of each line
            result = int(line)
            if (not isTidy(str(result))):
                for j in range(len(line)):
                    for k in range(1, 10):
                        resultStr = str(result)
                        if (resultStr[len(resultStr) - 1 - j] == '9'):
                            break
                        result = result - (10**j)
                        resultStr = str(result)
                        #print("j: {}, k: {}, resultStr: {}".format(j, k, resultStr))
                        if (isTidy(resultStr)):
                            break
                        if (resultStr[len(resultStr) - 1 - j] == '9'):
                            break
                    if (isTidy(resultStr)):
                        break
            # Print this line
            print("Case #{}: {}".format(i, result), file=f2)

if DEBUG:
    with open(f2_name) as f2:
        for line in f2:
            print(line, end='')