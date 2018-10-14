import os, sys
from operator import itemgetter, attrgetter

def time_for_ammount(production, ammount):
    pass

try:
    file = sys.argv[1]
except Exception as inst:
    print inst, '\n\nSyota avattava tiedosto parametrina!\n\n'
finally:
    file = sys.argv[1]
    fin = open(file, 'r')
    fout = open(file[:-2]+'out', 'w')
    cases = fin.readline()
    print 'Tapauksia ' + cases
    
    for case in range(0, int(cases)):
    #for case in range(0, 3):
        print ("\nCase " + str(case))
        lines = []
        lines.extend(fin.readline()[:-1].split(" "))
        #print lines
        #print float(lines[0]), float(lines[1])

        production = 2.0
        farm_price = float(lines[0])
        farm_prod = float(lines[1])
        wictory = float(lines[2])

        current_time = wictory/production
        next_time = 0
        time_passed = 0

        not_found = 10
        while not_found:
            #print production, current_time

            time_to_farm = farm_price/production
            production += farm_prod
            next_time = time_passed + time_to_farm + wictory/production

            #print production, current_time, next_time

            if current_time < next_time:
                not_found = False
            else:
                current_time = next_time
                time_passed += time_to_farm
                #not_found -= 1


        print ('Case #'+str(case+1)+': '+ str(current_time) + '\n')
        fout.write('Case #'+str(case+1)+': '+ str(current_time) + '\n')
        
        '''
        if len(lines)-1 == len(set(lines)):
            lines.sort()
            number = -1
            for x in xrange(0, len(lines)-1):
                if lines[x] == lines[x+1]:
                    #print (lines[x])
                    number = lines[x]
                    break
            print ('Case #'+str(case+1)+': '+ str(number) + '\n')
            fout.write('Case #'+str(case+1)+': '+ str(number) + '\n')
        elif len(lines) == len(set(lines)):
            print ('Case #'+str(case+1)+': Volunteer cheated!\n')
            fout.write('Case #'+str(case+1)+': Volunteer cheated!\n')
        else:
            print ('Case #'+str(case+1)+': Bad magician!\n')
            fout.write('Case #'+str(case+1)+': Bad magician!\n')
        '''

        
    fin.close()
    fout.close()
