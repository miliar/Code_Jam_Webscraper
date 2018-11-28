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
        ll n, k; scanf("%lld%lld", &n, &k);
        ll a = 0LL;
        ll last = -1LL;
        priority_queue<pr> pq;
        pq.push(pr(n, 1LL)); // 길이 n짜리 1개 seg
        while (a < k) {
            pr t = pq.top(); pq.pop();
            while ((!pq.empty()) && (t.first == pq.top().first)) {
                t.second += pq.top().second;
                pq.pop();
            }
            if (t.first % 2LL) {
                if (t.first > 1LL) {
                    pq.push(pr(t.first/2LL, t.second * 2LL));
                }
            } else {
                pq.push(pr(t.first/2LL, t.second));
                pq.push(pr(t.first/2LL-1LL, t.second));
            }
            last = t.first;
            a += t.second;
        }
        last--;
        printf("Case #%d: %lld %lld\n", TT-T, last - last/2LL, last/2LL);
    }
/*----------------------------------------------------------------------------*/
#ifdef MICRO_LOCAL
    timer_end = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed_seconds = timer_end - timer_start;
    printf("\nElapsed time: %.5lfms\n", elapsed_seconds.count()*1000.);
#endif
    return 0;
}
