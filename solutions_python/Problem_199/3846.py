def fliperr(strx,pansize):
    flippedstrx = ''
    for i in range(pansize):
        if strx[i] == '-':
            flippedstrx = flippedstrx + '+'
        else:
            flippedstrx = flippedstrx + '-'
    return flippedstrx


def recursiveflip(strx,pansize,count):
    minus = '-'
    indexOfMinus = strx.find(minus)
    stringsize = strx.__len__()
    buff = stringsize-int(pansize)
    buff2 = int(indexOfMinus)+int(pansize)
    final = ''
    counter = count
    while indexOfMinus <= buff and indexOfMinus != -1:
        counter += 1
        subsold = strx[indexOfMinus:buff2]
        subsnew = fliperr(subsold,pansize)
        return recursiveflip(strx.replace(subsold,subsnew,1),pansize,counter)

    if strx.find('-') != -1:
        return ('IMPOSSIBLE')
    else:
        return counter

if __name__ == "__main__":
    import fileinput

    f = fileinput.input()
    """The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line """

    T = int(f.readline())
    for case in range(1, T + 1):
        S = f.readline().strip().split(' ')
        #print (S)
        solution = recursiveflip(S[0],int(S[1]),0)
        print("Case #{0}: {1}".format(case, solution))