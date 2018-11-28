#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

pair<pair<ll, ll>, pair<ll, ll> > stk[100001];
int top = 0;
long long n, k;

int main( ) {
	int T, tp = 0;
	scanf("%d", &T);
	while (T --) {
		cin >> n;
		stk[top = 1] = make_pair(make_pair(n, 1), make_pair(-1, -1));
		for (; ; ) {
			pair<ll, ll> x = stk[top].first;
			pair<ll, ll> y = stk[top].second;
			ll mx = 0, mn = 0x3f3f3f3f3f3f3f3fLL;
			ll cnt1 = 0, cnt2 = 0;
			if (x.first != -1) {
				ll xx = x.first / 2, yy = (x.first - 1) / 2;
				mx = max(xx, yy); mn = min(xx, yy);
			}
			if (y.first != -1) {
				ll xx = y.first / 2, yy = (y.first - 1) / 2;
				mx = max(mx, max(xx, yy));
				mn = min(mn, min(xx, yy));
			}
			if (x.first != -1) {
				ll xx = x.first / 2, yy = (x.first - 1) / 2;
				if (xx == mx) cnt1 += x.second;
				else cnt2 += x.second;
				if (yy == mx) cnt1 += x.second;
				else cnt2 += x.second;
			}
			if (y.first != -1) {
				ll xx = y.first / 2, yy = (y.first - 1) / 2;
				if (xx == mx) cnt1 += y.second;
				else cnt2 += y.second;
				if (yy == mx) cnt1 += y.second;
				else cnt2 += y.second;
			}
			if (mn == mx) stk[++ top] = make_pair(make_pair(mx, cnt1), make_pair(-1, -1));
			else stk[++ top] = make_pair(make_pair(mx, cnt1), make_pair(mn, cnt2));
			if (mx == 0) break;
		}
		cin >> k;
		long long ans = 0;
		for (int i = 1; i <= top; i ++) {
			pair<ll, ll> x = stk[i].first;
			pair<ll, ll> y = stk[i].second;
			if (k > x.second) k -= x.second;
			else {
				ans = x.first;
				break;
			}
			if (y.first == -1) continue;
			if (k > y.second) k -= y.second;
			else {
				ans = y.first;
				break;
			}
		}
		printf("Case #%d: ", ++ tp);
		cout << ans / 2 << " " << (ans - 1) / 2 << endl;
	}
	return 0;
}
		
