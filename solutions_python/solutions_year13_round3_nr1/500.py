
def map_cons(name,n):
    l=[]
    voc = {"a","e","i","o","u"}
    for i in range(len(name)-n+1):
        if not set(name[i:i+n]).intersection(voc):
            l.append(i)
    return l
def triangle(n):
    return n*(n+1)//2
def main():
    fout = open('consonants.out','w')
    with open("consonants.in",'r') as fin:
        test_cases = int(fin.readline().strip())
        for i in range(test_cases):
            buff = fin.readline().split()
            name = buff[0]
            n = int(buff[1])
            cons_map = map_cons(name,n)
          
            res = 0
            for q in range(0,len(name)-n+1):
                for j in range(q+n-1,len(name)):
                    ok = 0
                   
                    for k in cons_map:
                        if q<=k and j>= k+n-1:

                            ok=1
                            break
                    if ok:
                        res += 1
            fout.write("Case #{}: {}\n".format(i+1,res))
              
         
                            
                    
            



if __name__== '__main__':
    main()
