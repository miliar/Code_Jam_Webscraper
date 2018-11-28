'''
Created on 12 Apr 2014

@author: Nigel.Fernandez
'''

#import time

def main():
    #start = time.time()
    
    fread = open('B-large.in', 'r')
    fwrite = open('B_cookie_clicker_alpha_output_large_nigel_fernandez.dat', 'w')
    c_num = int(fread.readline())
    
    for i in range(c_num):
        info = fread.readline().split()
        if(i != c_num - 1):
            fwrite.write('Case #' + str(i + 1) + ': {:.7f}'.format(find_time(info)) + '\n')
        else:
            fwrite.write('Case #' + str(i + 1) + ': {:.7f}'.format(find_time(info)))
    
    fread.close()
    fwrite.close()
    #stop = time.time()
    #print "Time " + str(stop - start) + " s"


def find_time(info):
    rate = 2.0
    current_time = 0.0
    
    while(1):
        C = float(info[0])
        F = float(info[1])
        X = float(info[2])
        time_without_farm = X / rate
        time_with_farm = (C / rate) + (X / (rate + F))
    
        if(time_without_farm < time_with_farm):
            break
        else:
            current_time += C / rate
            rate += F

    return round(current_time + time_without_farm, 7)
        

if __name__ == '__main__':
    main()