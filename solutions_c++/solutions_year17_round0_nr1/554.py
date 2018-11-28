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
	char line[1001];

	int TC;
	scanf("%d", &TC);
	FOR(T, 1, TC)
	{
		int K; scanf("%s%d", line, &K);
		int len = strlen(line), ans = 0;
		FOR(i, 0, len - K)if (line[i] == '-') {
			++ans;
			rep(j, K)line[i + j] = line[i + j] == '+' ? '-' : '+';
		}
		if (!strchr(line, '-'))
			printf("Case #%d: %d\n", T, ans);
		else printf("Case #%d: IMPOSSIBLE\n", T);
	}

	return 0;
}