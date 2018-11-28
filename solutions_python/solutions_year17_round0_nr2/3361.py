n = int(input())

for i in range(0,n):
    num = int(input())
    for j in range(num,-1,-1):
        s = str(j)
        tidy = True
        for index in range(len(s)-1):
            if int(s[index]) > int(s[index+1]):
                tidy = False
                break
        if tidy:
            print(f"Case #{i+1}: {j}")
            break
