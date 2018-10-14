import math
import bisect

my_list = '''1 1
2 4
3 9
11 121
22 484
101 10201
111 12321
121 14641
202 40804
212 44944
1001 1002001
1111 1234321
2002 4008004
10001 100020001
10101 102030201
10201 104060401
11011 121242121
11111 123454321
11211 125686521
20002 400080004
20102 404090404
100001 10000200001
101101 10221412201
110011 12102420121
111111 12345654321
200002 40000800004
1000001 1000002000001
1001001 1002003002001
1002001 1004006004001
1010101 1020304030201
1011101 1022325232201
1012101 1024348434201
1100011 1210024200121
1101011 1212225222121
1102011 1214428244121
1110111 1232346432321
1111111 1234567654321
2000002 4000008000004
2001002 4004009004004
10000001 100000020000001
10011001 100220141022001
10100101 102012040210201
10111101 102234363432201
11000011 121000242000121
11011011 121242363242121
11100111 123212464212321
11111111 123456787654321
20000002 400000080000004
'''

def List_Gen():
    # base = []
    sqrt = []
    i = 1
    sq = 1
    # n = 0
    while sq <= 10 ** 15:
        if Is_Palindrome(str(i)):
            sq = i ** 2
            if Is_Palindrome(str(sq)):
                print(sq)
                # base.append(i)
                sqrt.append(sq)
                # n = n + 1
        i = i + 1
    return sqrt

def List_Convert():
    sqrt = []
    for pair in my_list.strip().split('\n'):
        sqrt.append(list(map(int, pair.split()))[1])        
    return sqrt

def Read_Input(filename):
    # The structure of output_list:
    # [T, [A, B], [A, B], ...]

    output_list = []

    input_file = open(filename, 'r')

    # T: num_case
    num_case = int(input_file.readline().strip('\n'))
    output_list.append(num_case)
       
    for i in range(num_case):
        A, B = list(map(int, input_file.readline().strip('\n').split()))
        output_list.append([A, B])        
    input_file.close()
    return output_list

def Fair_Square_Find(data_list):
    result = []
    T = data_list[0]
    for i in range(1, T + 1):
        A, B = data_list[i]
        n = bisect.bisect_right(sqrt_list, B) - bisect.bisect_left(sqrt_list, A)                
        result.append(n)
    return result

if __name__ == '__main__':
    #my_list = List_Gen()
    sqrt_list = List_Convert()
    input_list = Read_Input('C-large-1.in')
    result = Fair_Square_Find(input_list)
    ans = open('ans2.txt', 'w')
    i, n = 1, input_list[0]
    while i <= n:
        ans.write('Case #' + str(i) + ': ' + str(result[i-1]) + '\n')
        i = i + 1
    ans.close()    
    
