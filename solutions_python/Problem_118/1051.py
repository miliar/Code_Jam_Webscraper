file = open('./C-small-attempt0.in')
new_file = open('./C-small-attempt.out', 'w')

testcases = [x.rstrip() for x in file.readlines()]

def palindrome(num):
    s_num = str(num)
    for i in range(len(s_num)/2):
        if s_num[i] != s_num[-(i+1)]:
            return False
    return True
        

for i in range(int(testcases[0])):
    x, y = testcases[i+1].split()
    x, y = int(x), int(y)
    root_x, root_y = x**(0.5), y**(0.5)
    root_x, root_y = int(root_x), int(root_y)
    if root_x**2 < x:
        root_x = root_x + 1
    possible = [z**2 for z in range(root_x, root_y+1) if palindrome(z) if palindrome(z**2)]
    count = len(possible)
    new_file.write('Case #%s: %s\n' % ((i+1), count))

file.close()
new_file.close()



