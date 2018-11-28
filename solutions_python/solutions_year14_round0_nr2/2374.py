# Google Codejam - Cookie Clicker Alpha

def ShouldInvest(C, F, X, Gradient):
    return Gradient < (F * (X - C) / C) # mathematics ;P

def MinimumTime(C, F, X):
    Gradient = 2
    Time = 0
    # start
    while 1:
        if ShouldInvest(C, F, X, Gradient):
            Time += C / Gradient # time till we reach C cookies
            Gradient += F # we create a new farm
        else: # we do not invest anymore
            Time += X / Gradient # wait till we reach X cookies
            return Time
    return -1 # if the interpreter arrives here, something went wrong

def main():
    try:
        f = open('cookie.in','r')
    except:
        print('cannot open input file!')
    T = int(f.readline())
    for t in range(1, T + 1):
        print('Case #', t, ': ', end='', sep='')
        Line = f.readline()
        Line = Line.split(' ')
        C = float(Line[0])
        F = float(Line[1])
        X = float(Line[2])
        print('{0:.7f}'.format(MinimumTime(C, F, X)))
    f.close()
    return 0

if __name__=='__main__':
    main()
