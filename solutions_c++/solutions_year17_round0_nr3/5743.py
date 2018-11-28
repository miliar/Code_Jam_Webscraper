#include <bits/stdc++.h>

using namespace std;

#define sd(x) scanf("%d", &x)
#define boost ios_base::sync_with_stdio(false);
#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()
#define f first
#define s second
#define TRACE
#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1) {
  cerr << name << " : " << arg1 << endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args) {
  const char* comma = strchr(names + 1, ',');
  cerr.write(names, comma - names) << " : " << arg1<<" | ";
  __f(comma+1, args...);
}
#else
#define trace(...)
#endif

typedef pair <int, int> pii;
typedef long long ll;
typedef vector <vector <ll>> matrix;

const int mod = 1000000007;
const int inf = 50000000;
const int maxn = 100010;

ll n, k;

int main() {
	// freopen("C.in", "r", stdin);
	// freopen("o.txt", "w", stdout);
	int t, cn = 1;
	scanf("%d", &t);
	while (t--) {
		scanf("%lld %lld", &n, &k);
		if (k == 1) {
			printf("Case #%d: %lld %lld\n", cn++, n / 2, (n - 1) / 2);
			continue;
		}
		ll scnt = 1, uscnt = ((n ^ 1) & 1), mx = n / 2;
		ll mn = mx - 1;
		k -= 1;
		int b;
		for (b = 1; k > (1LL << b); b++) {
			if (n & (1LL << b)) {
				scnt += (1LL << b);
			}
			else {
				uscnt += (1LL << b);
			}
			k -= (1LL << b);
			mx /= 2;
			mn = mx - 1;
		}
		if (k > 0) {
			mx /= 2;
			mn = mx - 1;
		}
		// trace(b, k, scnt, uscnt, mx, mn);
		if (n & (1LL << b)) {
			if ((k <= (1LL << b) - uscnt)) {
				mn += 1;
			}
		}
		else {
			if (k > scnt) {
				mx -= 1;
			}
		}
		printf("Case #%d: %lld %lld\n", cn++, mx, mn);
	}
	return 0;
}