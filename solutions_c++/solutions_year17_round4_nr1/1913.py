#include <iostream>
#include <string.h>
#include <cstdio>
#include <set>
#include <vector>
#include <map>
#include <cmath>
using namespace std;

typedef long long lint;
int N, P;
int C[4];
const int INF = 1 << 30;

int check(int cur, int res) {
    if (cur != -INF) {
        return max(cur + 1, res);
    }
    return res;
}

int dp3[110][110];
int dp[110][110][110];

int rec3(int c1, int c2) {
    if (c1 == 0 && c2 == 0) {
        return 0;
    }
    if (c1 == 0) {
        return (c2 + 2) / 3;
    }
    if (c2 == 0) {
        return (c1 + 2) / 3;
    }
    if (c1 + c2 < 3) {
        return 1;
    }
    if (dp3[c1][c2] != -1) {
        return dp3[c1][c2];
    }
    int res = -INF;
    
    // Sum = 3
    // 1+1+1
    if (c1 >= 3) {
        int cur = rec3(c1 - 3, c2);
        res = check(cur, res);
    }
    // 1+2
    if (c1 >= 1 && c2 >= 1) {
        int cur = rec3(c1 - 1, c2 - 1);
        res = check(cur, res);
    }
    
    return dp3[c1][c2] = res;
}


int rec4(int c1, int c2, int c3) {
    if (c1 == 0 && c2 == 0 && c3 == 0) {
        return 0;
    }
    if (dp[c1][c2][c3] != -1) {
        return dp[c1][c2][c3];
    }
    int res = INF;
    // 1+1+1+1
    if (c1 >= 4) {
        int cur = rec4(c1 - 4, c2, c3);
        res = check(cur, res);
    }
    // 1+1+2
    if (c1 >= 2 && c2 >= 1) {
        int cur = rec4(c1 - 2, c2 - 1, c3);
        res = check(cur, res);
    }
    // 1+3
    if (c1 >= 1 && c3 >= 1) {
        int cur = rec4(c1 - 1, c2, c3 - 1);
        res = check(cur, res);
    }
    // 2+2
    if (c2 >= 2) {
        int cur = rec4(c1, c2 - 2, c3);
        res = check(cur, res);
    }
    
    
    
    // Sum = 3
    // 3
    if (c3 >= 1) {
        int cur = rec4(c1, c2, c3 - 1);
        res = check(cur, res);
    }
    
    // 1+1+1
    if (c1 >= 3) {
        int cur = rec4(c1 - 3, c2, c3);
        res = check(cur, res);
    }
    // 1+2
    if (c1 >= 1 && c2 >= 1) {
        int cur = rec4(c1 - 1, c2 - 1, c3);
        res = check(cur, res);
    }
    
    // Sum = 2
    // 1+1
    if (c1 >= 2) {
        int cur = rec4(c1 - 2, c2, c3);
        res = check(cur, res);
    }
    // 2
    if (c2 >= 1) {
        int cur = rec4(c1, c2 - 1, c3);
        res = check(cur, res);
    }
    
    // Sum=1
    // 1
    if (c1 >= 1) {
        int cur = rec4(c1 - 1, c2, c3);
        res = check(cur, res);
    }

    
    
    
    
    return dp[c1][c2][c3] = res;
}

int solve2() {
    return (C[1] + 1) / 2 + C[0];
}

int solve3() {
    memset(dp3, -1, sizeof(dp3));
    int res = rec3(C[1], C[2]);
    res += C[0];
    return res;
}

int solve4() {
    memset(dp, -1, sizeof(dp));
    return rec4(C[1], C[2], C[3]) + C[0];
}


void solve(int tst) {
    cin >> N >> P;
    
    C[0] = C[1] = C[2] = C[3] = 0;
    for (int i = 0; i < N; ++i) {
        int g;
        cin >> g;
        C[g % P]++;
    }
    
    int ans = 0;
    if (P == 2) {
        ans = solve2();
    } else if (P == 3) {
        ans = solve3();
    } else if (P == 4) {
        ans = solve4();
    }
    
    printf("Case #%d: %d\n", tst, ans);
}

int main() {
    freopen("/Users/ryuzmukhametov/gcj/input.txt", "r", stdin);
    freopen("/Users/ryuzmukhametov/gcj/output.txt", "w", stdout);
    int tst;
    cin >> tst;
    for (int i = 1; i <= tst; ++i) {
        solve(i);
    }
    return 0;
}
