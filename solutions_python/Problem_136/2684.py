#!/usr/bin/env python3

import sys
from numpy import *

input_file = open(sys.argv[1], 'r')
output_file = open("out_" + sys.argv[0].rstrip(".py"), 'w')

input_size = int(input_file.readline().rstrip("\n"))



    


estimatedTime = 0
nextEstimatedTime = 0

for i in range(input_size):
    output_file.write("Case #" + str(i + 1) + ": ")
    # C : Prix d'une ferme à cookie
    # F : Production d'une ferme à cookie
    # X : Nombre de cookies à atteindre
    (C, F, X) = map(float, input_file.readline().rstrip("\n").split())

    cookies = 0 
    cookiesProduction = 2
    estimatedTime = X / cookiesProduction
    time = 0
    while (cookies < X):
        farmBuildTime = C / cookiesProduction
        nextEstimatedTime = time + farmBuildTime + X / (cookiesProduction + F)
        if (nextEstimatedTime < estimatedTime):
            estimatedTime = nextEstimatedTime
            cookiesProduction += F
            time+= farmBuildTime
            #cookies à 0, on les a dépensé
        else:
            cookies = X
            time += X / cookiesProduction
    #print("Time : %.7f\n" % time)
    output_file.write("%.7f\n" % time)
        
    
input_file.close()
output_file.close()
