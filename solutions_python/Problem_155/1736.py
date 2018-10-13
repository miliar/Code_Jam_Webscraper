'''
Created on Apr 11, 2015

@author: mostasem
'''

def get_min_friends(aud,max_shy):
    extra = 0
    for i in range(len(aud)):
        sum_before = sum(aud[:i])
        if(i > sum_before):
            diff = abs(i - sum_before)
            aud[i - 1] +=diff
            extra += diff
    return extra
    





f_r = open('A-large.in',"r")
n_test=int(f_r.readline().strip()) 
f_w = open("A.out", "w")
result = ""
for i in range(n_test):
    S,St = f_r.readline().strip().split()
    aud = map(int,St)
    result = get_min_friends(aud, S)
    print result
    output_str='Case #{itr}: {res}'.format(itr=(i+1),res=result)
    f_w.write(output_str+'\n')
    
f_r.close()


