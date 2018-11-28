#include <bits/stdc++.h>

using namespace std;

long double pi = 3.14159, ans, fans;
long double b, h, n ,k;
int t;
vector<pair<long double, long double> > bh;
multiset<long double> hb;
multiset<long double>::iterator it;

int main() {
	freopen("inn", "r", stdin);
	freopen("myfile.txt", "w", stdout);
	scanf("%d", &t);
	for (int kk = 1; kk <= t; kk++) {
		bh.clear();
		hb.clear();
		ans = fans = 0;
		cin >> n >> k;
		for (int i = 0; i < n; i++) {
			cin >> b >> h;
			hb.insert(2.0 * pi * b * h * -1);
			bh.push_back(make_pair(-1 * b, -1 * h));
		}
		sort(bh.begin(), bh.end());
		for (int i = 0; i < n; i++) {
			ans = 0;
			long double base = bh[i].first * -1;
			ans += (base * base) * pi;
			ans += (2.0 * pi * base * (bh[i].second * -1));
			hb.erase(hb.find(-2.0 * pi * bh[i].first * bh[i].second));
			it = hb.begin();
			if (hb.size() >= k - 1) {
				for (int j = 1; j < k; j++) {
					ans += -(*it);
					it++;
				}
			}
			fans = max(ans, fans);
		}
		printf("Case #%d: %.7llf\n", kk, fans);
	}
	return 0;
}
