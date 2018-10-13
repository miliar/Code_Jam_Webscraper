import sys

f = open('D:\Users\john\My Documents\Google Code Jam 2014\cookie_small.txt','r+')
g = open('D:\Users\john\My Documents\Google Code Jam 2014\cookie_small_answer.txt','w+')

test_cases = int(f.readline())

for t in range(test_cases):
    cookie_per_sec = 2
    cookie_total = 0
    min_time = 0
    
    C, F, X = f.readline().split()
    C, F, X = float(C), float(F), float(X)
    
    print('Case '+str(t+1))
    while True:
        if X - cookie_total < C:
            #print('\t'+str(cookie_total)+' '+str(cookie_per_sec)+' '+str((X - cookie_total) / cookie_per_sec)+'\tbefore factory')
            min_time += (X - cookie_total) / cookie_per_sec
            g.write('Case #'+str(t+1)+': '+'%.7f\n' % min_time)
            break
            
        #Factory Buy Time
        time_to_buy = C / cookie_per_sec
        cookie_total += C
        min_time += time_to_buy
        
        no_buy_time_estimate = (X - cookie_total) / cookie_per_sec
        buy_time_estimate = (X - (cookie_total - C)) / (cookie_per_sec + F)
        
        if buy_time_estimate < no_buy_time_estimate:
            #Buy Farm
            cookie_total -= C
            cookie_per_sec += F
            #print('\t'+str(cookie_total)+' '+str(cookie_per_sec)+' '+str(time_to_buy)+'\tbuy factory')
        else:
            cookie_total += no_buy_time_estimate * cookie_per_sec
            min_time += no_buy_time_estimate
            #print('\t'+str(cookie_total)+' '+str(cookie_per_sec)+' '+str(no_buy_time_estimate)+'\tno buy factory')
            
        if cookie_total >= X:
            g.write('Case #'+str(t+1)+': '+'%.7f\n' % min_time)
            break
    #print

f.close()
g.close()