import sys,os

filename = sys.argv[1].strip()

# Open input file and read lines
ifile = open(filename+'.in','r')
all = ifile.readlines()
ifile.close()

ofile = open(filename+'.out','w')

# Read in L, D, N parameters
params = all[0][:-1].split(' ')
while (params.count('')>0):
    params.remove('')
num_letters = int(params[0])
num_dictionary = int(params[1])
num_cases = int(params[2])

# Read dictionary lines and store as list
dictionary = []
n = 1
while (n <= num_dictionary):
    dictionary.append(all[n][:-1].strip(' '))
    n = n + 1

# Read and interpret cases and count possible matches
m = 1
for line in all[num_dictionary+1:]:
    print str(m) + " START"
    line = line[:-1]
    # Create list for each letter in a word
    words = []
    n = 0
    while (n < num_letters):
        words.append([])
        n = n + 1
    n = 0
    lettern = 0
    status = 0
    print str(m) + " LISTS"
    while (n < len(line)):
        if (line[n]=="("):
            status = 1
        elif (line[n]==")"):
            status = 0
            lettern = lettern + 1
        elif (status==1):
            words[lettern].append(line[n])
        elif (status==0):
            words[lettern].append(line[n])
            lettern = lettern + 1
        n = n + 1

    counter = 0
    for word in dictionary:
        good = "yes"
        n = 0
        while (n < num_letters):
            letter = word[n]
            if (letter in words[n]):
                pass
            else:
                good = "no"
            n = n + 1
        if (good=="yes"):
            counter = counter + 1

    ofile.write('Case #%i: %i\n' % (m,counter))
    print 'Case #%i: %i' % (m,counter)

    m = m + 1

ofile.close()
