f = open('A-small-attempt0.in','r')

Trans = {'y':'a','e':'o','q':'z','z':'q'}

Untranslated = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'    
Translated =   'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'
for i in range(len(Untranslated)):
    Trans[Untranslated[i]] = Translated[i]

NumberOfCases = int(f.readline())
CaseNumber = 1
for i in range(NumberOfCases):
    a = f.readline()
    ans =  ''
    for letter in a:
        if letter != '\n':
            ans = ans + Trans[letter]

    value = 'Case #{}: {}'.format(CaseNumber,ans)
    CaseNumber = CaseNumber + 1
    print value
