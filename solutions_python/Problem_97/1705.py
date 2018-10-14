
def remove_start(nums):
    copy = nums[:]
    for i in copy:
        if str(i[1])[0] == "0":
            nums.remove(i)
    return nums

def recycled_numbers(num, minimum, maximum):
    orig_num = num
    num = str(num)
    recycled = []
    for i in range(len(num)-1):
        temp = num[-1*(i+1):] + num[:len(num)-i-1]

        if (int(temp) >= minimum) and (int(temp) <= maximum) and (int(temp) > orig_num):
            recycled.append((num, temp))
    return recycled

if __name__ == "__main__":
    lines = int(raw_input())
    for i in range(lines):
        raw = raw_input()
        splitted = raw.split(" ")
        start = int(splitted[0])
        end = int(splitted[1])
        total = set([])
        for j in range(start, end+1):
            total = total | set(remove_start(recycled_numbers(j, start, end)))
        print  "Case #" + str(i+1) + ": " + str(len(total))
