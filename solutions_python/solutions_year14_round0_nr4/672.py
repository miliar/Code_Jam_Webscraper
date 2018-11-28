import fileinput
import copy

def getScore(list1, list2):
    list1.sort(reverse=True)
    list2.sort(reverse=True)
    score = 0
    num=0
    while (len(list1)!=0):
        num = list1.pop()
        comp = list2.pop()
        if num > comp:
            score +=1
        else:
            while num < comp and len(list1)!=0:
                num = list1.pop()
            if num>comp:
                score +=1
    return score

i=0
n=0
l=0
for line in fileinput.input():
    if i==0:
        n=int(line)
        i+=1
        continue
    if i%3 ==1:
        l = int(line)
        i+=1
        continue
    if i%3 == 2:
        list1 = [float(j) for j in line.split()]
        i+=1
        continue
    if i%3 == 0:
        list2 = [float(j) for j in line.split()]
        i+=1
        list1copy = list1.copy()
        list2copy = list2.copy()
        ans1 = getScore(list1,list2)
        ans2 = l-getScore(list2copy,list1copy)
        print("Case #" + str(i // 3) + ": " + str(ans1) + " " + str(ans2))




