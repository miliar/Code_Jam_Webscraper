from sys import stdin


def func(n,p):
    n = list(map(int,n))
    while True:
        t = False
        for i in range(len(n)-1):
            y = n.copy()
            y.sort()
            if n[i] > n[i+1]:
                if n[i] == 1:
                    if i == 0:
                        t = True
                        y = n.copy()
                        y.sort()
                        n = [9]* (len(n)-1)
                        break
                    else:
                        y = n.copy()
                        y.sort()
                        
                        n = n[:i]+[0]+[9]*(len(n)-(i+1))
                        
                else:
                    y = n.copy()
                    y.sort()
                    n = n[:i]+[n[i]-1]+[9]*(len(n)-(i+1))
                y = n.copy()
                y.sort()
                    
                if n == y:
                    t = True
                    break
        if t:
            break
    n = list(map(str,n))
    n = "".join(n)
    print("Case #"+str(p+1)+":",n)
         
def main():
    x = int(stdin.readline())
    for i in range(x):
        n = int(stdin.readline())
        if n < 10:
            print("Case #"+str(i+1)+":",n)
        else:
            y = list(str(n))
            y.sort()
            if y == list(str(n)):
                print("Case #"+str(i+1)+":",n)
                
            else:
                func(list(str(n)),i)
                    
        
main()
