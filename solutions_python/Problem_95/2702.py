def googlerese(inputs):
    convt = {' ':' ',
             'a':'y',
             'b':'h',
             'c':'e',
             'd':'s',
             'e':'o',
             'f':'c',
             'g':'v',
             'h':'x',
             'i':'d',
             'j':'u',
             'k':'i',
             'l':'g',
             'm':'l',
             'n':'b',
             'o':'k',
             'p':'r',
             'q':'z',
             'r':'t',
             's':'n',
             't':'w',
             'u':'j',
             'v':'p',
             'w':'f',
             'x':'m',
             'y':'a',
             'z':'q' }
    inlist = inputs.split("\n")
    while inlist[len(inlist)-1] == '':
        inlist.remove('')
    if int(inlist[0]) == (len(inlist) - 1):
        i = 0
        for line in inlist[1:]:
            newline = ""
            for char in line:
                newline += convt[char]
            i += 1
            print "Case #" + str(i) + ": " + newline
    else:
        print "The number of test cases and the number of lines inputted do not match"
        
