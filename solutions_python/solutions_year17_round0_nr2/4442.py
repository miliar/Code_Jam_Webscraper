from sys import argv

def solution(num):

    index_to_fix = -1
    if len(num) != 1:
        for i in xrange(1,len(num)):
            if num[i-1] > num[i]:
                index_to_fix = i-1
                break
    
    # print index_to_fix

    if index_to_fix == -1:
        return num

    if index_to_fix == 0:
        if num[index_to_fix] == 1:
            return [9]*(len(num)-1)
        else:
            return [num[index_to_fix]-1] + [9]*(len(num)-1)

    
    for i in xrange(index_to_fix, -1,-1):
        if num[index_to_fix]-1<num[index_to_fix-1]:
            index_to_fix -=1
        else:
            num[index_to_fix] -=1
            num[index_to_fix+1:] = [9]*len(num[index_to_fix+1:])
            break
    return num


def main():
    filename = './B-small-attempt0.in'
    if len(argv) > 1:
        filename = argv[1]

    with open(filename) as f:
        T = int( f.readline() )
        case_count = 0
        for i in xrange(T):
            case_count += 1
            d = f.readline().rstrip('\n')
            num = solution(map(int,d))
            ans = int(''.join(map(str,num)))
            # print d,num,ans
            print "Case #" + str(case_count) + ": " + str(ans)
main()

# print solution(list('111111111111111110'))
# print solution(list('132'))
# print solution(list('1000'))
# print solution(list('7'))
# g = 409
# num =  solution(map(int,str(g)))
# kint = int(''.join(map(str,num)))
# print kint
