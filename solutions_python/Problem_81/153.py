from string import strip

def main():
    filename = raw_input('File: ')
    file = open(filename)
    output = []
    # logic goes here, append results to output list
    numcases = int(file.readline())
    for i in range(numcases):
        output.append("Case #" + str(i+1) + ":")
        numteams = int(file.readline())
        results = []
        for j in range(numteams):
            result = tuple(file.readline().strip())
            results.append(result)
        for j in range(numteams):
            print "Doing", str(j+1), "of", str(numteams)
            output.append(str(calcrpi(results, j)))
    with open(filename[:-3] + '.out', 'w') as outputfile:
        for line in output:
            outputfile.write(line + "\n")

def calcrpi(results, teamindex):
    wins = len(filter(lambda x: x == '1', results[teamindex]))
    total = len(filter(lambda x: x == '1' or x == '0', results[teamindex]))
    wp = calcwp(wins, total)
    owp = calcowp(results, teamindex)
    oowp = calcoowp(results, teamindex)
    return rpi(wp, owp, oowp)

def calcwp(wins, total):
    return float(wins) / total

def calcowp(results, teamindex):
    owp = 0
    num = 0
    for i in range(len(results)):
        if i == teamindex:
            continue
        result = results[i]
        if result[teamindex] == '.':
            continue
        #print "owp", result, teamindex
        result = result[:teamindex] + result[teamindex+1:]
        #print "fowp", result, teamindex
        wins = len(filter(lambda x: x == '1', result))
        total = len(filter(lambda x: x == '1' or x == '0', result))
        owp = owp + calcwp(wins, total)
        num = num + 1
    #print "final owp", owp / num
    return owp / num

def calcoowp(results, teamindex):
    oowp = 0
    num = 0
    for i in range(len(results)):
        if i == teamindex:
            continue
        result = results[i]
        if result[teamindex] == '.':
            continue
        #print "oowp", result, teamindex
        oowp = oowp + calcowp(results, i)
        num = num + 1
    return oowp / num

def rpi(wp, owp, oowp):
    return 0.25*wp + 0.5*owp + 0.25*oowp

if __name__ == '__main__':
    main()
