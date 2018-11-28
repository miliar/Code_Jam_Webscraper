T = int(input())
for t in range(1,T+1):
    r = int(input())
    for i in range(r-1):
        l = input()
    a = set(map(int, input().split()))
    for i in range(r+1, 5):
        l = input()    
    r = int(input())
    for i in range(r-1):
        l = input()
    b = set(map(int, input().split()))
    for i in range(r+1, 5):
        l = input()  
    c = list(a & b)
    if len(c) == 1:
        print('Case #'+str(t)+':',*list(c))
    elif len(c) > 1:
        print('Case #'+str(t)+':','Bad magician!')
    else:
        print('Case #'+str(t)+':','Volunteer cheated!')
   