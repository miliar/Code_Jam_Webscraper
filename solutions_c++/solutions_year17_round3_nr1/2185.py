#include <bits/stdc++.h>

using namespace std;

#define F first
#define S second
#define PB push_back

typedef long long ll;
typedef double dou;
const int MAXN = 1e3 + 10;
dou pi = 3.141592653589;
ll t, h;

ll mrx(ll a, ll b) {return a < b ? b : a;}

int main() {
	ios_base::sync_with_stdio(false);
	cin >> t;
	while (t--) {
		ll n, k, ans = 0, mx = 0;
		cin >> n >> k;
		pair <ll, ll> p[MAXN];
		for (int i = 0; i < n; i++) {
			ll r, h;
			cin >> r >> h;
			p[i] = make_pair(2 * r * h, r);
		}
		sort(p, p + n), reverse(p, p + n);
		for (int i = 0; i < n; i++) {
			ll r = p[i].S, l = 0, ans = 0;
			pair <ll, ll> sp[MAXN];
			for (int j = 0; j < n; j++)
				if (p[j].S <= r && j != i)
					sp[l++] = make_pair(p[j].F, p[j].S);
			if (l > k - 2) {
				for (int j = 0; j < k - 1; j++)
					ans += sp[j].F;
				ans += p[i].F + r * r;
				mx = max(ans, mx);
			}
		}
		cout << "Case #" << ++h << ": " << setprecision(9) << fixed << dou(dou(mx) * pi) << endl;
	}
	return 0;
}
