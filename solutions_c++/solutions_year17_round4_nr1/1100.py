//TAG : 
#include<bits/stdc++.h>
using namespace std;
#define rep(i,n)	for(int (i)=0;(i)<(n);(i)++)
#define repd(i,n)	for(int (i)=(n)-1;(i)>=0;(i)--)
#define REP(i,j,n)  for(int (i)=(j),_n=(n);(i)<_n;(i)++)
#define FOR(i,a,b)  for(int _b=(b),(i)=(a);(i)<=_b;(i)++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(),(c).end()
#define SORT(c) sort(ALL(c))
#define CLEAR(x) memset((x),0,sizeof(x))
#define ff first
#define ss second
#define MP make_pair
#define EPS 	(1e-9)
typedef pair<int, int>	pii;
typedef vector<pii>	vii;
typedef vector<int>	vi;
typedef long long		ll;
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

const int MX = 100;
int cnt[5];
int dp[MX + 1][MX + 1][MX + 1];

int main()
{
	int TC;
	scanf("%d", &TC);
	FOR(T, 1, TC)
	{
		int n, P; scanf("%d%d", &n, &P);
		CLEAR(cnt);
		rep(i, n) {
			int j; scanf("%d", &j);
			++cnt[j%P];
		}
		CLEAR(dp);
		FOR(a1, 0, cnt[1])
			FOR(a2, 0, cnt[2])
			FOR(a3, 0, cnt[3]) {
			int sum = a1 + a2 * 2 + a3 * 3;
			bool fresh = sum%P == 0;
			if (a1 < cnt[1])check_max(dp[a1 + 1][a2][a3], dp[a1][a2][a3] + fresh);
			if (a2 < cnt[2])check_max(dp[a1][a2 + 1][a3], dp[a1][a2][a3] + fresh);
			if (a3 < cnt[3])check_max(dp[a1][a2][a3 + 1], dp[a1][a2][a3] + fresh);
		}
		int ans = cnt[0] + dp[cnt[1]][cnt[2]][cnt[3]];
		printf("Case #%d: %d\n", T, ans);
	}

	return 0;
}