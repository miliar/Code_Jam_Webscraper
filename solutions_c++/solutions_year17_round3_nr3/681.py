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
        int n,k; scanf("%d%d", &n, &k);
        double unit; scanf("%lf", &unit);
        double prob[55];
        prob[n] = 1.0;
        REP(i,0,n) scanf("%lf", prob+i);
        sort(prob, prob+n);
        REP(i,0,n) {
            if (unit >= (i+1) * (prob[i+1] - prob[i])) {
                unit -= (i+1) * (prob[i+1] - prob[i]);
                for (int j=0; j<=i; ++j) {
                    prob[j] = prob[i+1];
                }
            } else {
                double e = unit / (i+1);
                for (int j=0; j<=i; ++j) {
                    prob[j] += e;
                }
                break;
            }
        }
        double ans = 1.0;
        REP(i,0,n) {
            ans *= prob[i];
        }
        printf("Case #%d: %.8lf\n", TT-T, ans);
    }
/*----------------------------------------------------------------------------*/
#ifdef MICRO_LOCAL
    timer_end = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed_seconds = timer_end - timer_start;
    printf("\nElapsed time: %.5lfms\n", elapsed_seconds.count()*1000.);
#endif
    return 0;
}
