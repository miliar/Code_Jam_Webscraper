'''
Created on Apr 8, 2017

@author: tortor
'''

def solve(S, K):
    
    if not "-" in S:
        return 0
    
    l = len(S)
    count = 0
    for i in range(l-K+1):
        if S[i] == "+":
            continue
        
        #not happy flip K pancakes
        S = S[:i]+flip(S[i:i+K])+S[i+K:]
        count += 1
        
        #print(S)
    
    if "-" in S:
        return "IMPOSSIBLE"
    
    return count

def flip(S):
    temp = [];
    for c in S:
        if c == "+":
            temp.append("-")
        else:
            temp.append("+")
            
    return "".join(temp)

def main(filename):
    with open(filename+".in") as fin:
        with open(filename+".out", "w") as fout:
            T = int(fin.readline().strip())
            
            for i in range(T):
                S, K = fin.readline().split()
                result = solve(S, int(K))
                #print("result=",result)
                fout.write("Case #{:d}: {}\n".format(i+1,result))

if __name__ == '__main__':
    main("A-large")