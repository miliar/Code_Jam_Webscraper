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
		double unit;
		scnaf("%lf" , &unit);
		vector<double> core(n+1);
		REP(i, n) {
			scanf("%lf", &core[i]);
		}
		core[n] = 1;

		sort(ALL(core));
		double ans = 1;

		REP(i, n) {
			double sa = core[i + 1] - core[i];
			sa *= i+1;
			if (unit <= sa) {
				ans *= pow((core[i] + unit/(i+1)), i+1);
				unit = 0;
			}
			else unit -= sa;

			if (unit == 0) {
				rep(j, i + 1, n) {
					ans *= core[j];
				}
				break;
			}
		}

		printf("Case #%d: %.8lf\n",cc+1,  ans);

	}

	return 0;
}