def isTidy(N):
    dig = []
    while N >= 1:
        r = N % 10
        N = N // 10
        dig.append(r)
    
    sd = sorted(dig)                        
    dig.reverse()     
    
    if sd == dig:     
        tidy = 1               
    else:              
        tidy = 0        
    return tidy 


def TidyNumbers(N):
    for i in range(N):
        if isTidy(N - i) == 1:
            break
    print(N - i)   

# def main():
T = int(input())

for i in range(T):
    N = int(input())
    # print(N)

    print("Case #%d: "%(i + 1), end='')
    TidyNumbers(N)
