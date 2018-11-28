#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#* File Name : stalls.py
#* Purpose : Code Jam 2017
#* Creation Date : 08-04-2017
#* Last Modified : Sun 09 Apr 2017 01:14:14 EEST
#* Created By : Vasilis Livanos <basilis3761@yahoo.gr>
#_._._._._._._._._._._._._._._._._._._._._.*/

def main():
    for t in range(int(input())):
        n, k = map(int, input().split())
        s = bin(k)[2:]
        l = len(s)
        for i in range(l):
            a = b = n // 2
            if(n % 2 == 0):
                b -= 1
            if(i < l-1):
                if(s[-(i+1)] == '0'):
                    n = a
                else:
                    n = b
        print("Case #", t+1, ": ", a, " ", b, sep="")

if __name__=="__main__":
  main()

