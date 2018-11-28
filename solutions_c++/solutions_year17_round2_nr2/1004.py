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
typedef pair<int,int> pr;
#define REP(i,m,n) for (int i=(m); i<(n); ++i)
#define RREP(i,m,n) for (int i=(m)-1; i>=n; --i)

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
        // red orange(r+y) yellow green(y+b) blue violet(r+b)
        int n, r, o, y, g, b, v; scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
        // sum(r,o,y,g,b,v) == n
        // small: o = g = v = 0
        if (r * 2 <= n && y * 2 <= n && b * 2 <= n) {
            char ans[1002] = "";
            pr a[3];
            a[0] = pr(r, 'R');
            a[1] = pr(y, 'Y');
            a[2] = pr(b, 'B');
            sort(a, a+3, greater<pr>());
            a[0].first--;
            char last = a[0].second;
            ans[0] = last;
            REP(i,1,n) {
                sort(a, a+3, greater<pr>());
                int t = 0;
                if (last == a[0].second) {
                    t++;
                }
                last = a[t].second;
                a[t].first--;
                ans[i] = last;
            }
            if (ans[n-1] == ans[0]) {
                char t = ans[n-1];
                ans[n-1] = ans[n-2];
                ans[n-2] = t;
            }
            printf("Case #%d: %s\n", TT-T, ans);
        } else {
            printf("Case #%d: IMPOSSIBLE\n", TT-T);
        }
    }
/*----------------------------------------------------------------------------*/
#ifdef MICRO_LOCAL
    timer_end = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed_seconds = timer_end - timer_start;
    printf("\nElapsed time: %.5lfms\n", elapsed_seconds.count()*1000.);
#endif
    return 0;
}
