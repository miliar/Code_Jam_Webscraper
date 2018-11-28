from sys import stdin

if __name__ == '__main__':
    t = int(stdin.readline().strip())
    for i in range(t):
        chars = stdin.readline().strip().split()[1]
        nums = [int(char) for char in chars]
        stand = 0
        need = 0
        for j in range(len(nums)):
            if (stand + need) < j:
                need += (j - stand - need)
            stand += nums[j]
        print('Case #{0}: {1}'.format(i+1, need))