import sys

def main():
    if len(sys.argv) >= 2:
        file = sys.argv[1]
        f = open(file)
        numOfTest = f.readline().split()[0]
        for i in range(int(numOfTest)):
            length = int(f.readline().split()[0])
            list_a = f.readline().split()
            list_b = f.readline().split()
            list_a.sort()
            list_b.sort()
            war = judge_war(list_a, list_b, length)
            deceit = judge_war(list_b, list_a, length)
            print "Case #" + str(i+1) + ": " + str(length - deceit) + " " + str(war)
            
def judge_war(list_a, list_b, length):
    count = 0
    index_b = length -1
    index_a = length -1
    while index_a >=0 and index_b >=0:
        if(float(list_b[index_b]) > float(list_a[index_a])):
            count +=1
            index_b -=1
            index_a -=1
        else:
            index_a -=1
    return length - count

    
if __name__ == '__main__':
    main()