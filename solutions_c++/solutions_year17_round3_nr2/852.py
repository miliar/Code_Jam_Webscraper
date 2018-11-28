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
        int Ac, Aj; scanf("%d%d", &Ac, &Aj);
        pr cameron[101], jamie[101];
        REP(i,0,Ac) scanf("%d%d", &cameron[i].first, &cameron[i].second);
        REP(i,0,Aj) scanf("%d%d", &jamie[i].first, &jamie[i].second);
        sort(cameron, cameron+Ac);
        sort(jamie, jamie+Aj);
        int ans = -1;
        if ((Ac == 0 && Aj == 1) || (Ac == 1 && Aj == 0)) ans = 2;
        else if (Ac == 1 && Aj == 1) {
            ans = 2;
        }
        else if (Ac == 2) {
            if (cameron[1].second - cameron[0].first <= 720 || cameron[1].first - cameron[0].second >= 720) {
                ans = 2;
            } else {
                ans = 4;
            }
        }
        else if (Aj == 2) {
            if (jamie[1].second - jamie[0].first <= 720 || jamie[1].first - jamie[0].second >= 720) {
                ans = 2;
            } else {
                ans = 4;
            }
        }

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
