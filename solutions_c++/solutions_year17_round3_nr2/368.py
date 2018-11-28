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
	int n;
	scanf("%d", &n);
	REP(cc, n) {
		int c, j;
		scanf("%d %d", &c, &j);
		vector<pii> ac(c), aj(j);
		int sc[1441] = {};
		REP(i, c) {
			scanf("%d %d", &ac[i].first, &ac[i].second);
			rep(j, ac[i].first, ac[i].second)
				sc[j] = 1;
		}
		REP(i, j) {
			scanf("%d %d", &aj[i].first, &aj[i].second);
			rep(j, aj[i].first, aj[i].second)
				sc[j] = 2;
		}
		sort(ALL(ac));
		sort(ALL(aj));
		int dp[1440][721][2][2];
		Fill(dp, -1);

		function<int(int, int, int, int)> dfs = [&](int t1, int t2, int bef, int st) {
			int sum = t1 + t2;
			if (sum == 1440)
				return (st != bef ? 100000 : 0);

			if (dp[t1][t2][bef][st] != -1) return dp[t1][t2][bef][st];

			int ret = 100000;

			if (sc[sum] != 1 && t1 < 720) ret = min(ret, (bef != 1) + dfs(t1 + 1, t2, 1, st));
			if (sc[sum] != 2 && t2 < 720) ret = min(ret, (bef != 2) + dfs(t1, t2 + 1, 2, st));

			if (ret > 2000) ret = 100000;

			return dp[t1][t2][bef][st] = ret;
		};
		printf("Case #%d: %d\n",cc+1, min(dfs(0, 0, 2, 2), dfs(0, 0, 1, 1)));
	}
	return 0;
}