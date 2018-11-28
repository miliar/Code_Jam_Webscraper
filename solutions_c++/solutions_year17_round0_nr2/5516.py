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

vector <int> dig;

void f(ll x) {
	dig.clear();
	while (x) {
		dig.pb(x % 10);
		x /= 10;
	}
	reverse(all(dig));
}

int main() {
	// freopen("B.in", "r", stdin);
	// freopen("o.txt", "w", stdout);
	int t, cn = 1;
	ll n;
	scanf("%d", &t);
	while (t--) {
		scanf("%lld", &n);
		f(n);
		int pos = -1;
		for (int i = 1; i < dig.size(); i++) {
			if (dig[i] < dig[i - 1]) {
				pos = i;
				break;
			}
		}
		if (pos == -1) {
			printf("Case #%d: %lld\n", cn++, n);
			continue;
		}
		int rep = 0;
		for (int i = pos - 1; i > 0; i--) {
			if (dig[i] - 1 >= dig[i - 1]) {
				rep = i;
				break;
			}
		}
		ll ans = 0;
		for (int i = 0; i < rep; i++) {
			ans = ans * 10 + dig[i];
		}
		ans = ans * 10 + dig[rep] - 1;
		for (int i = rep + 1; i < dig.size(); i++) {
			ans = ans * 10 + 9;
		}
		printf("Case #%d: %lld\n", cn++, ans);
	}
	return 0;
}