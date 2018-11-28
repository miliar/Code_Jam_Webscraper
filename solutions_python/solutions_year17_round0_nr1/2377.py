


def solve(input_txt):
    K = int( "".join(s for s in input_txt if s.isdigit()))
    input_list = list(s=="+" for s in input_txt if s in ("+","-"))
    #print(K,input_list)
    ans =0
    for i in range(0,len(input_list)- K+1):
        if input_list[i] == False:
            #print("-",i)
            ans += 1
            for j in range(K):
                input_list[i+j] = not input_list[i+j]
    if all(input_list):
        print(ans)
    else:
        print("IMPOSSIBLE")

for i in range(int(input())):
    print("Case #{}:".format(i+1),end=" ")
    solve(input())