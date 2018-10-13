for t in range(int(input())):
    n = int(input())
    i=1
    while(i<n):
    	input()
    	i+=1
    x = set(map(int, input().split(" ")))
    while(i<4):
    	input()
    	i+=1
    n = int(input())
    i=1
    while(i<n):
    	input()
    	i+=1
    y = set(map(int, input().split(" ")))
    while(i<4):
    	input()
    	i+=1
    z = x.intersection(y);
    l = len(z)
    if l==0:
    	ans = 'Volunteer cheated!'
    elif l==1 :
    	ans = list(z)[0]
    else :
    	ans = 'Bad magician!'
    print("Case #{}: {}".format(t+1,ans))
    
