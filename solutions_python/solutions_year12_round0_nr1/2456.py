#

samples = [
        ('y qee z', 'a zoo q'),
        ('ejp mysljylc kd kxveddknmc re jsicpdrysi', 'our language is impossible to understand'),
        ('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'there are twenty six factorial possibilities'),
        ('de kr kd eoya kw aej tysr re ujdr lkgc jv', 'so it is okay if you want to just give up')]

alphabet = {}

def BuildMap():
    for test in samples:
        a = test[0]
        b = test[1]

        assert(len(a) == len(b))
        for idx in range(0, len(a)):
            ca = a[idx]
            cb = b[idx]
            #print(ca + ' -> ' + cb)
            alphabet[ca] = cb
        #print(test)

    #alphabet = sorted(alphabet)

    keys = []
    vals = []
    for key,val in alphabet.iteritems():
        keys.append(key)
        vals.append(val)

    keys.sort()
    vals.sort()
    #print keys
    #print vals

    for key,val in alphabet.iteritems():
        assert(val in keys)
        assert(key in vals)

    
def Translate(input, counter):
    output = 'Case #' + str(counter) + ': '
    counter += 1

    for char in input:
        output += alphabet[char]

    output += '\n'
    return output 


if __name__ == "__main__":
    BuildMap()
    
    file_ = 'A-small-attempt1.in'
    inputdata = open(file_).read().split('\n')
   
    count = int(inputdata.pop(0))

    output = open(file_ + '.out', 'w')

    counter = 1
    for line in inputdata:
        #print line, len(line)
        trans = Translate(line, counter)
        counter += 1

        if(len(line)):
            output.write(trans)
   

    #for test in inputs:
    #    Translate(test, counter)
    #    counter += 1

    #if len(sys.argv) < 2:
    #    sys.exit('Need command line arguments!')
