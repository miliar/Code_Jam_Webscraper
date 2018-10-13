def reverse(string):
    if string == '-':
        return '+'
    elif string == '+':
        return '-'

def find(string):
    _ = string.index('-',0,len(string))
    return _
# file = open('B-large.in','r')
# out = open('output1.txt','a')


# N = int(file.readline())
# strings = file.readlines()
N = int(input())
for e in range(N):
    # token = strings[e].split(" ")
    token = input().split(" ")
    string = [x for x in token[0]]
    num = int(token[1])
    count = 0
    while True:
        if '-' not in string:
            print("Case #{}: {}".format(str(e + 1), count))
            break
        _=find(string)
        if _+num > len(string):
            print("Case #{}: {}".format(str(e + 1), "IMPOSSIBLE"))
            break
        for i in range(_,_+num):
            string[i] = reverse(string[i])
        count+=1

    # print("Case #{}: {}".format(str(e + 1), str(int(str_sum))))
    # out.write('Case #'+str(e+1)+': '+str(int(str_sum))+'\n')
# out.close()
# file.close()
