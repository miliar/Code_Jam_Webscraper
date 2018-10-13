def flip(z):
    if z == '+':
        return '-'
    else:
        return '+'

t = raw_input()
for i in range(int(t)):
    flips = 0
    stringNFlipper = raw_input()
    string,sizeFlipper = stringNFlipper.split()
    sizeFlipper = int(sizeFlipper)
    sizeString = len(string)
    if (string[0] == "+" and len(set(string))==1):
        print "Case #" + str(i+1) + ":" + " "+str(flips)
    elif (sizeString < sizeFlipper or (sizeString == sizeFlipper and len(set(string))==2)):
        print "Case #" + str(i+1) + ":" + " "+"IMPOSSIBLE"
    else:
        for c in range(sizeString-sizeFlipper+1):
            if string[c] == '+':
                continue
            else:
                for x in range(c,c+sizeFlipper):
                    string = string[:x] + flip(string[x]) + string[x + 1:]
                flips = flips+1
        if (len(set(string)) == 1):
            print "Case #" + str(i+1) + ":" + " "+str(flips)
        else:
            print "Case #" + str(i+1) + ":" + " "+"IMPOSSIBLE"
                
