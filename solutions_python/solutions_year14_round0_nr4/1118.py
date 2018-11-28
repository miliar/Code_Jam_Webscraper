infile = open('D:\study\codejam\codejam2014\D-large.in','r')
outfile = open('D:\study\codejam\codejam2014\D-large.out','w')
def main():
    T = int(infile.readline())
    for case in range(1,T+1):
        doCase(case)
    infile.close()
    outfile.close()

def doCase(case):
    no_of_weights = int(infile.readline())
    naomi_weights = sorted(map(float,infile.readline().split()),reverse = True)
    ken_weights = sorted(map(float,infile.readline().split()), reverse = True)
    #print(naomi_weights,ken_weights)
    #checkwin(naomi_weights,ken_weights)
    #checkdeceitwin(naomi_weights,ken_weights)
    outfile.write('Case #'+str(case)+': '+str(checkdeceitwin(naomi_weights,ken_weights))+' '+\
          str(checkwin(naomi_weights,ken_weights))+'\n')    

def checkwin(naomi_weights,ken_weights):
    naomi_weights = naomi_weights[:]
    ken_weights = ken_weights[:]
    win = 0
    while len(naomi_weights):
        if naomi_weights[0] > ken_weights[0]:
            win += 1
            naomi_weights.pop(0)
            ken_weights.pop(len(ken_weights)-1)
        else:
            naomi_weights.pop(0)
            ken_weights.pop(0)
    return win

def checkdeceitwin(naomi_weights,ken_weights):
    deceitfulwin = 0
    naomi_weights = naomi_weights[:]
    ken_weights = ken_weights[:]
    while len(naomi_weights):
        if naomi_weights[len(naomi_weights)-1] < ken_weights[len(ken_weights)-1]:
            naomi_weights.pop(len(naomi_weights)-1)
            ken_weights.pop(0)
        else:
            naomi_weights.pop(len(naomi_weights)-1)
            ken_weights.pop(len(ken_weights)-1)
            deceitfulwin += 1

    return (len(naomi_weights)+deceitfulwin)

if __name__ == '__main__':
    from copy import *
    main()
        
