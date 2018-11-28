#include <bits/stdc++.h>

using namespace std;

int hd, ad, hk, ak, b, d;

int dp[101][101][101][101];
int hasvis[101][101][101][101];

int solve(int mh, int oh, int ma, int oa) {
    if (mh <= 0) {
        return INT_MAX / 2;
    }
    if (oh <= 0) {
        return 0;
    }
    if (ma >= oh) {
        return 1;
    }
    if (dp[mh][oh][ma][oa] != -1) {
        return dp[mh][oh][ma][oa];
    }
    if (hasvis[mh][oh][ma][oa]) {
        return INT_MAX / 2;
    }
    hasvis[mh][oh][ma][oa] = true;
    /*
    if (ma == 0 && oa == 0) {
        return dp[mh][oh][ma][oa] = solve(mh, oh, b, 0) + 1;
    }
    if (ma == 0) {
        return dp[mh][oh][ma][oa] = solve(mh-oa, oh, b, oa);
    }
    if (oa == 0) {
        return dp[mh][oh][ma][oa] = solve(, <#int oh#>, <#int ma#>, <#int oa#>);
    }*/
    int ans = solve(mh - oa, oh - ma, ma, oa);
    int noa = max(0, oa - d);
    ans = min(ans, solve(mh - noa, oh, ma, noa));
    ans = min(ans, solve(mh - oa, oh, ma + b, oa));
    ans = min(ans, solve(hd - oa, oh, ma, oa));
    
    return dp[mh][oh][ma][oa] = ans + 1;
}

int main(int argc, const char * argv[]) {
    freopen("/Inputs/GC2017/in.txt", "r", stdin);
    freopen("/Inputs/GC2017/out.txt", "w", stdout);
    
    int t;
    scanf("%d", &t);
    for (int c = 1; c <= t; c++) {
        scanf("%d%d%d%d%d%d", &hd, &ad, &hk, &ak, &b, &d);
        memset(dp, -1, sizeof(dp));
        memset(hasvis, 0, sizeof(hasvis));
        int sol = solve(hd, hk, ad, ak);
        if (sol >= INT_MAX / 2) {
            printf("Case #%d: IMPOSSIBLE\n", c);
            continue;
        }
        printf("Case #%d: %d\n", c, sol);
    }
    return 0;
}
