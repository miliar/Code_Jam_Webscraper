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
        ll n; scanf("%lld", &n);
        char s[20] = "", ans[20] = "";
        sprintf(s, "%lld", n);
        int len = strlen(s);
        bool smaller = false;
        ans[0] = s[0];
        REP(i,1,len) {
            if (s[i] >= ans[i-1]) {
                ans[i] = s[i];
            } else if (smaller == false) {
                ans[i-1]--;
                ans[i] = '9';
                smaller = true;
                RREP(j,i,1) {
                    if (ans[j] < ans[j-1]) {
                        ans[j] = '9';
                        ans[j-1]--;
                    } else {
                        break;
                    }
                }
            } else {
                ans[i] = '9';
            }
        }
        int t = 0;
        while (ans[t] == '0') t++;
        printf("Case #%d: %s\n", TT-T, ans+t);
    }
/*----------------------------------------------------------------------------*/
#ifdef MICRO_LOCAL
    timer_end = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed_seconds = timer_end - timer_start;
    printf("\nElapsed time: %.5lfms\n", elapsed_seconds.count()*1000.);
#endif
    return 0;
}
