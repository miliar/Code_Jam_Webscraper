import sys

inputFileName="input.in"
outputFileName="output.out"

fi=open(inputFileName,"r")
fo=open(outputFileName,"w")

T=int(fi.readline())

def compute(pancakes,flipper):
    pancakes=map(lambda pancake:True if pancake=="+" else False,pancakes)
    flipper=int(flipper)
    flips=0
    for i in range(len(pancakes)-flipper+1):
        if(not pancakes[i]):
            flips+=1
            for j in range(i,i+flipper):
                pancakes[j]=not pancakes[j]
    if(sum(pancakes)==len(pancakes)):
        return str(flips)
    return "IMPOSSIBLE"

map(lambda i:fo.write("Case #"+str(i+1)+": "+compute(*fi.readline().strip().split(" "))+"\n"),range(T))
