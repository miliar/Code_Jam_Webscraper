#encoding=utf-8

def pd(text, word):
    line = [0] + (len(text)) * [1]
    for indexw in xrange(len(word)):
        indexl = 1
        for indext in xrange(len(text)):
            if word[indexw] == text[indext]:
                line[indexl] = line[indexl] + line[indexl-1]
            else:
                line[indexl] = line[indexl-1]
            indexl += 1
    return line[-1]
    
if __name__ == '__main__':
    
    N = input()
    word='welcome to code jam'

    for case in range(1,N+1):
        text = raw_input()
        print 'Case #%d: %04d' % (case, pd(text, word) % 10000)