#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <bitset>
#include <cstdlib>
#include <cmath>
#include <set>
#include <list>
#include <deque>
#include <map>
#include <queue>
#include <fstream>
#include <cassert>
#include <unordered_map>
#include <unordered_set>
#include <cmath>
#include <sstream>
#include <time.h>
#include <complex>
#include <iomanip>
#include <tuple>

#define Max(a,b) ((a)>(b)?(a):(b))
#define Min(a,b) ((a)<(b)?(a):(b))
#define FOR(a,b,c) for (ll (a)=(b);(a)<(c);++(a))
#define FORN(a,b,c) for (ll (a)=(b);(a)<=(c);++(a))
#define DFOR(a,b,c) for (ll (a)=(b);(a)>=(c);--(a))
#define FORSQ(a,b,c) for (ll (a)=(b);(a)*(a)<=(c);++(a))
#define FORC(a,b,c) for (char (a)=(b);(a)<=(c);++(a))
#define FOREACH(a,b) for (auto &(a) : (b))
#define rep(i,n) FOR(i,0,n)
#define repn(i,n) FORN(i,1,n)
#define drep(i,n) DFOR(i,n-1,0)
#define drepn(i,n) DFOR(i,n,1)
#define MAX(a,b) a = Max(a,b)
#define MIN(a,b) a = Min(a,b)
#define SQR(x) ((LL)(x) * (x))
#define Reset(a,b) memset(a,b,sizeof(a))
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define all(v) v.begin(),v.end()
#define ALLA(arr,sz) arr,arr+sz
#define SIZE(v) (int)v.size()
#define SORT(v) sort(all(v))
#define REVERSE(v) reverse(ALL(v))
#define SORTA(arr,sz) sort(ALLA(arr,sz))
#define REVERSEA(arr,sz) reverse(ALLA(arr,sz))
#define PERMUTE next_permutation
#define TC(t) while(t--)
#define forever for(;;)
#define PINF 1000000000000
#define newline '\n'

#define test if(1)if(0)cerr
using namespace std;
using namespace std;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef pair<double,double> dd;
typedef pair<char,char> cc;
typedef vector<ii> vii;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<ll, ll> l4;

const int maxn = 60;

int r[maxn];
int q[maxn][maxn];
ii qq[maxn][maxn];
int ptr[maxn];
int n, p;
struct interval
{
    int l, r;
    bool operator<(const interval &R) const
    {
        return r < R.r;
    }
};
int solve();
int maxans;
int main()
{
    ios::sync_with_stdio(false);    cin.tie(0);
    int T;  cin >> T;
    repn(kase, T)
    {
        maxans = 0;
        cin >> n >> p;
        rep(i, n) cin >> r[i];
        rep(i, n) rep(j, p) cin >> q[i][j];
        rep(i, n) rep(j, p)
        {
            qq[i][j] = mp(ceil(q[i][j]/1.1/r[i]), floor(q[i][j]/0.9/r[i]));
            MAX(maxans, qq[i][j].second);
        }
        rep(i, n) sort(qq[i], qq[i]+p);
        cout << "Case #" << kase << ": " << solve() << newline;
    }
}

int solve()
{
    int ret = 0;
    Reset(ptr, 0);
    multiset<interval> s[60];
    repn(num, maxans)
    {
        rep(i, n)
        {
            while (ptr[i] < p && num >= qq[i][ptr[i]].first) s[i].insert((interval) {qq[i][ptr[i]].first, qq[i][ptr[i]].second}), ++ptr[i];
            while (!s[i].empty() && s[i].begin()->r < num) s[i].erase(s[i].begin());
        }
        bool work = true;
        while (work)
        {
            rep(i, n)
            {
                if (s[i].empty())
                {
                    work = false;   break;
                }
            }
            if (work)
            {
                ++ret;
                rep(i, n) s[i].erase(s[i].begin());
            }
        }
    }
    
    return ret;
}

