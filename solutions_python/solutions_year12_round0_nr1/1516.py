
import sys

def print_case(fo, text):
    print text
    if fo!=None:
        fo.write(text + '\n')


if __name__ == '__main__':
    gl = 'y n f i c w l b k u o m x s e v z p d r j g a t h a q set k oset xa ynfd'
    tl = 'a b c d e f g h i j k l m n o p q r s t u v y w x y z now i enow my abcs'
    
    translation = {}
    for i,j in zip(gl,tl):
        if not(i in translation.keys()):
            translation[i] = j
    
    if len(sys.argv) >= 2:
        tx = open(sys.argv[1], 'r').read()
        fw = open(sys.argv[2], 'w')
    else:
        tx = open('a_test.txt','r').read()
        fw = None
        
    lines = tx.split('\n')
    numofcases = int(lines[0])
    cases = []
    
    for i in range(numofcases):
        c = {}
        c['tx'] = lines[i+1]
        cases.append(c)
        
    for i,case in enumerate(cases):
        result = ''
        for c in case['tx']:
            result = result + translation[c]
        print_case(fw,'Case #%d: %s'%(i+1,result))
        
    if fw!=None:    
        fw.close()
