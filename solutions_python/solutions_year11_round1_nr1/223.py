def main():
    filename = raw_input('File: ')
    file = open(filename)
    output = []
    # logic goes here, append results to output list
    numcases = int(file.readline())
    for i in range(numcases):
        outputstr = "Case #" + str(i+1) + ": "
        vals = map(int, file.readline().split(" "))
        maxgt = vals[0]
        pday = vals[1]
        pever = vals[2]
        if pday < 100 and pever == 100:
            outputstr = outputstr + "Broken"
            output.append(outputstr)
            continue
        if pever == 0 and pday > 0:
            outputstr = outputstr + "Broken"
            output.append(outputstr)
            continue
        if pever == 0 and pday == 0:
            outputstr = outputstr + "Possible"
            output.append(outputstr)
            continue
        gamefactor, feh = reducefract(100, pday)
        totalfactor, bleh = reducefract(100, pever)
        gamestoday = gamefactor
        gamestotal = totalfactor
        found = False
        while not found and gamestoday <= maxgt:
            for k in range(1, gamestotal+1):
                if (k*100) / gamestotal == pever:
                    for j in range(1, gamestoday+1):
                        if (j*100) / gamestoday == pday:
                            outputstr = outputstr + "Possible"
                            output.append(outputstr)
                            found = True
                    gamestoday = gamestoday + gamefactor
            gamestotal = gamestotal + totalfactor
                    
        if not found:
            outputstr = outputstr + "Broken"
            output.append(outputstr)
    with open(filename[:-3] + '.out', 'w') as outputfile:
        for line in output:
            outputfile.write(line + "\n")

def reducefract(n, d):
    def gcd(n, d):
        while d != 0:
            t = d
            d = n%d
            n = t
        return n
    greatest=gcd(n,d)
    n/=greatest
    d/=greatest
    return n, d

if __name__ == '__main__':
    main()
