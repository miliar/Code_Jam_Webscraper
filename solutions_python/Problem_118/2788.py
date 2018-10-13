

def is_palindrome(num):
    str_num = str(num)
    for i in range(len(str_num)/2):
        if str_num[i] != str_num[-1]:
            return False
    return True
    
def is_square(num):
    square = pow(int(num), 0.5)
    if square == int(square):
        if is_palindrome(str(int(square))):
            return True
    return False
    
if __name__ == "__main__":
    with open("C-small-attempt0.in", "r") as f:
        content = f.readlines()

    for i in range(int(content[0])):
        count = 0
        range_nums = content[i+1].split()
        for j in range(int(range_nums[0]), int(range_nums[1])+1):
            if is_palindrome(j) and is_square(j):
                count += 1
        print "Case #%d: %d" % (i+1, count)