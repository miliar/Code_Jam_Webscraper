def print_case(case,result):
    print "Case #"+str(case+1)+": "+str(result)

cases = ['441','414','433','432','423','421','412','422','411','442','424','431','413',
         '344','322','321','312','311','342','324','341','314','331','313',
         '231','213','233','211']

T = int(raw_input())
for case in range(T):
    raw = raw_input().split(" ")
    X = int(raw[0])
    R = int(raw[1])
    C = int(raw[2])
    if X == 1:
        print_case(case, "GABRIEL")
        continue
    if (str(X)+str(R)+str(C)) in cases:
        print_case(case, "RICHARD")
    else:
        print_case(case, "GABRIEL")