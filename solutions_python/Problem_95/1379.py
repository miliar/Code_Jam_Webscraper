
def complete_lang(lang, input, output):
    for i in range(0,len(input)):
        lang[input[i]] = output[i]
        
def learn(lang):
    input_1 = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
    output_1 = 'our language is impossible to understand'
    
    input_2 = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
    output_2 = 'there are twenty six factorial possibilities'
    
    input_3 = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'
    output_3 = 'so it is okay if you want to just give up'
    
    complete_lang(lang, input_1, output_1)
    complete_lang(lang, input_2, output_2)
    complete_lang(lang, input_3, output_3)
    complete_lang(lang, input_3, output_3)
    complete_lang(lang, 'z', 'q')
    complete_lang(lang, 'q', 'z')

def getTestCases():    
    test = []
    #test.append('ejp mysljylc kd kxveddknmc re jsicpdrysi')
    #test.append('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd')
    #test.append('de kr kd eoya kw aej tysr re ujdr lkgc jv')    
    f = open("A-small-attempt0.in", "r")
    n_line = 0
    n = 0
    while True:
      linea = f.readline()        
      if not linea: break
      if n_line != 0:          
          test.append(linea.strip())
      else:
          n = linea.strip()        
      n_line = n_line + 1        
    f.close()
    return test, n

def solve(language, tests):
    result = []
    i = 1
    for e in tests:        
        solution = ''
        for c in e:            
            solution = solution +  language[c]            
        #result.append(solution)
        print 'Case #'+str(i)+': ' +  solution
        i = i + 1   
    return result
    
language = {}
learn(language)
tests, n = getTestCases()
solution= solve(language,tests)

    





    