'''    
Created on Apr 8, 2017

@author: tortor
'''
def solve(N):
    
    if len(N) == 1:
        return N
    
    l = len(N)
    idx = -1
    
    for i in range(l-1):
        if int(N[i]) > int(N[i+1]):
            idx = i+1
            break
    
    if idx == -1:
        return N
    
    #not Tidy
    temp = []
    for j in range(idx-1,-1,-1):
        curr = int(N[j])-1
        if j != 0:
            #compare to next one
            next = int(N[j-1])
            if next > curr:
                temp.insert(0,"9")
            else:
                temp.insert(0,str(curr))
                temp.insert(0,N[:j])
                break
        else:
            temp.insert(0,str(curr))
    
    temp += ["9"]*(l-idx)
    
    #print("idx=",idx)
    #print("temp=",temp)
    
    result = int("".join(temp))
    
    if result > int(N):
        print("ERROR!! N={}, Result={}".format(N,Result))
    
    return result

def main(filename):
    with open(filename+".in") as fin:
        with open(filename+".out", "w") as fout:
            T = int(fin.readline().strip())
            
            for i in range(T):
                N = fin.readline().strip()
                result = solve(N)
                #print("result=",result)
                fout.write("Case #{:d}: {}\n".format(i+1,result))

if __name__ == '__main__':
    main("B-large")