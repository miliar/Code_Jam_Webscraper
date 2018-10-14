#! /usr/bin python

def rate(farm, numfarms=0):
    return 2 + farm * numfarms

def tempo_farm(farm, cost, n):
    time = 0

    while n>=1:
        time += cost/rate(farm,n-1)
        n -= 1
    ##print time

    return time

def tempo_vitoria(X, farm, n):
    return X/rate(farm, n)

def main():
    with open("input.txt", "r") as inputfile:
        inputfile = inputfile.readlines()

        ###print inputfile

        numberofcases = int(inputfile[0])
        case = 1

        while case <= numberofcases:
            C, F, X = map(float, inputfile[case].strip().split())
            #print "Conditions"
            #print C, F, X

            n = 0

            while(True):
                tempof = tempo_farm(F, C, n)
                tempov = tempo_vitoria(X, F, n)

                tempototal = tempof + tempov

                next_r = rate(F, n+1)
                ##print "rate+1",
                ##print next_r
                next_tempof = tempo_farm(F, C, n+1)
                ##print "tempof+1",
                ##print next_tempof
                next_tempov = tempo_vitoria(X, F, n+1) 
                ##print "tempov+1",
                ##print next_tempov

                next_tempototal = next_tempof + next_tempov

                ##print tempototal, next_tempototal

                #raw_input()

                if next_tempototal > tempototal:
                    with open("outputb.txt", "a") as outfile:
                        outfile.write("Case #{}: {}\n".format(case, tempototal))
                    break


               
                n += 1




            case +=1

if __name__ == '__main__':
    main()