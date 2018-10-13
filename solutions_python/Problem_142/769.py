__author__ = 'fabrizio'

def get_letters(s):
    letters=[]
    for i in range(len(s)):
        if i==0 or s[i]!=s[i-1]:
            letters.append((s[i],1))
        else:
            letters[-1]=(s[i],letters[-1][1]+1)
    return letters

with open("input.txt") as fin:
    with open("output.txt","w") as fout:
        T=int(fin.readline().strip())
        for t in range(1,T+1):
            N=int(fin.readline().strip())
            strings=[]
            for i in range(N):
                strings.append(fin.readline().strip())

            letters_strings=[]
            for s in strings:
                letters_strings.append(get_letters(s))

            possible=True
            for i in range(1,N):
                if len(letters_strings[i])!=len(letters_strings[i-1]):
                    possible=False
                    break

                for j in range(len(letters_strings[i])):
                    if letters_strings[i][j][0]!=letters_strings[i-1][j][0]:
                        possible=False
                        break

            if not possible:
                 fout.write("Case #%s: Fegla Won\n"%(t,))
            else:
                res=0
                for n_letter in range(len(letters_strings[0])):
                    min_letter=1000
                    max_letter=1
                    for letters in letters_strings:
                        min_letter=min(min_letter,letters[n_letter][1])
                        max_letter=max(max_letter,letters[n_letter][1])

                    best_letter=1000
                    for res_letter in range(min_letter,max_letter+1):
                        tot=0
                        for letters in letters_strings:
                            tot+=abs(letters[n_letter][1]-res_letter)
                        best_letter=min(best_letter,tot)
                    res+=best_letter
                fout.write("Case #%s: %s\n"%(t,res))




