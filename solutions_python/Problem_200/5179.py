def tidy(number):
    numberx = [int(d) for d in str(number)]
    for i in range(len(numberx)):
        if i == 0:
            continue
        else:
            if numberx[i] < numberx[i-1]:
                return False
            else:
                continue
    return True

t = int(input())

for i in range(t):
    n = int(input())

    for c in range(n, 0, -1):
        if tidy(c):
            print ("Case #"+ str(i+1)+":" ,c)
            break
        else:
            continue
        
