# -*- coding: utf-8 -*-



def get_best_result(num,surprising=False):
    if num == 0:
        return 0
    if surprising:
        return (num+4)//3
    else:
        return (num+2)//3


with open('B-large.in') as f, open ('out.txt','w') as f_out:
    f.__next__()

    for i,line in enumerate(f,1):
        line = line.rstrip()
        values = [int(el) for el in line.split()]
        N,num_super,p,*T = values
        fit = 0
        fit_with_super = 0
        for t in T:
            if get_best_result(t)>=p:
                fit += 1
            else:
                if get_best_result(t,surprising=True)>=p:
                    fit_with_super += 1
        result = fit + min(num_super,fit_with_super)
            
        
        #print('---')
        #print(N,num_super,p,T)
        #print(result)
        f_out.write('Case #{}: {}\n'.format(i,result))

print('OK')
        



