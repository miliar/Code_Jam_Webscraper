#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      udonko
#
# Created:     05/05/2013
# Copyright:   (c) udonko 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def calcHowManyTimesAdd(currentval, target):
    if currentval == 1:
        return -1, 10000000000000000000
    elif(currentval > target):
        return 0 , currentval+target
    elif currentval == target:
        return 1 , currentval + currentval -1 + target
    else:
        count = 0
        while True:
            currentval += currentval - 1
            count += 1
            if currentval > target:
                break
        return count , currentval +target


minvalue = 0

def resolve2(current, n, count, index, motes):
    global minvalue
    if count > minvalue:
        return
    if index == n:
        minvalue = min(count, minvalue)
        return
    if current > max(motes):
        minvalue = min(count, minvalue)
        return
    value = motes[index]

    num_op , currentval = calcHowManyTimesAdd(current, value)
    if num_op == -1:
        return
    elif num_op == 0:
        # no operation
        resolve2(currentval , n, count, index+1, motes)
    else:

        # add
        resolve2(currentval , n, count + num_op, index+1, motes )
        # or
        if num_op > 1:
            #remove
            resolve2(current, n, count+1, index+1, motes)


def resolve(a,n,motes):
    global minvalue
    minvalue = n
    motes.sort()

    resolve2(a,n,0,0,motes)

    return minvalue





def main():
    infile = open("input.txt","r")
    outfile = open("output.txt","w")
    num = int(infile.readline())

    # num of test loop
    for i in range(num):
        #sys.stdout.write(str(i)+"----\n")
        temp = infile.readline()
        temps = temp.split()
        a = int(temps[0])
        n = int(temps[1])

        temp = infile.readline()
        temps = temp.split()
        motes = [int(j) for j in temps]
        #resolve
        ret = resolve(a,n,motes)
        outfile.write("Case #"+str(i+1)+": "+str(ret)+"\n")



    infile.close()
    outfile.close()

if __name__ == '__main__':
    main()
