# Imports

# Constants
DEBUG = True

# Filenames
f_name = 'A-large.in'#'A-small-attempt0.in'#'test.in'
f2_name = 'A.out'


trantab = str.maketrans('-+', '+-')
with open(f_name) as f:
    with open(f2_name,'w') as f2:
        i = 0
        f.readline() # Discard first line
        for line in f:
            i += 1
            result = ''
            # Do the processing of each line
            j = 0
            s, k = line.split(' ')
            k = int(k)
            s = list(s)
            for l in range(len(s) - k + 1):
                if s[l] == '-':
                    j += 1
                    for m in range(k):
                        s[l+m] = s[l+m].translate(trantab)
            s = "".join(s)
            #print(s)
            if '-' in s:
                result = "IMPOSSIBLE"
            else:
                result = j
            # Print this line
            print("Case #{}: {}".format(i, result), file=f2)

if DEBUG:
    with open(f2_name) as f2:
        for line in f2:
            print(line, end='')