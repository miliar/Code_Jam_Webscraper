import fileinput

i=0
n=0
target = 0
targetList = list()

for line in fileinput.input():
    if i==0:
        i+=1
        n=int(line)
        continue
    if i%5==1:
        target = i+int(line)
    if i==target:
        targetList.append([int(j) for j in line.split()])
    i+=1

test1 = list()
test2 = list()

def check(list1,list2):
    n = 0
    n2 =0
    for k1 in list1:
        for k2 in list2:
            if k2==k1:
                n+=1
                n2=k2
    return [n,n2]

for i in range(n):
    test1 = targetList[2*i]
    test2 = targetList[2*i+1]
    result = check(test1,test2)
    if result[0] ==1:
        print("Case #" + str(i+1) + ": " + str(result[1]))
    elif result[0]==0:
        print("Case #" + str(i+1) + ": " + "Volunteer cheated!")
    else:
        print("Case #" + str(i+1) + ": " + "Bad magician!")

