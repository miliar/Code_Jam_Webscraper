from multiprocessing import Pool
import os
import math


def solvePuzzle(dsize, files):
    files.sort()

    disks=0
    while len(files):
        disks+=1
        small = files[0]
        files.remove(small)
        if len(files)>0:
            for big in reversed(files):
                if big+small<=dsize:
                    files.remove(big)
                    break
    return str(disks)

input_text = open("input.in")
lines = input_text.readlines()
input_text.close()
currentLine=1
with open("output", "a") as outputfile:
    pool = Pool(processes=6)
    results = {}
    for num in range(0,int(lines[0])):
        dsize=int(lines[num*2+1].split(" ")[1])
        files=[int(x) for x in lines[num*2+2].split(" ")]
        results[num]= pool.apply_async(solvePuzzle, [dsize, files])
        #outputfile.write("Case #"+str(num+1)+": "+solvePuzzle(dsize, files)+"\n")
    for num in range(0,int(lines[0])):
        outputfile.write("Case #"+str(num+1)+": "+results[num].get()+"\n")
