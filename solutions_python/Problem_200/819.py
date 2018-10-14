[t, ] = [int(x) for x in input().split()]

def process_test(ind):
    num = list(input())
    for i in range(0, len(num)-1):
        if num[i] > num[i+1]:
            while i > 0 and num[i] == num[i-1]:
                i -= 1
            num[i] = str(int(num[i]) - 1)
            num[i+1:] = ['9' for _ in range(len(num[i+1:]))]
            print("Case #", ind, ": ", int(''.join(num)), sep='')
            return
    print("Case #", ind, ": ", int(''.join(num)), sep='')

for num in range(1, t + 1):
    process_test(num)