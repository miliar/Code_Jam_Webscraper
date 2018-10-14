if __name__ == "__main__":
    t = int(input())
    for i in range(1, t+1):
        num = str(input())
        ans=""
        for digit in range(0, len(num)-1):

            if int(num[digit])> int(num[digit+1]) :
                ans+=str(int(num[digit])-1)
                ans+="9"*(len(num)-1-digit)
                for backward in reversed(range(1, digit+1)):
                    if int(ans[backward])< int(ans[backward - 1]):
                        ans = ans[:(backward -1)] + str(int(ans[backward-1])-1) +'9' + ans[(backward+1):]
                break
            ans+=(num[digit])
            if digit == (len(num)-2):
                ans+=(num[digit+1])
    

        
        if len(num)==1:
            ans = num
        #remove leading non-zeros
        elif ans[0] == 0:
            ans = ans[1:]
        
        print("Case #{}: {}".format(i, int(ans)))