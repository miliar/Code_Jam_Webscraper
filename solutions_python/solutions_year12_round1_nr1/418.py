#!/usr/bin/env python
#coding:utf-8

def solve(typed,passlen,prob):
    firstwrong = []
    for i in range(typed):
        tmp = (1-prob[i])
        for j in prob[:i]:
            tmp = tmp * j
        firstwrong.append(tmp)

    firstwrong.insert(0,1-sum(firstwrong))
    scores = []
    for i in range(len(firstwrong)):
        score = 0
        for j,prob in enumerate(firstwrong):
            if j==0:
                score = score + (i+passlen-typed+i+1)*prob
            elif (typed-j+1) <= i:
                score = score + (i+passlen-typed+i+1)*prob
            else:
                score = score + (i+passlen-typed+i+1+passlen+1)*prob

        scores.append(score)

    #Right
    scores.append(passlen+2)
    return min(scores)



def main():
    T = int(input())
    for i in range(T):
        inp = input().strip().split(' ')
        inp = [int(i) for i in inp]
        A = inp[0]
        B = inp[1]
        inp = input().strip().split(' ')
        inp = [float(i) for i in inp]
        x = solve(A,B,inp)
        print("Case #%d: "%(i+1)+str(x))

if __name__ == "__main__":
    main()
