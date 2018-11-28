f = open('A-small-attempt5.in')
lines = f.readline()
inputlist = f.readlines()
linewords =[]
TranslatedWord = ''
TranslatedWords = []
TranslatedSentence = ''
outputlist=[]


tongues = {}
tongues['a']='y'
tongues['b']='h'
tongues['c']='e'
tongues['d']='s'
tongues['e']='o'
tongues['f']='c'
tongues['g']='v'
tongues['h']='x'
tongues['i']='d'
tongues['j']='u'
tongues['k']='i'
tongues['l']='g'
tongues['m']='l'
tongues['n']='b'
tongues['o']='k'
tongues['p']='r'
tongues['q']='z'
tongues['r']='t'
tongues['s']='n'
tongues['t']='w'
tongues['u']='j'
tongues['v']='p'
tongues['w']='f'
tongues['x']='m'
tongues['y']='a'
tongues['z']='q'


for i in inputlist:
    linewords =  i.split( )
    #print linewords
    for j in linewords:
        for letters in j:
            TranslatedWord = TranslatedWord + tongues[letters]
        TranslatedWords.append(TranslatedWord)
        TranslatedWord = ''
    #print TranslatedWords
    for word in TranslatedWords:
        TranslatedSentence = TranslatedSentence + ' ' + word
    x = len(outputlist)
    outputlist.append('Case #' + str(x+1) + ':' + TranslatedSentence + '\n') 
    #print TranslatedSentence
    TranslatedSentence = ''
    TranslatedWords=[]
#Now lets print results
results = open('output.txt', 'w')
results.writelines(outputlist)
for outputSentence in outputlist:
    print outputSentence
results.close()

