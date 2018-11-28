#google code jam '09 template
#
import math
strip = ['b','f','g','h','i','k','n','p','q','r','s','u','v','x','y','z']
sentence = 'welcome to code jam'

file_name = 'C-small-attempt1.in'
read_fp = None

def main():
    global strip
    global sentence
    global read_fp
    Initializations()

    num = int(read_fp.readline().strip())

    for m in range(num):
        count = 0
        exp = read_fp.readline().strip()
        for i in range(len(strip)):
            exp.replace(strip[i],'')
        count = solve(exp,sentence)

        if count == 0:
            print "Case #%i:"%(m+1),'0000'
            continue
        count = count % 1000
        place = 3-int(log(count,10))
        print "Case #%i:"%(m+1), '0'*place+str(count)

        

    read_fp.close()
    return


def solve(exp_remain,sent_remain):
    
    if len(sent_remain) == 1:
        return exp_remain.count(sent_remain[0])
    else:
        sum = 0
        index = exp_remain.find(sent_remain[0])
        while index >= 0:
            sum += solve(exp_remain[index+1:],sent_remain[1:])
            exp_remain = exp_remain[index+1:]
            index = exp_remain.find(sent_remain[0])
        return sum
            

def Initializations():
    global file_name
    global read_fp
    read_fp = open(file_name, 'r')
    return

if (__name__ == "__main__"):
    main()
