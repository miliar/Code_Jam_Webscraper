
def solve(arr):
    if arr.count(0) == len(arr): #just to make it work for all 0s, for elegance
        return 0
    if len(list(filter(lambda x: x<=1,arr))) == len(arr):
        return 1
    copy_stay = [0 if x==0 else x-1 for x in arr]
    time_stay = solve(copy_stay)
    most = arr.index(max(arr))
    
    copy_split = arr[:]
    if copy_split[most] != 9:
        half = copy_split[most]//2
    else:
        half = copy_split[most]//3 # from 1 to 9, 9 is the only one that's better to not divide in halfs
    copy_split[most] -= half #handles odd numbers
    copy_split.append(half)
    time_split = solve(copy_split)
    
    return 1 + min(time_split, time_stay)

T = int(input())
for case in range(T):
    D = input()
    arr = list(map(int, list(input().split(' '))))
    time = solve(arr)
    print("Case #", case+1, ': ', time, sep='')
    