
def test(n1,list1,n2,list2):
    count = 0
    #list = set(list1[n1-1])& set(list2[n2-1])
    list = set(list1[n1-1]).intersection(list2[n2-1])
    if (len(list) == 1):
        return list.pop()
    elif (len(list) == 0):
        return "Volunteer cheated!"
    else:
        return "Bad magician!"

n = int(raw_input())
for case in range(1,n+1):
        row_number_1 = int(raw_input())
        list1 = [[] for i in range(4)]
        for i in range(4):
            list1[i].extend(map(int,raw_input().split()))
        row_number_2 = int(raw_input())
        list2 = [[] for i in range(4)]
        for i in range(4):
            list2[i].extend(map(int,raw_input().split()))
        output = test(row_number_1,list1,row_number_2,list2)
        print "Case #%d:" %(case),output
