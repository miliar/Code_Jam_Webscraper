#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:10034217728")
#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <utility>
#include <ctime>
#include <string>
#include <sstream>
#include <queue>
#include <cstring>
#include <cmath>

using namespace std;
typedef long long ll;
typedef long double ld;
#define ZERO(x) memset((x), 0, sizeof(x))
#define NEGATE(x) memset((x), 255, sizeof(x))
#define mp make_pair
#define mt(a, b, c) mp(a, mp(b, c))

ll n, k;

map<ll, ll> M;

bool ismin = 0;

ll minmax(ll a, ll b) {
	if (ismin) return min(a, b);
	return max(a, b);
}

ll f_min(ll m, ll n) {
	if (M.count(n)) return M[n];
	ll g = n - 1;
	ll L = g / 2;
	ll R = g - L;
	ll pos = minmax(L, R);
	if (pos < m) return 0; //проверить условие!
	return M[n] = f_min(m, L) + f_min(m, R) + 1;
}

bool check(ll m) {
	M.clear();
	return f_min(m, n) >= k;
}

ll find_binary() {
	ll l = 0, r = 2e18;
	while (r - l > 1) {
		ll m = (l + r) / 2;
		if (check(m)) {
			l = m;
		}
		else {
			r = m;
		}
	}
	return l;
}

int main()
{
#ifdef XXX
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int T;
	cin >> T;
	for (int q = 0; q < T; q++) {
		cin >> n >> k;
		printf("Case #%d: ", q + 1);
		ismin = 0;
		printf("%lld ", find_binary());
		ismin = 1;
		printf("%lld ", find_binary());
		printf("\n");
	}

	return 0;
}