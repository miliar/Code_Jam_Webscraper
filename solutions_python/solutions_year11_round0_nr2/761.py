#!/usr/bin python

def main():
    path = "B-large.in"
    f = open(path)
    C = f.readline()
    for case in range(int(C)):
        combine_rules=[[None]*26 for x in range(26)]
        oppose_rules=[[False]*26 for x in range(26)]
        result = []

        line = f.readline()
        line = line.strip()
        linetokens = line.split(' ')
        #print "linetokens", linetokens
        
        #parse rules
        for rule in range(int(linetokens.pop(0))):
            arr = [c for c in linetokens.pop(0)]
            combine_rules[ord(arr[0])-ord('A')][ord(arr[1])-ord('A')] = arr[2]
            combine_rules[ord(arr[1])-ord('A')][ord(arr[0])-ord('A')] = arr[2]

        for rule in range(int(linetokens.pop(0))):
            arr = [c for c in linetokens.pop(0)]
            oppose_rules[ord(arr[0])-ord('A')][ord(arr[1])-ord('A')] = True
            oppose_rules[ord(arr[1])-ord('A')][ord(arr[0])-ord('A')] = True

        #print oppose_rules

        #process stream
        linetokens.pop(0)
        for char in linetokens.pop(0):
            #print "process",char
            result.append(char)

            if len(result) == 1:
                continue

            combi = combine_rules[ord(char)-ord('A')][ord(result[-2])-ord('A')]
            while combi and len(result) > 1:
                result.pop()
                result[-1] = combi
                char = combi
                if len(result) > 1:
                    combi = combine_rules[ord(char)-ord('A')][ord(result[-2])-ord('A')]

            if len(result) == 1:
                continue

            for char,check in enumerate(oppose_rules[ord(char)-ord('A')]):
                if check:
                    #print "check", chr(char + ord('A'))
                    if chr(char + ord('A')) in result:
                        #print "clear because of", chr(char + ord('A'))
                        result = []


        strresult = ""
        for x in result[0:-1]:
            strresult +=str(x)+", "
        if len(result)>0:
            strresult +=str(result[-1])
        print "Case #"+str(case+1)+": "+"["+strresult+"]"

if __name__ == "__main__":
        main()

