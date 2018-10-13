# encoding=utf-8
def main():
    f = open('B-large.in','r')
    w = open('B-large.out','w')

    t = int(f.readline())
    #t = int(raw_input())

    for i in range(t):
        input = f.readline().split()
        line = input[0]
        #line = raw_input()
        r=0

        while tidy(line)==False:
            for j in range(len(line)-1):
                if line[j]>line[j+1]:
                    break

            r= int(line[:j+1])-1
            for j in range(len(line)-j-1):
                r=r*10+9
            line = str(r)

        #print "Case #{}: {}".format(i+1,line)
        w.write("Case #{}: {}".format(i+1,line) + '\r')

    f.close()
    w.close()

def tidy(s):
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return False
    return True

main()