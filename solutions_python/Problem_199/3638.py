def snapout():
        totalTest = int(input())
        inpu = []
        result =[]
        change = []
        flipby = []
        # input of values
        for i in range(totalTest):
                inpu.append(input())
                x = inpu[i].split(" ")
                change.append(x[0])
                flipby.append(int(str(x[1])))
        # to flip the symbols
        for i in range(totalTest):
                count = 0
                # if all are already +
                if change[i].count("+") == len(change[i]):
                        result.append(0)
                        continue
                pan = int(flipby[i])
                # if the string is imposible to move
                if len(change[i])<pan:
                        result.append("IMPOSSIBLE")
                        continue
                #if something need to be changed
                for j in range(len(change[i])-pan+1):
                        if change[i][j]=="-":                                
                                change[i]=change[i][:j]+ ''.join('-' if x == '+' else '+' for x in change[i][j:j+pan]) + change[i][j+pan:]      
                                count+=1
                # if a - is also removed
                if change[i].count("-")>0:
                        result.append("IMPOSSIBLE")
                        continue
                result.append(int(count))
        #printing of final output
        for i in range(1,len(result)+1):
                print("Case" , "#"+str(i)+":" , result[i-1])
snapout()
