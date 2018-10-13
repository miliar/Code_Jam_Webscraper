def main():
    ff = open('Aoutput.txt', 'w')
    tc = int(raw_input())
    for loop in range(0, tc):
        n = int(raw_input())
        str1 = raw_input()
        str2 = raw_input()
        l1 = len(str1)
        l2 = len(str2)
        indd1 = 0
        indd2 = 0
        ans = 0
        flag = 0
    while indd1<l1 or indd2<l2:
        if indd1 < l1 and indd2 < l2 and str1[indd1] == str2[indd2]:
            indd1=indd1+1
            indd2=indd2+1
            continue
        elif indd1 < l1 and indd2 > 0 and str1[indd1] == str2[indd2-1]:
            ans=ans+1
            indd1=indd1+1
            continue
        elif indd1 > 0 and indd2 < l2 and str1[indd1-1] == str2[indd2]:
            ans=ans+1
            indd2=indd2+1
            continue
        else:
            print "Fegla Won"
            ff.write("Case #"+str(loop+1)+": Fegla Won\n")
            flag = 1
            break
    if flag==0:
        ff.write("Case #"+str(loop+1)+": "+str(ans)+"\n")
        print ans
    ff.close()
main()
