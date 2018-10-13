import sys
from itertools import permutations
test_cases = open(sys.argv[1], 'r').readlines()
test_cases = map(lambda s: s.strip(), test_cases)
while '' in test_cases:
    test_cases.remove('')
lis=[]
i=1
for test in test_cases[1:]:
    a=test.split()
    shy={}
    for maxs,inp in zip(range(int(a[0])+1),a[1]):
        shy[maxs]=int(inp)
        
    def sequence_check(shy):
	    claps=0
	    i=0
	    for key in shy:
		    if i==0:
		        claps=shy[key]
		        i=1
		    else:
			    if claps>=key:
				    claps=claps+shy[key]
			    else:
				    return key,shy[key]
            
    def correct(ans):
        if sequence_check(shy) is not None:
            prevkey=shy.keys().index(sequence_check(shy)[0])-1   
            prevval=shy.get(prevkey)
            def add(prevkey,num,shy,ans):
	                update=shy
	                shy[prevkey]=shy[prevkey]+num
	                ans=ans+num
	                return update,ans
            ans=add(prevkey,1,shy,ans)[1]
            lis.append(ans)
            correct(ans)
    correct(0)
    if lis!=[]:
        print "Case"+" "+"#"+str(i)+":"+" "+str(lis[-1])
        lis=[]
    else:
        print "Case"+" "+"#"+str(i)+":"+" "+str(0)
    i=i+1