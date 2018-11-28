//
// Created by Denis Mukhametianov on 08.04.17.
//

#include <iostream>
#include <set>
#include <map>


using namespace std;


const int infin = (int)1e5;
int currentAnswer;


int solve(int debuffs, int buffs, int initHd, int ad, int hk, int ak, int buff, int debuff, bool trace = false) {
    int hd = initHd;
    for(int i = 1; i <= currentAnswer; i++) {
        if(hd <= (ak - (debuffs > 0 ? debuff : 0)) && hk > ad) {
            hd = initHd;
            if(trace)fprintf(stderr, "heal\n");
        } else if(debuffs > 0) {
            debuffs--;
            ak = max(ak - debuff, 0);
            if(trace)fprintf(stderr, "debuff\n");
        } else if(buffs > 0) {
            buffs--;
            ad += buff;
            if(trace)fprintf(stderr, "buff\n");
        } else {
            hk -= ad;
            if(trace)fprintf(stderr, "attack\n");
        }
        if(hk <= 0)
            return i;
        hd -= ak;
        if(hd <= 0)
            return infin;
        if(trace)fprintf(stderr, "%d %d %d %d\n", hd, ad, hk, ak);
    }
    return infin;
}


void solveC(int testNumber) {
    int hd, ad, hk, ak, b, d;
    cin >> hd >> ad >> hk >> ak >> b >> d;
    currentAnswer = infin;
    int bestDec = 0;
    int bestInc = 0;
    for(int decreases = 0; decreases <= (d == 0 ? 0 : ((ak / d) + 5)); decreases++)
        for(int increases = 0; increases <= 100; increases++) {
            int z = solve(decreases, increases, hd, ad, hk, ak, b, d);
            if(z < currentAnswer) {
                currentAnswer = z;
                bestDec = decreases;
                bestInc = increases;
            }
        }
    //solve(bestDec, bestInc, hd, ad, hk, ak, b, d, true);
    if(currentAnswer != infin)
        printf("Case #%d: %d\n", testNumber, currentAnswer);
    else
        printf("Case #%d: IMPOSSIBLE\n", testNumber);
}


void runC() {
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int tc;
    cin >> tc;
    for (int i = 0; i < tc; i++) {
        solveC(i + 1);
    }
}