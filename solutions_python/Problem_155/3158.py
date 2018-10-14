import sys

def main():
    with open(sys.argv[1],'r') as fp:
        a=fp.read()

    text=a.split('\n')
    num=int(text.pop(0))

    for count in range(num):
        j=text[count].split()
        print 'Case #%d: %d'%(count+1,get_soln(j))

def get_soln(text):
    reqd=0
    total=0
    step1=text
    #print text[1]
    total+=int(step1[1][0])
    for i in range(1,int(step1[0])+1):
        if total==0 or total<i:
            reqd+=1
            total+=1
        total+=int(step1[1][i])
    return reqd

main()
