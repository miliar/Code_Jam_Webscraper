#Coockie Clicker Aplha

BASE_COOCKIE_RATE = 2

def main(input_file,output_file='output.txt'):
    with open(input_file, 'r') as inf:
        with open(output_file, 'w') as outf:
            #outf.write('\n') #skip first line
            #inf.readline() #skipline
            T = int(inf.readline().rstrip('\n')) #number of cases
            for case in range(T): #read case input
                input_line = inf.readline().rstrip('\n').split()
                C = float(input_line[0]) #cost of coockie farm
                F = float(input_line[1]) #extra rate of coockie farm
                X = float(input_line[2]) #total cookies
                
                cookie_rate = float(BASE_COOCKIE_RATE)
                total_time = 0
                while True:
                    if X/(cookie_rate)>(X/(cookie_rate+F)+C/(cookie_rate)):
                        time_2_farm_purchase = C/(cookie_rate)
                        total_time+=time_2_farm_purchase
                        cookie_rate+=F
                        
                    else:
                        time_2_cookies_total = X/(cookie_rate)
                        total_time+=time_2_cookies_total
                        break

                outf.write('Case #%s: %.7f\n'%(case+1,total_time))
                

   
if __name__=='__main__':
    import sys
    if len(sys.argv)<3:
        main(sys.argv[1])
    else:
        main(sys.argv[1],sys.argv[2])
