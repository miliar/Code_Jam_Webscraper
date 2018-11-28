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
        int d, n; scanf("%d%d", &d, &n); // destination, number of other horses
        int k, s; // initial position, maximum speed
        double ans = 0.0;
        REP(i,0,n) {
            scanf("%d%d", &k, &s);
            double t = (d - k) / (double)s;
            ans = max(t, ans);
        }
        printf("Case #%d: %lf\n", TT-T, d/ans);
    }
/*----------------------------------------------------------------------------*/
#ifdef MICRO_LOCAL
    timer_end = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed_seconds = timer_end - timer_start;
    printf("\nElapsed time: %.5lfms\n", elapsed_seconds.count()*1000.);
#endif
    return 0;
}
