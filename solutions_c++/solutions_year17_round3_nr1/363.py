#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <cstring>
#include <numeric>
#include <algorithm>
#include <functional>
#include <array>
#include <map>
#include <queue>
#include <limits.h>
#include <set>
#include <stack>
#include <random>
#include <complex>
#include <unordered_map>
#include <nmmintrin.h>
#include <chrono>
#define rep(i,s,n) for(int i = (s); (n) > i; i++)
#define REP(i,n) rep(i,0,n)
#define RANGE(x,a,b) ((a) <= (x) && (x) <= (b))
#define DUPLE(a,b,c,d) (RANGE(a,c,d) || RANGE(b,c,d) || RANGE(c,a,b) || RANGE(d,a,b))
#define INCLU(a,b,c,d) (RANGE(a,c,d) && (b,c,d))
#define PW(x) ((x)*(x))
#define ALL(x) (x).begin(), (x).end()
#define MODU 1000000007
#define bitcheck(a,b)   ((a >> b) & 1)
#define bitset(a,b)      ( a |= (1 << b))
#define bitunset(a,b)    (a &= ~(1 << b))
#define MP(a,b) make_pair((a),(b))
#define Manh(a,b) (abs((a).first-(b).first) + abs((a).second - ((b).second))
#define pritnf printf
#define scnaf scanf
#define itn int
#define PI 3.141592653589
#ifdef _MSC_VER
#define __builtin_popcount _mm_popcnt_u32
#define __builtin_popcountll _mm_popcnt_u64
#endif
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
ll gcd(ll a, ll b) {
	if (b == 0) return a;
	return gcd(b, a%b);
}
template<typename A, size_t N, typename T>
void Fill(A(&array)[N], const T &val) {
	std::fill((T*)array, (T*)(array + N), val);
}


signed main() {
	int t;
	scnaf("%d", &t);
	REP(cc, t) {
		int n, k;
		scanf("%d %d", &n, &k);

		ll dp[1001][1001];
		vector<pll> sz(n);
		REP(i, n) {
			scanf("%lld %lld", &sz[i].first, &sz[i].second);
		}
		Fill(dp, -1);

		sort(ALL(sz), greater<pll>());
		function<ll(int,int)> dfs = [&](int cur, int cou) {
			if (dp[cur][cou] != -1) return dp[cur][cou];
			if (cou == k) return (ll)0;
			if (cur == n) return (ll)0;
			ll ret = -1;

			if (dfs(cur + 1, cou) != -1)
				ret = max(ret, dfs(cur + 1, cou));

			ll ns = (ll)sz[cur].first*sz[cur].first + 2* (ll)sz[cur].second*sz[cur].first;
			if (cou != 0) 
				ns -= sz[cur].first*sz[cur].first;

			if(dfs(cur + 1, cou + 1) != -1)
				ret = max(ret,  ns + dfs(cur + 1, cou + 1));

			return dp[cur][cou] = ret;
		};

		printf("Case #%d: %.8lf\n",cc+1,  PI*(double)dfs(0, 0));

	}

	return 0;
}