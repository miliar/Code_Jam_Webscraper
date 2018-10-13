#Python 3.3

#2 arrangements
arr1=[]
arr2=[]
t = []

n = int(input())

for i in range(1, n+1):
    r1 = int(input());
    #get the row and store in arr1
    for j in range (1, 5):
        if j == r1:
            #get the input
            arr1 = [int(x) for x in input().split()]
        else:
            t = list(input())

    r2 = int(input())
    for j in range (1, 5):
         if j == r2:
            arr2 = [int(x) for x in input().split()]

         else:
            t = list(input())

    
    #process the two finding common element(s)
    count = 0
    for number in arr1:
        if number in arr2:
            common = number
            count+=1

    #print("Count is {}".format(count))
    #print(arr1)
    #print(arr2)

    if count == 1:
        print("Case #{}: {}".format(i, common))
    elif count > 1:
        print("Case #{}: Bad Magician!".format(i))
    elif count < 1:
        print("Case #{}: Volunteer cheated!".format(i))

