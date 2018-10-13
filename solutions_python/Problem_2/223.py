import os,array
from array import *

bgPrint = False

def solve(case, train_arr):
    tr_present = 0
    tr_req = 0
    counter = -1
    for i in train_arr:
        counter = counter + 1
        if i != 0:
            if i + tr_present < 0:
                tr_req = tr_req - (i + tr_present)
                tr_present = 0
                if bgPrint:
                    print str(counter/60) + ":" + str(counter%60),
            else:
                tr_present = tr_present + i

    if bgPrint:
        print
    return tr_req

def get_t(tm):
    (h,m) = map(int,tm.split(":"))
    t = h*60 + m
    return t


def main():
    print "Current directory has: ", os.listdir(".")
    file_name = raw_input("Enter the file name: ")
    try:
        file_handle = file(file_name, 'r')
        num_cases = int(file_handle.readline())
        for case in range(num_cases):
            T_min = int(file_handle.readline())
            trains_A = [0]*(24*60 + T_min + 1)
            trains_B = [0]*(24*60 + T_min + 1)

            (NA, NB) = map(int, file_handle.readline().split())
            for i in range(NA):
                (deptA, arrB) = file_handle.readline().split()
                t = get_t(deptA)
                trains_A[t] = trains_A[t] - 1
                t = get_t(arrB)
                trains_B[t + T_min] = trains_B[t + T_min] + 1

            for i in range(NB):
                (deptB, arrA) = file_handle.readline().split()
                t = get_t(deptB)
                trains_B[t] = trains_B[t] - 1
                t = get_t(arrA)
                trains_A[t + T_min] = trains_A[t + T_min] + 1

            fh = file('temp', 'a')
            fh.write("Case #" + str(case+1) + str(trains_A) + "\n" + str(trains_B))
            res_A = solve(case, trains_A)
            res_B = solve(case, trains_B)
            print "Case #" + str(case + 1) + ":", res_A, res_B
            fh.close()

        file_handle.close()
    except IOError, e:
        print "Bad file!"
        raw_input("Press any key to exit...")
        return 0
    

if __name__ == "__main__":
    main()
