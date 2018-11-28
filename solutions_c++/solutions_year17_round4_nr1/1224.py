#include<stdio.h>
#include<string.h>
#include<memory.h>
#include<algorithm>
#include <map>
#include <unordered_map>
#include<utility>
#include<iostream>
#include<math.h>
#include<vector>
#include <queue>

using namespace std;
int dp[101][101][101][101][4];

int solve(int g1, int g2, int g3, int g4, int rem,int P) {
  if(dp[g1][g2][g3][g4][rem]!=-1) {
      return dp[g1][g2][g3][g4][rem];
  }
    int bestres = 0;

    if(g1>0) {
        bestres = max(solve(g1-1,g2,g3,g4,rem,P) + ((rem > 0)?0:1), bestres);
    }


    if(g2>0) {
        bestres = max(solve(g1,g2-1,g3,g4,(rem-1+P)%P,P) + ((rem > 0)?0:1), bestres);
    }


    if(g3>0) {
        bestres = max(solve(g1,g2,g3-1,g4,(rem-2+P)%P,P) + ((rem > 0)?0:1), bestres);
    }


    if(g4>0) {
        bestres = max(solve(g1,g2,g3,g4-1,(rem-3+P)%P,P) + ((rem > 0)?0:1), bestres);
    }

    return dp[g1][g2][g3][g4][rem]=bestres;


}

int solveCase(int N,int P) {
    int g0 = 0, g1 = 0, g2 = 0, g3 = 0;
    for(int i=0;i<N;i++) {
        int K;
        cin >> K;
        switch (K%P) {
                case 0: g0++; break;
            case 1: g1 ++; break;
            case 2: g2++; break;
            case 3: g3++;

        }




    }
    memset(dp,-1,101*101*101*101*4*sizeof(int));
    return solve(g0,g1,g2,g3,0,P);
}


int main() {
    int testCases;
    cin >> testCases;
    for(int i=0;i<testCases; i++) {
        int N,P;
        cin>> N>>P;
        cout << "Case #" << (i + 1) << ": " << solveCase(N,P) << endl;

    }

}