#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define fst first
#define snd second
#define sz(a) int((a).size())
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<ll> vll;
const int INF = 2000 * 1000 * 1000;
const ll LLINF = 1ll << 53;
template<class T> void relaxmax(T& r, T v) { r = max(r, v); }
template<class T> void relaxmin(T& r, T v) { r = min(r, v); }

const int MAXN = 20;
ll dp[MAXN][10][2];
char s[MAXN + 1];

ll solve(int n, int ne, bool strict) {
	if (n == 0) return strict ? -LLINF : 0;
	ll& r = dp[n][ne][strict];
	if (r != -1) return r;
	int d = min(ne, s[n - 1] - '0');
	ll ans = 0;
	do {
		relaxmax(ans, solve(n - 1, d, d > s[n - 1] - '0' || (d == s[n - 1] - '0' && strict)) * 10 + d);
		d = (d + 9) % 10;
	} while (d != s[n - 1] - '0' && d <= ne);
	return r = ans;
}

bool isincreasing(ll n) {
	ll p = 9;
	while (n > 0) {
		if (n % 10 > p) return false;
		p = n % 10;
		n /= 10;
	}
	return true;
}

ll test() {
	ll v = 0;
	for (int i = 0; s[i]; ++i)
		v = v * 10 + s[i] - '0';
	while (!isincreasing(v))
		v--;
	return v;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		for (int i = 0;  i < MAXN; ++i)
			for (int j = 0; j < 10; ++j)
				dp[i][j][0] = dp[i][j][1] = -1;
		scanf(" %s", s);
//		printf("%lld %lld\n", solve(strlen(s), 9, false), test());
//		assert(solve(strlen(s), 9, false) == test());
		printf("Case #%d: %lld\n", t, solve(strlen(s), 9, false));
//		printf("Case #%d: %lld\n", t, test());

	}
	return 0;
}
	
