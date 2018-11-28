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
        int n, p; scanf("%d%d", &n, &p);
        int r[51], q[51][51];
        vector<pr> s[51];
        REP(i,0,n) scanf("%d", r+i);
        REP(i,0,n) {
            REP(j,0,p) {
                scanf("%d", &q[i][j]); // i ingredients, j packages
                double t1 = q[i][j] / (double)r[i] / 1.1;
                double t2 = q[i][j] / (double)r[i] / 0.9;
                int l = t1, u = t2;
                if (fabs((double)l - t1) > 1e-7) {
                    l++;
                }
                if ((double)u + 1.0 - t2 < 1e-7) {
                    u++;
                }
                if (l <= u) {
                    s[i].emplace_back(pr(l, u));
                }
            }
        }
        REP(i,0,n) {
            sort(s[i].begin(), s[i].end());
        }
        int ans = 0;
        bool used[55][55] = {{false, }, };
        if (n == 1) {
            ans = s[0].size();
        } else {
            int sz0 = s[0].size();
            int sz1 = s[1].size();
            REP(i,0,sz0) {
                REP(j,0,sz1) {
                    if (used[1][j] == true) continue;
                    if (!(s[1][j].second < s[0][i].first || s[0][i].second < s[1][j].first)) {
                        used[0][i] = used[1][j] = true;
                        ans++;
                        break;
                    }
                }
            }
        }
        /*
        puts("----");
        REP(i,0,n) {
            for (auto it: s[i]) {
                printf("%d %d\n", it.first, it.second);
            }
            puts("");
        }
        puts("----");
        */
        printf("Case #%d: %d\n", TT-T, ans);
    }
/*----------------------------------------------------------------------------*/
#ifdef MICRO_LOCAL
    timer_end = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed_seconds = timer_end - timer_start;
    printf("\nElapsed time: %.5lfms\n", elapsed_seconds.count()*1000.);
#endif
    return 0;
}
