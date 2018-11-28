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

typedef pair<double, double> pdd;
int main()
{
	const int MX = 1001;
	pdd A[MX];

	int TC;
	scanf("%d", &TC);
	FOR(T, 1, TC)
	{
		int D, N; scanf("%d%d", &D, &N);
		rep(i, N)scanf("%lf%lf", &A[i].ff, &A[i].ss);
		double ans, l = 0, r = 1e20;
		rep(a, 100) {
			double mid = (l + r) / 2;
			bool ok = true;
			rep(i, N) {
				if (mid > A[i].ss) {
					double t = A[i].ff / (mid - A[i].ss);
					double y2 = A[i].ff + t*A[i].ss;
					if (y2 < D) { ok = false; break; }
				}
			}
			if (ok)ans = mid, l = mid;
			else r = mid;
		}
		printf("Case #%d: %.6lf\n", T, ans);
	}

	return 0;
}