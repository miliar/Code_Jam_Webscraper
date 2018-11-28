#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <array>
using namespace std;

#define SZ(a) (int)(a).size()
typedef long long ll;

int itc;

void solve() {
	array<int, 2> ns;
	int n = 0;
	for (int i = 0; i < 2; i++) {
		cin >> ns[i];
		n += ns[i];
	}
	vector<pair<pair<int, int>, int>> a;
	array<int, 2> ts = {0, 0};
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < ns[i]; j++) {
			int s, e;
			cin >> s >> e;
			a.push_back({{s, e}, i});
			ts[i] += e-s;
		}
	}
	// printf("%d %d \n", ts[0], ts[1]);
	sort(begin(a), end(a));
	int ans = n;
	array<vector<int>, 2> b;
	for (int i = 0; i < n; i++) {
		int j = (i+1)%n;
		if (a[i].second != a[j].second) {
			continue;
		}
		ans++;
		int k = a[i].second;
		int x = a[j].first.first - a[i].first.second;
		if (x < 0) {
			x += 1440;
		}
		b[k].push_back(x);
	}
	for (int i = 0; i < 2; i++) {
		sort(begin(b[i]), end(b[i]));
		for (int x: b[i]) {
			if (ts[i]+x > 720) {
				break;
			}
			ts[i] += x;
			ans -= 2;
		}
	}
	printf("%d\n", ans);
}

int main() {
	cin.sync_with_stdio(false);
	int ntc;
	cin >> ntc;
	for (itc = 1; itc <= ntc; itc++) {
		printf("Case #%d: ", itc);
		solve();
	}
}
