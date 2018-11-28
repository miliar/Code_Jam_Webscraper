#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <memory.h>
#include <string>
#include <sstream>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef pair<PII,PII> PIIII;

#define MP make_pair
#define PB push_back
#define FF first
#define SS second

#define FORN(i, n) for (int i = 0; i <  (int)(n); i++)
#define FOR1(i, n) for (int i = 1; i <= (int)(n); i++)
#define FORD(i, n) for (int i = (int)(n) - 1; i >= 0; i--)

#define DEBUG(X) { cout << #X << " = " << (X) << endl; }
#define PR0(A,n) { cout << #A << " = "; FORN(_,n) cout << A[_] << ' '; cout << endl; }

#define MOD 1000000007
#define INF 2000000000

int GLL(LL& x) {
    return scanf("%lld", &x);
}

int GI(int& x) {
    return scanf("%d", &x);
}

int T;

int n, p;

const int MAXN = 105;
int dp[MAXN][MAXN][MAXN];

const int MAXP = 4;
int cnt[MAXP];

int rec(int r1, int r2, int r3) {
    if (dp[r1][r2][r3] != -1) return dp[r1][r2][r3];

    int rtot = (r1 * 1 + r2 * 2 + r3 * 3) % p;

    int& res = dp[r1][r2][r3]; res = 0;

    if (r1 > 0) {
        res = max(res, ((rtot + p - 1) % p == 0) + rec(r1-1, r2, r3));
    }
    if (r2 > 0) {
        res = max(res, ((rtot + p - 2) % p == 0) + rec(r1, r2-1, r3));
    }
    if (r3 > 0) {
        res = max(res, ((rtot + p - 3) % p == 0) + rec(r1, r2, r3-1));
    }

    return res;
}

void solve() {
    GI(n);
    GI(p);

    memset(cnt, 0, sizeof cnt);

    int res = 0; int g;

    FOR1(i, n) {
        GI(g);
        cnt[g % p]++;
    }

    res = cnt[0];

    memset(dp, -1, sizeof dp);
    dp[0][0][0] = 0;

    res += rec(cnt[1], cnt[2], cnt[3]);

    cout << res << "\n";
}

int main() {
    GI(T);

    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        solve();
    }
    
    return 0;
}
