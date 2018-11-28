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

const int maxn = 30;
char G[maxn][maxn];

int main()
{
#ifndef ONLINE_JUDGE
    freopen("foo", "rt", stdin);
#endif
    int tc = 1, T; cin >> T;
    while (T--) {
        int R,C; cin >> R >> C;
        FOR(i,0,R) {
            string s; cin >> s;
            FOR(j,0,C) 
                G[i][j] = s[j];
        }
        FOR(i,0,R) FOR(j,0,C) if (G[i][j] != '?') {
            const char ch = G[i][j];
            for (int k = j-1; k >= 0 && G[i][k] == '?'; k--)
                G[i][k] = ch;
            for (int k = j+1; k < C && G[i][k] == '?'; k++)
                G[i][k] = ch;
        }
        FOR(i,0,R) FOR(j,0,C) if (G[i][j] != '?') {
            const char ch = G[i][j];
            for (int k = i-1; k >= 0 && G[k][j] == '?'; k--)
                G[k][j] = ch;
            for (int k = i+1; k < R && G[k][j] == '?'; k++)
                G[k][j] = ch;
        }
        printf("Case #%d:\n",tc++);
        FOR(i,0,R) {
            FOR(j,0,C)
                printf("%c",G[i][j]);
            printf("\n");
        }
    }
    return 0;
}
