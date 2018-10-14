import math

def run():
    T=int(input())
    test_case=1
    while test_case<=T :
        line=[float(i) for i in input().split(' ')]
        C,F,X=line[0], line[1], line[2]
        total_secs=0
        current_cookies=0
        step_factor=2
        #print(C,F,X)
        while 1==1:
            if(current_cookies >= X):
                print("Case #%d: %.7f" % (test_case, total_secs))
                break
            secsWithCurrentSpeed=X/step_factor
            secsWithIncSpeed=(X/(step_factor+F)) + (C/step_factor)
            #print(secsWithCurrentSpeed,secsWithIncSpeed)
            if(secsWithCurrentSpeed > secsWithIncSpeed):
                # buy farm
                total_secs+=C/step_factor
                #print('buying farm total_secs so far: %f' % total_secs)
                current_cookies=0
                step_factor+=F
            else:
                # continue with current speed
                #print('continuing with current speed')
                total_secs+=secsWithCurrentSpeed
                current_cookies+=step_factor*total_secs
            #print("cur cookies %f " % current_cookies)
        test_case+=1

if __name__ == "__main__":
    run()
