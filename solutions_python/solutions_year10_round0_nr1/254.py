'''
Created on 2010/05/08

@author: banana
'''

if __name__ == '__main__':
    pass

fp = open("A-small-attempt0.in", "r")

lines = fp.readlines()

T = int(lines[0])

fpout = open("A-sample.txt", "w")

for t in range(1, T+1):
    N = int(lines[t].split()[0])
    K = int(lines[t].split()[1])
    
    states = [0 for x in range(N)]
    # 1 : turned on
    # 0 : turned off
    
    power_idx = 0
    
    for i in range(K):
        for j in range(0, min(power_idx + 1, N)):
            states[j] = 1 - states[j]
        
        power_idx = 0
        while power_idx < N and states[power_idx] == 1:
            power_idx = power_idx + 1
    
        #print i, power_idx, states
        
    fpout.write("Case #%d: "%(t))    
    if power_idx == N:
        fpout.write("ON\n")
    else:
        fpout.write("OFF\n")
        
        
fpout.close()