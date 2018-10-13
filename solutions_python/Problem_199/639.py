#coding:utf8

def main():
    cases = int(raw_input())
    for i in range(cases):
        inp = raw_input().split(" ")
        text = inp[0]
        k = int(inp[1])
        print "Case #" + str(i+1)+": " + str(algorithm(text,k))




def format(input):
    lis = [a for a in input]
    return lis



def flip(lis,index,k):
    if index+k>len(lis):
        return
    for i in range(index,index+k):
        if lis[i] == "+":
            lis[i] = "-"
        else:
            lis[i] = "+"


def algorithm(text,k):
    count = 0
    lis = format(text)
    #print lis
    for item in lis:
        if item == "-":
            flip(lis, lis.index(item),k)
            count+=1
    for item in lis:
        if item == "-":
            return "IMPOSSIBLE"
    return count
            


main()

