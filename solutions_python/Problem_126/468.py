'''
Created on 2013-5-12

@author: t
'''


vowel = ['a','e','i','o','u']


def test(word,n):
    length = len(word)
    
    k = 0
    
    for i in range(length):
        for j in range(i,length):
            if check(word[i:(j+1)],n):
                k += 1
    return k
            
def check(word,n):
    
#    print word
    
    length = len(word)
    

    
    
    for i in range(length-n+1):
        
        sub = word[i:i+n]
        
        if hasvowel(sub):
            pass
        else:
            return True
    return False
        
        
        
def hasvowel(word):
    for v in vowel:
        if word.find(v)<0:
            continue
        else:
            return True
    return False
    
    
    
if __name__ == '__main__':
    inputfile = open("A-small-attempt0.in",'r')
    outputfile = open('result','w')
    num_test = int(inputfile.readline())
    for i in range(num_test):
        
        record = inputfile.readline()
        word = record.split(' ')[0]
        n = int(record.split(' ')[1])
        outputfile.write('Case #'+str(i+1)+': '+str(test(word,n))+'\n')
    
    
    
#    print test('tsetse',2)
    
    