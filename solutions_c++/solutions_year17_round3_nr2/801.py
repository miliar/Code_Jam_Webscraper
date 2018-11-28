#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

const int MAX_N = 101;

int Ac, Aj;
int C[MAX_N], D[MAX_N];
int J[MAX_N], K[MAX_N];

int solve(){
    if (Ac != 2 && Aj != 2) return 2;
    if (Ac == 2){
        if (C[0] > C[1]){
            swap(C[0], C[1]);
            swap(D[0], D[1]);
        }
        if (D[1] <= C[0]+720) return 2;
        if (D[0]+1440 <= C[1]+720) return 2;
    }
    else if (Aj == 2){
        if (J[0] > J[1]){
            swap(J[0], J[1]);
            swap(K[0], K[1]);
        }
        if (K[1] <= J[0]+720) return 2;
        if (K[0]+1440 <= J[1]+720) return 2;
    }
    return 4;
}

int main(){
    freopen("/Users/eajoy/Downloads/B-small-attempt0.in", "r", stdin);
    freopen("/Users/eajoy/Downloads/B-small-attempt0.out", "w", stdout);
    int TEST;
    scanf("%d", &TEST);
    for (int CASE = 1; CASE <= TEST; ++CASE){
        scanf("%d%d", &Ac, &Aj);
        for (int i = 0; i < Ac; ++i) scanf("%d%d", C+i, D+i);
        for (int i = 0; i < Aj; ++i) scanf("%d%d", J+i, K+i);
        int ans = solve();
        printf("Case #%d: %d\n", CASE, ans);
    }
    return 0;
}
