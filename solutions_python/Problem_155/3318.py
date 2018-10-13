def main():
    cases = [line.rstrip('\n') for line in open("A-large.in")]
    total = int(cases[0])
    for case in range(1,total+1):
        invited = 0
        inputstr = cases[case]
        maxlevel,audience = inputstr.split(" ")
        maxlevel = int(maxlevel)
        everybody = int(audience[0])
        if len(audience) > 1:
            for index in range(1,maxlevel+1):
                if int(audience[index])!=0:
                    if everybody < index:
                        invited += (index - everybody)
                        everybody+=(index - everybody)
                    everybody += int(audience[index])
        print("Case #"+str(case)+": "+str(invited))
        case+=1
        
        

if  __name__ =='__main__':main()
