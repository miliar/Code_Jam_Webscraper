#! /usr/bin/env python3 -O

##########
## Adam Sorkin
## Google codejam 2012 qual b
## April 13, 2012
##########

def main():
    "compute max number"

    T = int(input()) # test cases
    for i in range(1, T+1):
        raw_data = input().split()
        data = [ int(blah) for blah in raw_data]
        number_of_googlers = data.pop(0)
        surprises = data.pop(0)
        best_score = data.pop(0)
        data.sort()
        if best_score == 0:
            answer = number_of_googlers
        elif best_score == 1:
            #print("i={0}, list={1}".format(i, data) ) ####
            if data != []:
                while data[0] == 0:
                    data.pop(0)
                    if data == []:
                        break
                answer = len(data)
            else:
                answer = 0
        else:
            answer = 0        
            for j in range(len(data)):
                if data[j] >= 3* best_score - 4 and surprises >0 :
                    answer += 1
                    surprises -= 1
                    continue
                if data[j] >= 3*best_score - 2:
                    answer += 1
        print("Case #{0}: {1}".format(i, answer) )
    return 

if __name__ == "__main__":
    main()
