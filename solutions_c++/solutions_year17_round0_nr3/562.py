//TAG : 
#include<bits/stdc++.h>
using namespace std;
#define rep(i,n)	for(int (i)=0;(i)<(n);(i)++)
#define repd(i,n)	for(int (i)=(n)-1;(i)>=0;(i)--)
#define REP(i,j,n)  for(int (i)=(j),_n=(n); (i) < _n; (i)++)
#define FOR(i,a,b)  for(int _b=(b), (i)=(a); (i) <= _b; (i)++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define CLEAR(x) memset((x),0,sizeof(x))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define X first
#define Y second
#define MP make_pair
#define MT make_tuple
#define EPS 	(1e-9)
typedef pair<int, int>	pii;
typedef vector<int>		vi;
typedef unsigned int	uint;
typedef long long		ll;
typedef unsigned long long	ull;
template<typename T> void check_max(T& a, T b) { if (a < b) a = b; }
template<typename T> void check_min(T& a, T b) { if (a > b) a = b; }
#ifdef _MSC_VER
#include "builtin_gcc_msvc.h"
#define gets	gets_s
#else
#define popcnt(x)	__builtin_popcount(x)
#define ctz(x)		__builtin_ctz(x)
#define clz(x)		__builtin_clz(x)
#define popcntll(x)	__builtin_popcountll(x)
#define ctzll(x)	__builtin_ctzll(x)
#define clzll(x)	__builtin_clzll(x)
#endif

int main()
{
	map<ll, ll> table;

	int TC;
	scanf("%d", &TC);
	FOR(T, 1, TC)
	{
		ll n, k; scanf("%lld%lld", &n, &k);
		table.clear();
		table[-n] = 1;
		ll al = 0, ar = 0;
		while (k > 0) {
			auto it = table.begin();
			ll x = -(it->X), y = it->Y;
			ll l = (x - 1) / 2, r = x / 2;
			if (l)table[-l] += y;
			if (r)table[-r] += y;
			k -= y;
			if (k <= 0) {
				al = l, ar = r; break;
			}
			table.erase(it);
		}
		printf("Case #%d: %lld %lld\n", T, ar, al);
	}

	return 0;
}