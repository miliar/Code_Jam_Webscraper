#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
//#include <regex>

/* g++ -g -std=c++0x */
/* g++ -g -std=c++11 */

using namespace std;

// std::ios::sync_with_stdio(false);

// freopen("input.txt", "rt", stdin);
// freopen("output.txt", "wt", stdout);

#define ALL(c)          (c).begin(), (c).end()
#define ALLR(c)         (c).rbegin(), (c).rend()
#define FOR(i,a,b)      for (int i=(a); i < (b); ++i)
#define FORR(i,a,b)     for (int i=(a); i > (b); --i)
#define FOR_ALL(i,c)    for (__typeof((c).begin()) i=(c).begin();   \
                             i != (c).end(); ++i)
#define FOR_ALLR(i,c)   for (__typeof((c).rbegin()) i=(c).rbegin(); \
                             i != (c).rend(); ++i)
#define SZ(array)       (sizeof(array)/sizeof(array[0]))
#define lc(x)           (x<<1)     /* 2*x */
#define rc(x)           (x<<1 | 1) /* 2*x+1 */
#define lowbit(x)       (x & (-x)) /* 0b10100 -> 0b100 */

typedef long long       LL;
typedef map<int,int>    MII;
typedef pair<int,int>   PII;
typedef set<int>        SI;
typedef vector<bool>    VB;
typedef vector<double>  VD;
typedef vector<int>     VI;
typedef vector<string>  VS;

/* check if a key is in container C */
template <class C>
inline bool in_(const typename C::key_type& k, const C& A)
{ return A.find(k) != A.end(); }
inline bool in_(const string& s, const string& S)
{ return S.find(s) != string::npos; }

map<int,LL> dp[2][3];

int main()
{
#ifndef ONLINE_JUDGE
    freopen("foo", "rt", stdin);
#endif
    int T,tc = 1; cin >> T;
    while (T--) {
        LL N; cin >> N;
        VI A; LL n = N;
        while (n) {
            A.push_back(n%10);
            n /= 10;
        }
        reverse(ALL(A));
        int cur,nxt; cur = 0; nxt = 1;
        FOR(i,0,2) FOR(j,0,3)
            dp[i][j].clear();
        dp[cur][1][0] = 0;
        LL ans = 0;
        FOR(i,0,A.size()) {
            FOR(j,0,3)
                dp[nxt][j].clear();
            FOR(j,0,3) FOR_ALL(x,dp[cur][j]) {
                const int d = x->first;
                const LL v = x->second;
                FOR(dd,0,10) {
                    if (i == 0 && dd == 0)
                        continue;
                    if (dd >= d) {
                        const LL vv = v*10 + dd;
                        if (vv <= N) {
                            int k = j;
                            if (j == 1) {
                                if (dd < A[i])
                                    k = 0;
                                if (dd > A[i])
                                    k = 2;
                            }
                            dp[nxt][k][dd] = max(dp[nxt][k][dd],vv);
                            ans = max(ans,dp[nxt][k][dd]);
                        }
                    }
                }
            }
            swap(cur,nxt);
        }
        printf("Case #%d: %lld\n",tc++,ans);
    }
    return 0;
}
