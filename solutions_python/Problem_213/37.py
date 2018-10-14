import sys

fileName = "B-large"
sys.stdin = open(fileName+".in", 'r')
output = open(fileName+".out", 'w')
T = int(input())
for case in range(1,T+1):

    ###################### input data ###############################

    N,C,M = input().split(" ")
    print("N="+N+", C="+C+", M="+str(M))
    N,C,M = int(N),int(C),int(M)

    ride_demand = [0]*N
    customer_demand = [0]*C
    P,B = [],[]
    for i in range(M):
        p,b = input().split(" ")
        P.append(int(p))
        B.append(int(b))
        ride_demand[int(p)-1]+=1
        customer_demand[int(b)-1]+=1
    print(ride_demand)
    print(customer_demand)

    ######################### get min number of rides ##################################

    number_of_rides = max(customer_demand)
    for i in range(1,N+1):
        x = 1 + (sum(ride_demand[:i])-1) // i
        number_of_rides = max(number_of_rides,x)

    ######################### get min number of promtions ##################################

    number_of_promotions = 0
    for i in range(N):
        if ride_demand[i]>number_of_rides:
            number_of_promotions += (ride_demand[i]-number_of_rides)

    ######################## create output file ###############################
    answer = str(number_of_rides) + " " + str(number_of_promotions)
    print("Case #"+str(case)+": "+answer)
    print("Case #"+str(case)+": "+answer, file = output)
    ###########################################################################
