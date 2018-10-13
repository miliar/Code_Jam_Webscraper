def codejam():
    n_tests = int(raw_input())
    for n_test in range(n_tests):
        interval = raw_input().split(' ')
        start = int(interval[0])
        end = int(interval[1])
        quantity=0
        for i in range(start,end+1):
            if i==1 or i==4 or i==9 or i==121 or i==484:
                quantity+=1
        
        print('Case #'+str(n_test+1)+': '+str(quantity))

codejam()
