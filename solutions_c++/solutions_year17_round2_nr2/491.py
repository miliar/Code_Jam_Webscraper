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

int main()
{
	pair<int, char> A[6];
	char line[1001];

	int TC;
	scanf("%d", &TC);
	FOR(T, 1, TC)
	{
		int N, R, O, Y, G, B, V;
		scanf("%d%d%d%d%d%d%d", &N, &R, &O, &Y, &G, &B, &V);
		// for small, O = G = V = 0
		A[0] = MP(R, 'R');
		A[1] = MP(Y, 'Y');
		A[2] = MP(B, 'B');
		sort(A, A + 3, [](auto a, auto b) {
			return a.ff > b.ff;
		});
		if (O || G || V) {
			printf("Case #%d: large\n", T);
		} else if (A[0].ff <= N / 2) {
			int q = N / A[0].ff, r = N%A[0].ff;
			int pos = 0;
			CLEAR(line);
			rep(i, A[0].ff) {
				line[pos] = A[0].ss;
				if (i < A[1].ff)line[pos + 1] = A[1].ss;
				pos += q + (i < r);
			}
			rep(i, N)if (!line[i])
				line[i] = A[2].ss;
			printf("Case #%d: %s\n", T, line);
		} else printf("Case #%d: IMPOSSIBLE\n", T);
	}

	return 0;
}