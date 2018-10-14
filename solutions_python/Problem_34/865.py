
def get_int():
    return int(get_word())

def get_word():
    if not 'words' in dir(get_word):
        get_word.words=[]
    while len(get_word.words)==0:
        get_word.words=raw_input().split()
    return get_word.words.pop(0)
    
import re

def regularize(word):
    regexp = ''
    par = False
    pap = ''
    for c in word:
        if c=='(':
            par = True
        elif c==')':
            par = False
            regexp += '('+'|'.join(pap)+')'
            pap=''
        else:
            if par:
                pap+=c
            else:
                regexp+=c
    return regexp

def main():
    L = get_int()
    D = get_int()
    N = get_int()
    
    words = []
    
    for i in range(1,D+1):
        words.append(get_word())
    
    for i in range(1,N+1):
        test = get_word()
        reg = re.compile(regularize(test))
        n = len(filter(reg.match, words))
        print "Case #%d: %d"%(i,n)
    
if __name__ == '__main__':
    main()
