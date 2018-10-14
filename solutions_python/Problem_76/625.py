'''
Created on 07.05.2011

@author: ikari
'''

filename = "input.txt"
f = open(filename, "r")

T = int(f.readline())

for i in range(0, T):
    candies = []
    taken = []
    
    def search(index):
        if index == len(candies):
            sean = 0
            patrick = 0
            sum = 0
            sean_get = False
            pat_get = False
            for i in range(0, index):
                if taken[i]:
                    sean ^= candies[i]
                    sum += candies[i]
                    sean_get = True
                else:
                    patrick ^= candies[i]
                    pat_get = True
            if sean == patrick and sean_get and pat_get:
                return sum
        else:
            taken[index] = False
            l = search(index + 1)
            taken[index] = True
            r = search(index + 1)
            return max(l, r)
        return -1
    
    n = int(f.readline())
    ss = f.readline().split()
    
    for s in ss:
        candies.append(int(s))
        taken.append(False)
    
    aaa = search(0)
    
    answ = 'Case #' + str(i + 1) + ': '
    
    if aaa == -1:
        print answ + 'NO'
    else:
        print answ + str(aaa)
    
    