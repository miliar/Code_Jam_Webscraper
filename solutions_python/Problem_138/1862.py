import sys
inp = open("final.txt","r")
out = open("output.txt","w")

def main():
     
    
    
    nCases = int(inp.readline())
    output = []
    for case in range(nCases):
        deceit_count = 0
        global deceit_count
        
        
       
        
        n = int(inp.readline())
        naomi = map(float,inp.readline().split())
        ken = map(float,inp.readline().split())
        sorted_naomi = []
        sorted_ken = []

        sort_naomi = naomi
        sort_naomi.sort()
        for i in range(n):
            sorted_naomi.append(sort_naomi[i])

        sort_ken = ken
        sort_ken.sort()
        for j in range(n):
            sorted_ken.append(sort_ken[j])

        #print sort_naomi
        #print sort_ken
        war_count = warcount(n,sort_naomi,sort_ken)
        deceitful_war_count = deceitful_war(n,sorted_naomi,sorted_ken)
        #war_count = warcount(n,sort_naomi,sort_ken)
        
        #print war_count
        #print deceitful_war_count
        #print sorted_naomi
        #print sorted_ken
       
        output.append("Case #"+str(case+1)+": "+str(deceitful_war_count)+" "+str(war_count))

    for case in range(nCases):
        #print output[case]
        out.write("{0}\n".format(output[case]))


def warcount(n,list1,list2):
    l1 = list1
    l2 = list2
    #no = n
    #while n > 0:
    sum = 0
    #for a in range(n):
        #print l1[a]
        #print l2[a]
    a = 0    
    #while a < n:
    #for a in range(n):
    '''if n ==1:
        if (l1[0] > l2[0]):
            return 1
        else:
            sum = sum + 1
    else:
        sum = sum +1'''
    if (l1[0] > l2[n-1]):
        return n
            
    elif ( n == 1 and (l1[0] <l2[0])):
        return 0
    
    else:
        i = 0
        j = 0
        while (l2[j] < l1[i]):
            j = j + 1
            
        l1.pop(i)
        l2.pop(j)
        return warcount(n-1,l1,l2)
            
    
                
deceit_count = 0
def deceitful_war(n,list1,list2):
    #print l1
    #print l2
    l1 = list1
    l2 = list2
    global deceit_count
    
    if n == 1:
        if l1[0] > l2[0]:
            
            deceit_count = deceit_count + 1
            
            
        return deceit_count
    else:
        if (l1[0] < l2[0]):
            i = 0
            while( l1[i] < l2[0]):
                i = i + 1
                if i >= n:
                     break
            for j in range(i):
                l1.pop(0)
                l2.pop(n-1-j)

            if len(l1)> 0:
                return deceitful_war(n-i,l1,l2)
            else:
                return 0
            
            
        if (l1[0] > l2[0]):
            l1.pop(0)
            l2.pop(0)
            deceit_count = deceit_count + 1
            return deceitful_war(n-1,l1,l2)
    
    

if __name__ == '__main__':
    try:
        import psyco
        psyco.full()
    except ImportError:
            pass     
    main()
    inp.close()
    out.close()
