
import sys, math

def print_case(fo, text):
    print text
    if fo!=None:
        fo.write(text + '\n')

def triplet_score(n):
    av = float(n)/3.0
    
    if av-math.floor(av)==0.0:
        return [0, int(av),int(av),int(av)]
    elif av-math.floor(av)<0.5:
        return [1, int(av)+1,int(av),int(av)]
    else:
        return [2, int(av)+1,int(av)+1,int(av)]
        
if __name__ == '__main__':
    if len(sys.argv) >= 2:
        tx = open(sys.argv[1], 'r').read()
        fw = open(sys.argv[2], 'w')
    else:
        tx = open('b_test.txt','r').read()
        fw = None
        
    lines = tx.split('\n')
    numofcases = int(lines[0])
    cases = []
    for i in range(numofcases):
        params = [int(m) for m in lines[i+1].split()]
        c = {}
        c['n'] = params[0]
        c['s'] = params[1]
        c['p'] = params[2]
        lst = params[3:]
        lst.sort()
        c['g'] = lst
        cases.append(c)
        #print c 
        
    for i,case in enumerate(cases):
        n   = case['n']
        s   = case['s']
        p   = case['p']
        lst = case['g']
        result = 0
        
        score_lst = []
        for j in range(n):
            scores = triplet_score(lst[j])
            if scores[1]>=p:
                result += 1
                scores[0]=3
            score_lst.append(scores) 
        #print score_lst, result, s, p
        
        for j in range(s):
            for k in score_lst:
                if k[0]==2 and k[1]+1==p and k[2]>0:
                    result += 1
                    k[0]=3
                    break
                elif k[0]==0 and k[1]+1==p and k[3]>0:
                    result += 1
                    k[0]=3
                    break
        #print score_lst
        print_case(fw,'Case #%d: %d'%(i+1,result))
        
    if fw!=None:    
        fw.close()
