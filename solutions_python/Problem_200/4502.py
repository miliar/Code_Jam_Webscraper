def findtidy(a):
    string = list(str(a))
    reverse = []
    for i in range(len(string)-1, -1, -1):
        reverse.append(string[i])
    #print(reverse)
    
    for i in range(len(reverse)-1):
        if reverse[i]<reverse[i+1]:
            if(i==len(reverse)-2 and reverse[i+1]=='1'):
                for j in range(i+1):
                    reverse[j]='9'
                del reverse[-1]
            else:
                for j in range(i+1):
                    reverse[j]='9'
                if reverse[i+1]!='0':
                    reverse[i+1]=chr(ord(reverse[i+1])-1)
                else:
                    reverse[i+1]='9'
    #print(reverse)
    preanswer=[]
    for i in range(len(reverse)-1, -1, -1):
        preanswer.append(reverse[i])
    answer = int("".join(preanswer))
    return answer

def main():
    t = int(input())  # read a line with a single integer

    for i in range(1, t + 1):
        print("Case #{}: {}".format(i, findtidy(input())))

if __name__ == "__main__":
    main()
