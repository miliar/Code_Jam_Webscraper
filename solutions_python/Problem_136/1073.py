t = input()
for i in range(t):
        c,f,x = map(float,raw_input().split())
        current_time = 0.0
        current_rate = 2.0
        while (True):
                if x/current_rate <= (x/(current_rate+f) + c/current_rate):
                        current_time = current_time + x/current_rate
                        break
                else:
                        current_time = current_time + c/current_rate
                        current_rate = current_rate+f
        print 'Case #'+str(i+1)+': '+str(current_time)

