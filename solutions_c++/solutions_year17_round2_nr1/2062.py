#if 0
#if 0
#include<iostream>
using namespace std;
int main()
{
	int t;
	cin >> t;
	for (int i = 0; i<t; i++)
	{
		double d, n, a[2][2000];
		cin >> d >> n;
		for (int j = 0; j<n; j++)
			cin >> a[0][j] >> a[1][j];
		double min = -1;
		for (int j = 0; j<n; j++)
		if ((d - a[0][j]) / a[1][j] > min)
			min = (d - a[0][j]) / a[1][j];
		cout << "Case #" << i + 1 <<":" <<" "<<d / min << endl;
	}
	return 0;
}
#endif
#include <iostream>
#include <vector>
using namespace std;

int main() {
	int t = 0;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		double d = 0;
		int n = 0;
		cin >> d >> n;
		vector<double> k(n, 0);
		vector<double> s(n, 0);
		double max_t = 0;
		for (int j = 0; j < n; ++j) {
			cin >> k[j] >> s[j];
			double len = d - k[j];
			if (len / s[j] > max_t) {
				max_t = len / s[j];
			}
		}
		cout << "Case #" << i + 1 << ": " << d / max_t << endl;
	}
	return 0;
}
#endif
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
#ifdef _MSC_VER
#define __builtin_popcount _mm_popcnt_u32
#define __builtin_popcountll _mm_popcnt_u64
#endif
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef long double __float128;
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
	cin >> t;
	REP(cc, t+1) {
		int n, d;
		cin >> d >> n;

		vector<__float128> tt(n);

		REP(i, n) {
			int k, s;
			cin >> k >> s;

			tt[i] = (__float128)(d - k) / s;
		}
		sort(ALL(tt), greater<__float128>());
		printf("Case #%d: %lf\n", cc + 1, (double)((__float128)d / tt[0]));
	}


	return 0;
}