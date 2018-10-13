mulmatrix = [['-1','k','-j'],['-k','-1','i'],['j','-i','-1'],['i','j','k'],
             ['1','-k','j'],['k','1','-i'],['-j','i','1'],['-i','-j','-k']]
mapping = {'i':0,'j':1,'k':2,'1':3,'-i':4,'-j':5,'-k':6,'-1':7}
def mul(a,b):
    return mulmatrix[mapping[a]][mapping[b]]

def main():
    f = open("/home/ayush/random.txt","r+")
    y = f.readlines()
    t = int(y[0])
    x = 1
    w = 1
    while x<=t:
        l,n = map(int,y[w].split())
        s = y[w+1]
        w+=2
        flag = 0
        result = '1'
        for i in xrange(n):
            for j in xrange(l):
                result = mul(result,s[j])
                if flag == 0 and result == 'i':
                    flag+=1
                    result='1'
                elif flag == 1 and result == 'j':
                    flag+=1
                    result='1'
                elif flag == 2 and result == 'k':
                    flag+=1
                    result='1'
        if flag == 3 and result == '1':
            print 'Case #'+`x`+': YES'
        else:
            print 'Case #'+`x`+': NO'
        x+=1
main()
