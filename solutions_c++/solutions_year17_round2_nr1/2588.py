#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<ll> vll;
int main() {
	int t;
	scanf("%d", &t);
	for(int a = 1; a <= t; ++a) {
		ll d, n;
		scanf("%lld %lld", &d, &n);
		double ans = 0.0;
		ll k, m;
		for(int i = 0; i < n; ++i) {
			cin >> k >> m;
			ans = max(ans, double(d - k) / (double)m);
		}
		printf("Case #%d: %lf \n", a ,(double)d / ans);
	}
}