T= int(input())

for case in range(T):
    line= input().split()
    N=int(line[1])
    D=int(line[0])
    
    time=0;
    for i in range(N):
      line=input().split()
      K=int(line[0])
      S=int(line[1])
      thistime=(D-K)/S
      time=max(time,thistime)

    print("Case #"+str(case+1)+": "+str(D/time))

