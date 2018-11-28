#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <set>
#include <queue>
#include <deque>
#include <string>
#include <map>
#include <functional>
#include <cassert>
#include <ctime>
#include <chrono>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> pr;
#define REP(i,m,n) for (int i=(m); i<(n); ++i)
#define RREP(i,m,n) for (int i=(m)-1; i>=n; --i)

pr ra[1000001];
int n;
const double PI = 3.1415926535897932;
ll cache[1001][1001];

ll dfs(int idx, int left, ll last) {
    if (idx == -1) {
        ll ret = 0LL;
        for (int i=0; i<=n-left; ++i) {
            ret = max(ret, ra[i].second + dfs(i, left-1, ra[i].first));
        }
        return ret;
    }
    if (cache[idx][left] != -1LL) return cache[idx][left];

    ll &ret = cache[idx][left];
    if (left == 0) {
        return last * last;
    }

    for (int i=idx+1; i<=n-left; ++i) {
        ret = max(ret, ra[i].second + dfs(i, left-1, ra[i].first));
    }
    return ret;
}

int main()
{
#ifdef MICRO_LOCAL
    freopen("in.put", "r", stdin);
    chrono::time_point<chrono::high_resolution_clock> timer_start, timer_end;
    timer_start = chrono::high_resolution_clock::now();
#endif
/*----------------------------------------------------------------------------*/
    int T, TT; scanf("%d", &T);
    TT = T;
    while (T--) {
        memset(cache, -1LL, sizeof(cache));
        int k; scanf("%d%d", &n, &k);
        REP(i,0,n) {
            scanf("%lld%lld", &ra[i].first, &ra[i].second);
            ra[i].second *= 2LL * ra[i].first;
        }
        sort(ra, ra+n);
        double Ma = dfs(-1, k, 0) * PI;
        printf("Case #%d: %.10lf\n", TT-T, Ma);
    }
/*----------------------------------------------------------------------------*/
#ifdef MICRO_LOCAL
    timer_end = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed_seconds = timer_end - timer_start;
    printf("\nElapsed time: %.5lfms\n", elapsed_seconds.count()*1000.);
#endif
    return 0;
}
