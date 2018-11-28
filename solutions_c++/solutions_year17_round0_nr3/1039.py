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

ll solve(ll n, ll k)
{
    map<ll, ll> cnt;
    ll len = n;
    cnt[len] = 1;
    ll p = 1;
    for (;;)
    {
        if (p >= k) break;
        k -= p;
        p <<= 1;
        map<ll, ll> tmp;
        len -= 1;
        tmp[len/2] += cnt[len+1];
        tmp[(len+1)/2] += cnt[len+1];
        len -= 1;
        tmp[len/2] += cnt[len+1];
        tmp[(len+1)/2] += cnt[len+1];
        
        cnt = tmp;
        len += 1;
        len = (len+1)/2;
    }
    if (k <= cnt[len]) return len-1;
    return len-2;
    
}

int main()
{
    ios::sync_with_stdio(false);    cin.tie(0);
    int T;  cin >> T;
    repn(kase, T)
    {
        ll n, k;    cin >> n >> k;
        auto ret = solve(n, k);
        cout << "Case #" << kase << ": " << (ret+1)/2 << " " << (ret)/2 << newline;
    }
}
