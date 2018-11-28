#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#* File Name : pancake.py
#* Purpose : Code Jam 2017
#* Creation Date : 08-04-2017
#* Last Modified : Sat 08 Apr 2017 22:00:52 EEST
#* Created By : Vasilis Livanos <basilis3761@yahoo.gr>
#_._._._._._._._._._._._._._._._._._._._._.*/

def main():
    for t in range(int(input())):
        cn = 0
        s, k = input().split()
        k = int(k)
        s = list(s)
        for i, c in enumerate(s):
            if(cn >= len(s)):
                break
            if(c != '+'):
                cn += 1
                for j in range(k):
                    if(i+j < len(s)):
                        if(s[i+j] == '-'):
                            s[i+j] = '+'
                        else:
                            s[i+j] = '-'
                    else:
                        cn = len(s)
                        break
        if(cn >= len(s)):
            print("Case #", t+1, ": IMPOSSIBLE", sep="")
        else:
            print("Case #", t+1, ": ", cn, sep="")

if __name__ == "__main__":
    main()
