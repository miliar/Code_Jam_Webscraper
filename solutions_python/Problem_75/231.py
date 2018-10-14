
cin = open("in.txt")
cout = open("out.txt" , "w")
TestCase = cin.readline()
for CaseNumber in range(1 , int(TestCase) + 1):
    CombDic = {}
    OppsDic = {}
    Input = cin.readline().split()
    NComb = int(Input[0])
    NOpps = int(Input[NComb + 1])
    Comb = Input[1:NComb+1]
    Opps = Input[NComb+2:NComb+NOpps+2]
    List = Input[-1]
    for c in Comb:
        CombDic[c[0:2]] = c[2]
        CombDic[c[0:2][::-1]] = c[2]
    for o in Opps:
        OppsDic[o[0]] = o[1]
        OppsDic[o[1]] = o[0]
    ans = ""
    for ele in List:
        ans += ele
        for c in CombDic:
            if ans[-2:] == c:
                ans = ans[:len(ans)-2] + CombDic[c]
        for o in OppsDic:
            for i in range(0 , len(ans)):
                if ans[i] == o and ans[len(ans)-1] == OppsDic[o]:
                    ans = ""
                    break
    ansstr = "Case #" + str(CaseNumber) + ": ["
    if ans == "":
        ansstr += ", "
    for c in ans:
        ansstr += c + ", "
    ansstr = ansstr[:len(ansstr)-2] + "]"
    cout.write(ansstr + "\n")
