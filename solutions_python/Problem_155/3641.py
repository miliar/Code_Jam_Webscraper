'''
Created on 24 Mar 2015

@author: dev
'''


from AudienceStandingSolver import AudienceStandingSolver


solver = AudienceStandingSolver()
f = open('output.txt','w')

with open('A-small-attempt2.in') as file:
    lines = file.readlines()
    for i in range(1, len(lines)):
        S = lines[i].split()[1]
        print("Case #" + str(i) + ": " + solver.solve(S), file = f)
        
    
