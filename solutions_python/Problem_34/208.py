def main(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    outlines = []
    
    L, D, N = map(lambda x:int(x), lines.pop(0).split(' '))
    
    words = []
    for word in xrange(D):
        words.append(lines.pop(0)[:-1])
    
    num_chars = len(words[0])
    
    for case in xrange(N):
        input = lines.pop(0)[:-1]
        charset = []
        
        temp_chars = ''
        i = 0
        while i < len(input):
            temp_chars = input[i]
            
            if temp_chars == '(':
                temp_chars = ''
                i += 1
                while input[i] != ')':
                    temp_chars += input[i]
                    i += 1
        
            charset.append(temp_chars)
            i += 1
        
        valid_words = list(words)
        for i in xrange(len(charset)):
            valid_words = filter(lambda word: word[i] in charset[i], valid_words)
        
        line = 'Case #%i: %i\n' % ((case + 1), len(valid_words))
        outlines.append(line)
    
    f = open('A.out', 'w')
    f.writelines(outlines)
    f.close()

if __name__ == "__main__":
    main('A-large.in')