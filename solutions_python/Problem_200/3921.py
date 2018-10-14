n = int(input())
numbers = [input() for i in range(n)]

def check_neat(num):
    for i in range(len(num)-1,0,-1):
        if num[i]<num[i-1]:
            return False
    return True

for j in range(n):
    count = int(numbers[j])
    while count>= 0:
        if check_neat(str(count)):
            print("Case #{}: {}".format(j+1,count))
            break
        count-=1
