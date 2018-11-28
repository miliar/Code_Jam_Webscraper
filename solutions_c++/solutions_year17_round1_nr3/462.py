#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cctype>
#include <numeric>
#include <queue>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <iterator>
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define REP(i,n)   FOR(i,0,n)
#define ALL(x) (x).begin(), (x).end()
#define CLR(s) memset(s,0,sizeof(s))
#define PB push_back
#define ITER(v)      __typeof((v).begin())
#define FOREACH(i,v) for(ITER(v) i=(v).begin();i!=(v).end();i++)
using namespace std;
typedef long long LL;
typedef pair<int,int> pii;
typedef map<int,int> mii;
typedef vector<int> vi;
#define x first
#define y second

int hd_, ad, hk, ak, b, d;
int ans;

const int N = 102;
const LL INF = 1LL<<40;

LL dp[N][N][N][N];

LL go(int hd, int ad, int hk, int ak) {
    hd = max(hd, 0);
    ad = min(ad, 100);
    hk = max(hk, 0);
    ak = max(ak, 0);

    LL &ret = dp[hd][ad][hk][ak];
    if (ret != -1) return ret;
    if (hk == 0) return ret = 0;

    if (hd == 0) return ret = INF;

    ret = INF;

    ret = min(ret, go(hd - ak,                ad,     hk - ad, ak) + 1); // A
    ret = min(ret, go(hd - ak,                ad + b, hk,      ak) + 1); // B
    ret = min(ret, go(hd_ - ak,               ad,     hk,      ak) + 1); // C
    ret = min(ret, go(hd - max(0, (ak - d)),  ad,     hk,      ak - d) + 1); // D
    //printf("(%d %d %d %d) -> %lld\n", hd, ad, hk, ak, ret);
    return ret;
}

int main() {

    int T; scanf("%d", &T); FOE(ca, 1, T) {
        scanf("%d%d%d%d%d%d", &hd_, &ad, &hk, &ak, &b, &d);
        memset(dp, -1, sizeof(dp));
        LL ans = go(hd_, ad, hk, ak);
        if (ans == INF) {
            printf("Case #%d: IMPOSSIBLE\n", ca);
        } else {
            printf("Case #%d: %d\n", ca, int(ans));
        }
    }
    return 0;
}
