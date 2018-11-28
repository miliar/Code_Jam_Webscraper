



def tidy(num):
    nums = [int(n) for n in list(num)]


    for i in range(len(nums) - 1):
        back = len(nums) - i - 1
        front = len(nums) - i - 2

        if nums[front] > nums[back]:
            nums[front] -= 1

            for j in range(back, len(nums)):
                nums[j] = 9

    return int("".join(map(str, nums)))




t = int(input())

for i in range(1, t + 1):

    print("Case #" + str(i) + ": " + str(tidy(input())))






