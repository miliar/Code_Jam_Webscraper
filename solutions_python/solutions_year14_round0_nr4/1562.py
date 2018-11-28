def parse_file(input_file):
    T = int(input_file.readline().replace('\n',''))
        
    output_file = file("D-large.out", "w")
    sub = .0000001
    for tc in xrange(T):
        N = int(input_file.readline().replace('\n',''))
        Naomi = [float(x) for x in input_file.readline().replace('\n','').split(" ")]
        Ken = [float(x) for x in input_file.readline().replace('\n','').split(" ")]
        
        Naomi.sort()
        Ken.sort()
        KenT = Ken[:]
        war = 0;
        dwar = 0
        j = 0
        for i in xrange(N):
            l = len(KenT)
            if j < l:
                while j < l and KenT[j] < Naomi[i]:
                    j = j + 1                    
                if j < l:                    
                    del KenT[j]
            else:
                break
                
        war = len(KenT)

        ns = 0
        ks = 0
        ne = N-1
        ke = N-1
        while ns <= ne:
            if Naomi[ns] < Ken[ks]:
                ns = ns + 1
                ke = ke - 1
            elif Naomi[ns] > Ken[ks]:
                ns = ns + 1
                ks = ks + 1
                dwar = dwar + 1
            else:
                ns = ns + 1;
                ke = ke - 1
                
        output_file.write("Case #"+str(tc+1)+": "+ str(dwar) + " " + str(war) + "\n") 

    output_file.close()
    
if __name__ == "__main__":
    input_file = file("D-large.in")
    parse_file(input_file)
    #print isPalindrom(121)
