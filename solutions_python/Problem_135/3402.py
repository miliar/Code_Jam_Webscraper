import sys
def read_test_case(t):
    #ans1

    ans_1 = int(sys.stdin.readline())-1
    arr_1 = [[0]*4]*4
    for i in range(4):
        arr_1[i] = map(int,sys.stdin.readline().split(" "))

    #print "Arr", arr_1
    #print "Ans", ans_1


    #ans2

    ans_2 = int(sys.stdin.readline())-1
    arr_2 = [[0]*4]*4
    for i in range(4):
        arr_2[i] = map(int,sys.stdin.readline().split(" "))

    #print "Arr2", arr_2
    #print "Ans2", ans_2

    #finding common and unique of two rows
    comm = []
    uniq = []
    for i in range(4):
        ele1 = arr_1[ans_1][i]
        ele2 = arr_2[ans_2][i]

        #print ele1, ele2

        if ele1 in arr_2[ans_2] and ele1 not in comm:
            comm.append(ele1)
        elif ele1 not in uniq:
            uniq.append(ele1)

        #if ele2 in arr_1[ans_1] and ele2 not in comm:
        #    comm.append(ele2)
        #elif ele2 not in uniq:
        #    uniq.append(ele2)

    #print "common\n", comm
    #print "Unique\n", uniq
    fh = open('output','a')
    if len(comm) == 1:
        fh.write("Case #"+str(t)+": "+str(comm[0]))
    elif len(comm) > 1:
        fh.write("Case #"+str(t)+": Bad magician!")
    elif len(comm) == 0:
        fh.write("Case #"+str(t)+": Volunteer cheated!")
    fh.write('\n')
    fh.close()
    return

def main():
    for t in range(int(raw_input())):
        read_test_case(t+1)

main()