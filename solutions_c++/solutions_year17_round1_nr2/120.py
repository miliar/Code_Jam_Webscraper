#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
typedef long long ll;
typedef vector<int> vi;

#define pb push_back
#define eb emplace_back
#define mp make_pair
#define fi first
#define se second
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<(n);i++)
#define ALL(c) (c).begin(),(c).end()

int TC;
int N, P;
ll a[60];
ll b[60][60];
multiset<ll> s[60];

int main() {
	scanf("%d", &TC);
	rep(tc, TC) {
		scanf("%d %d", &N, &P);

		rep(i, N) scanf("%lld", &a[i]);

		rep(i, N) {
			s[i].clear();
			rep(j, P) {
				scanf("%lld", &b[i][j]);
				s[i].insert(b[i][j]);
			}
		}

		int ret = 0;
		ll x = 1;
		while (x <= 2000000) {
			bool ok = 1;

			rep(j, N) {
				ll u = a[j] * x * 9 / 10;
				if (u * 10 < a[j] * x * 9) ++u;
				auto it = s[j].lower_bound(u);
				if (it == s[j].end() || *it * 10 > a[j] * x * 11) {
					ok = 0;
				}
			}

			if (!ok) {
				++x;
			} else {
				++ret;
				rep(j, N) {
					ll u = a[j] * x * 9 / 10;
					if (u * 10 < a[j] * x * 9) ++u;
					s[j].erase(s[j].lower_bound(u));
				}
			}
		}

		printf("Case #%d: %d\n", tc + 1, ret);
	}
	return 0;
}