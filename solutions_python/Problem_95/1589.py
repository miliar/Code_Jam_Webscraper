import sys

def learn():
    code = ['y qee','ejp mysljylc kd kxveddknmc re jsicpdrysi','rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd','de kr kd eoya kw aej tysr re ujdr lkgc jv']
    decode = ['a zoo','our language is impossible to understand','there are twenty six factorial possibilities','so it is okay if you want to just give up']
    cipher = {' ':' '}
    reversecipher = {' ':' '}
    length = len(code)
    for indx in range(length):
        codeItem = list(code[indx])
        decodeItem = list(decode[indx])
        codeLen = len(codeItem)
        for x in range(codeLen):
            c1 = codeItem[x]
            d1 = decodeItem[x]
            if c1 not in cipher:
                cipher[c1] = d1
            if d1 not in reversecipher:
                reversecipher[d1] = c1                
    notfoundkeyincipher = []
    notfoundvalincipher = []
    for key in list('abdefghijklmnopqrstuvwxyz'):
        if key not in cipher:
            notfoundkeyincipher.append(key)
        if key not in reversecipher:
            notfoundvalincipher.append(key)
    length = len(notfoundkeyincipher)
    for indx in range(length):
        c1 = notfoundkeyincipher[indx]
        d1 = notfoundvalincipher[indx]
        if c1 not in cipher:
            cipher[c1] = d1
        if d1 not in reversecipher:
            reversecipher[d1] = c1         
    return cipher

def main():
    from sys import stdin, stdout
    cipher = learn()

    first_in = stdin.readline()
    testcases = int(first_in)
    inputs = stdin.readlines()
    count = 1
    for indx in range(testcases):
        item = inputs[indx]
        output = []
        for key in list(item.strip()):
            output.append(cipher[key])
        print "Case #"+str(count)+": "+"".join(output)
        count += 1
    # thing = first_in.split()
    # n = int(thing[0])
    # k = int(thing[1])
    # total = 0

    # list = stdin.readlines()
    # for item in list:
    #     if int(item) % k == 0:
    #         total += 1

    # stdout.write(str(total) + "\n")

if __name__ == "__main__":
    main()



    
    
