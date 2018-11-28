#include <bits/stdc++.h>

using namespace std;

#ifdef ACMTUYO
struct RTC{~RTC(){cerr << "Time: " << clock() * 1.0 / CLOCKS_PER_SEC <<" seconds\n";}} runtimecount;
#define DBG(X) cerr << #X << " = " << X << '\n';
#else
struct RTC{};
#define DBG(X)
#endif

#define fast_io() ios_base::sync_with_stdio(false)
#define mp make_pair
#define mt make_tuple
#define pb push_back
#define eb emplace_back
#define sz(x) ((int)(x).size())
#define all(c) (c).begin(),(c).end()
#define forn(i, n) for (int i = 0; i < (n); i++)
typedef long long int number;

int main() {
	int ntc;
	scanf("%d", &ntc);
	for (int tc = 1; tc <= ntc; tc++) {
		DBG(tc);
		number n, k;
		scanf("%lld %lld", &n, &k);
		map<number, number> cur;
		cur[n] = 1;
		number cnt = 0;
		number X = -1, Y;
		while (cnt < k) {
			assert(sz(cur) > 0);
			auto it = cur.end();
			it--;
			cur.erase(it);
			number len = it->first;
			number r = it->second;
			len--;
			Y = len >> 1LL;
			X = len - Y;
			cnt += r;
			if (X > 0) cur[X] += r;
			if (Y > 0) cur[Y] += r;
		}
		assert(X != -1);
		printf("Case #%d: %lld %lld\n", tc, X, Y);
	}
  return 0;
}
