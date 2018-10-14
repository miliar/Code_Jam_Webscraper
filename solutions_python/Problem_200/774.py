#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#* File Name : tidy.py
#* Purpose : Code Jam 2017
#* Creation Date : 08-04-2017
#* Last Modified : Sat 08 Apr 2017 22:33:11 EEST
#* Created By : Vasilis Livanos <basilis3761@yahoo.gr>
#_._._._._._._._._._._._._._._._._._._._._.*/

def main():
    for t in range(int(input())):
        n = int(input())
        l = len(str(n))
        if(l > 1):
            for i in range(l-1):
                d1 = (n % 10**(i+1)) // 10**i
                d2 = (n % 10**(i+2)) // 10**(i+1)
                if(d2 > d1):
                    c = n % 10**(i+1) + 1
                    n -= c
        print("Case #", t+1, ": ", n, sep="")

if __name__=="__main__":
  main()

