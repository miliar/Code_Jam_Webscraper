def findOut(arr1, arr2):
    match_count = 0
    number = 0
    for i in range(0,4):
        for j in range(0,4):
            if arr1[i] == arr2[j]:
                match_count+=1
                number = arr1[i]
    if match_count == 0:
        return "Volunteer cheated!"
    elif match_count == 1:
        return str(number)
    else:
        return "Bad magician!"

def run():
    t = input()
    c = 1
    while(t>0):
        t-=1
        a1 = input()
        arr1 = []
        for i in [1,2,3,4]:
            a = raw_input()
            if(i == a1):
                arr1 = map(int, a.split())
        a2 = input()
        arr2 = []
        for i in [1,2,3,4]:
            a = raw_input()
            if(i == a2):
                arr2 = map(int, a.split())
        print "Case #" + str(c) +": "+findOut(arr1, arr2)
        c+=1
run()