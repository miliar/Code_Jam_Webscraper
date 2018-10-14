#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Tushar Sadana
#
# Created:     08-04-2017
# Copyright:   (c) Tushar Sadana 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def checktidy(a):
    flag=True
    i=0
    while i<len(a)-1:
        if a[i]>a[i+1]:
            flag = False
            break
        i+=1

    return flag


def largesttidy(n):

    m=int(n)
    for i in range(m,0,-1):
        a=[]
        while i>0:
            b=i%10
            a.insert(0,b)
            i=i/10

        if checktidy(a):
            for i in range(0,len(a)):
                a[i]=str(a[i])
            num=''
            for i in range(0,len(a)):
                num+=a[i]

            num=int(num)
            break
    return num


def main():
    pass

if __name__ == '__main__':
    main()

input_file = open('b.in')
output_file = open('file.out', 'w')
i=0
t=int(input_file.readline())
if t>=1 and t<=100:
    for line in input_file:

        answer = largesttidy(line)

        output_file.write("Case #{}: {} ".format(i+1, answer))
        output_file.write("\n")
        i+=1
input_file.close()
output_file.close()




