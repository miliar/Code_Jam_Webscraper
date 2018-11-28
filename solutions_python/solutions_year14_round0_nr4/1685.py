f = open("D-large.in", "r")
#f = open("input", "r")
n = int(f.readline())
result = []
for j in range(n):
    arr1 = []
    arr2 = []
    m = int(f.readline())
    line = f.readline().split(" ")
    for i in line:
        arr1.append(float(i))
    line = f.readline().split(" ")
    for i in line:
        arr2.append(float(i))
    ans1 = 0
    ans2 = 0
    if m == 1:
        if arr1[0] > arr2[0]:
            ans1 += 1
            ans2 += 1
    else:
        arr1 = sorted(arr1)
        #print j, arr1
        arr2 = sorted(arr2)
        #print j, arr2
        visited = [False]*m
        tag = 0
        for i in arr1:
            for index, value in enumerate(arr2):
                if i < value  and visited[index]==False:
                    tag += 1
                    visited[-tag] = True
                    break
                elif i > value and visited[index]==False:
                    ans1 += 1
                    visited[index] = True
                    break
        visited = [False]*m
        for i in arr1:
            for index, value in enumerate(arr2):
                if visited[index]==False and i < value:
                    visited[index] = True
                    break
        for i in visited:
            if i == False:
                ans2 += 1
    result.append((ans1, ans2))
f.close()

f = open("output", "w")
for index, value in enumerate(result):
    f.write("Case #"+str(index+1)+": "+str(value[0])+" "+str(value[1])+"\n")
f.close()
