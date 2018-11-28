from sys import stdin


def replace(chaine,index,element):
    a=chaine[:index]+element+chaine[index+1:]
    return a




def answer(chaine):
    c = chaine.split()
    row = c[0]
    K = int(c[1])
    i=0
    N = len(row)
    cpt = 0
    a = row[:]
    while True:
        #on cherche le premier - a partir de i
        while i< N and a[i]=='+':
            i+=1
        if i==N:
            return str(cpt)
        elif N-i<K:
            return 'IMPOSSIBLE'
        else:
            for j in range(K):
                if a[i+j]=='+':
                    a = replace(a,i+j,'-')  
                else:
                    a = replace(a,i+j,'+')
            cpt += 1
     


T=int(stdin.readline())
for case in range(1,T+1):
	c=stdin.readline()
	print('Case #%i: %s' % (case,answer(c)))

