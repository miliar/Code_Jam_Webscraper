#!/usr/bin/python

caseNR=0


def main():
#    global N_engines, caseNR, engines, values
    global caseNR
#    engines = {}
#    values  = []
    
    test_cases = input()
       
    for caseNR in range(test_cases):
        calc()
            
def calc():
    global caseNR, caseNR
    
    engines = {};
    N_engines  = input()
    for i in range(N_engines):
        engines[raw_input()] = i
    
    queries = input()
    
    best = 0
    calcbest = 9999;
    values = [0 for i in range(N_engines)]
    
    for n in range(queries):
        calcbest = 9999;
        e = engines[raw_input()]
        for i in range(N_engines):
            if e==i:
                values[i] = -1;
            else:
                if values[i]==-1:
                    values[i]=best+1;
                if values[i]<calcbest:
                    calcbest = values[i]
        best = calcbest
    
    print "Case #" + str(caseNR+1) + ": " + str(best);
#    print "engines: " + str(values);

if __name__ == '__main__':
    main()
