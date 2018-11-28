#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <stdio.h>

using namespace std;

typedef long long ll;

void solve(int test) {
	cout << "Case #" << test << ": ";
	ll n, k;
	cin >> n >> k;
	k--;

	vector < pair<ll, ll> > a;
	a.push_back(make_pair(n, 1));
	ll MAX = -1;
	ll MIN = -1;

	while (!a.empty()) {	

		sort(a.begin(), a.end());
		reverse(a.begin(), a.end());

		bool FIND = false;

		for (auto E : a) {
			if (k < E.second) {
				ll x = E.first / 2;
				ll y = (E.first - 1) / 2;
				MAX = max(x, y);
				MIN = min(x, y);
				FIND = true;
				break;
			} else {
				k -= E.second;
			}
		}
		
		if (FIND) break;

		map <ll, ll> mp;
		for (auto e : a) {
			mp[e.first / 2] += e.second;
			mp[(e.first - 1) / 2] += e.second;
		}

		a.clear();

		for (auto e : mp) {
			if (e.first) {
				a.push_back(e);
			}
		}


	}
	cout << MAX << " " << MIN << "\n";
}

int main() {
#ifdef KOBRA
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		solve(i);
	}

	return 0;
}
