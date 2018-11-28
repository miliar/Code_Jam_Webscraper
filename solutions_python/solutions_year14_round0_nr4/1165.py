'''
Created on 13 Apr 2014

@author: Nigel.Fernandez
'''

#import time

#python library 'bisect' used
#link to library - https://docs.python.org/2/library/bisect.html
import bisect

def main():
    #start = time.time()
    
    fread = open('D-large.in', 'r')
    fwrite = open('D_deceitful_war_output_large_nigel_fernandez.dat', 'w')
    c_num = int(fread.readline())
    
    for i in range(c_num):
        j = int(fread.readline())
        naomi_str = fread.readline().split()
        ken_str = fread.readline().split()
        if(i != c_num - 1):
            fwrite.write('Case #' + str(i + 1) + ': ' + str(d_war_points(j, naomi_str[:], ken_str[:])) + ' ' + str(war_points(j, naomi_str[:], ken_str[:])) + '\n')
        else:
            fwrite.write('Case #' + str(i + 1) + ': ' + str(d_war_points(j, naomi_str[:], ken_str[:])) + ' ' + str(war_points(j, naomi_str[:], ken_str[:])))
    
    fread.close()
    fwrite.close()
    #stop = time.time()
    #print "Time " + str(stop - start) + " s"


def d_war_points(j, naomi_str, ken_str):
    points = 0
    naomi = [float(x) for x in naomi_str]
    ken = [float(x) for x in ken_str]
    naomi.sort()
    ken.sort()
    
    for _ in range(j):
        if(float(naomi[0]) < float(ken[0])):
            ken.pop()
            del naomi[0]
        else:
            del naomi[0]
            del ken[0]
            points += 1
            
    return points


def war_points(j, naomi_str, ken_str):
    points = 0
    naomi = [float(x) for x in naomi_str]
    ken = [float(x) for x in ken_str]
    naomi.sort()
    ken.sort()
    
    for _ in range(j):
        if(float(naomi[0]) > float(ken[-1])):
            del naomi[0]
            del ken[0]
            points += 1
        else:
            index = bisect.bisect(ken, naomi.pop(0))
            del ken[index]
            
    return points    


if __name__ == '__main__':
    main()