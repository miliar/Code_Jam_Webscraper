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
typedef long long LL;


int cnt[5];

int d[101][101][101];
int dp(int a, int b, int c)
{
    int &ret = d[a][b][c];
    if (ret == -1)
    {
        if (a == 0 && b == 0 && c == 0) return ret = 0;
        ret = 1;
        if (a >= 4) MAX(ret, dp(a-4, b, c)+1);
        if (b >= 2) MAX(ret, dp(a, b-2, c)+1);
        if (c >= 4) MAX(ret, dp(a, b, c-4)+1);
        if (a >= 1 && c >= 1) MAX(ret, dp(a-1, b, c-1)+1);
        if (b >= 1)
        {
            if (a >= 2) MAX(ret, dp(a-2, b-1, c)+1);
            if (c >= 2) MAX(ret, dp(a, b-1, c-2)+1);
        }
    }
    return ret;
}
int n, p;
int main()
{
    int T;  cin >> T;
    Reset(d, -1);
    repn(kase, T)
    {
        Reset(cnt, 0);
        cin >> n >> p;
        rep(i, n)
        {
            int a;  cin >> a;
            cnt[a%p] += 1;
        }
        int ans = 0;
        if (p == 2)
        {
            ans = cnt[0] + (cnt[1]+1)/2;
        }
        else if (p == 3)
        {
            ans = cnt[0];
            int tmp = min(cnt[1], cnt[2]);
            ans += tmp;
            repn(i, 2) cnt[i] -= tmp;
            ans += (cnt[1]+2)/3 + (cnt[2]+2)/3;
        }
        else
        {
            assert(p == 4);
            ans = cnt[0] + dp(cnt[1], cnt[2], cnt[3]);
        }
        
        cout << "Case #" << kase << ": " << ans << newline;
        
    }
}
