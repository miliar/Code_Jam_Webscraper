data = open('input.txt').readlines()
num_tests = int(data[0])



def magic_trick(a1,d1,a2,d2):
    """
    [{'answer': 2, 'arrangement': [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]}
    {'answer'': 3 'arrangement': [[1,2,5,4], [3,11,6,15], [9,10,7,12], [13,14,8,16]]}]
    """
    number_set1 = set(d1[int(a1)-1].split())
    number_set2 = set(d2[int(a2)-1].split())
    common_nums = number_set2.intersection(number_set1)
    ans_list = list(common_nums)
    if len(ans_list) == 1:
        return ans_list[0]
    if len(ans_list) > 1:
        return "Bad magician!"
    else:
        return "Volunteer cheated!"
    print common_nums


x = 0
for i in range(num_tests):
    ans1 = int(data[x+1].strip('\n'))
    l1 = [data[x+2].strip('\n'), data[x+3].strip('\n'), data[x+4].strip('\n'), data[x+5].strip('\n')]
    ans2 = int(data[x+6].strip('\n'))
    l2 = [data[x+7].strip('\n'), data[x+8].strip('\n'), data[x+9].strip('\n'), data[x+10].strip('\n')]
    result = magic_trick(ans1, l1, ans2, l2)
    print "Case #%s: %s" %(i+1, result) 
    x = x+10

