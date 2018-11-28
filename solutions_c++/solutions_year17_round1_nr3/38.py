#include <functional>
#include <iostream>
#include <deque>
#include <set>
#include <cstring>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <map>
#include <cmath>
#include <string>

using namespace std;

#define ll long long

ll Hd, Ad, Hk, Ak, B, D;
int mem[101][101][101][101];


int solve(int hd, int hk, int ad, int ak) {
    if (hk <= 0) return 0;
    if (hd <= 0) return -(1<<30);
    int &ans = mem[hd][hk][ad][ak];
    if (ans != -1) return ans;
    ans = -(1<<30);

    int tans = 1<<30;
    if (D > 0) {
        int t = solve(hd - max(0LL, (ak - D)), hk, ad, max(0LL, ak - D));
        if (t >= 0 && t + 1 < tans) {
            tans = t + 1;
        }
    }

    if (B > 0) {
        int t = solve(hd - ak, hk, min(100LL, ad + B), ak);
        if (t >= 0 && t + 1 < tans) {
            tans = t + 1;
        }
    }

    // cure 
    int t = solve(Hd - ak, hk, ad, ak);
    if (t >= 0 && t + 1 < tans) {
        tans = t + 1;
    }

    t = solve(hd - ak, hk - ad, ad, ak);
    if (t >= 0 && t + 1 < tans) {
        tans = t + 1;
    }
    
    if (tans == 1<<30) {
        tans = -tans;
    }
    //printf("%d %d %d %d gives %d\n", hd, hk, ad, ak, tans);
    return ans = tans;
    
}

int solveEasy() {
    memset(mem,-1,sizeof(mem));
    return solve(Hd, Hk, Ad, Ak);
}

int main() {
    int T;
    cin>>T;
    for (int t = 1; t <= T; ++t) {
        cin>>Hd>>Ad>>Hk>>Ak>>B>>D;
        
        int ans = solveEasy();

        if (ans < 0) {
            printf("Case #%d: IMPOSSIBLE\n", t);
        } else {
            printf("Case #%d: %d\n", t, ans);
        }
    }
}

