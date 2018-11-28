#include <bits/stdc++.h>
#define pb push_back
typedef long long ll;
const int N = 1e5 + 10;

using namespace std;

int test, id;
ll n, k;

void update(ll x, ll& t1, ll& t2) {
	x--;
	if (x & 1) {
		t1 = x / 2;
		t2 = x / 2 + 1;
	}
	else t1 = t2 = x / 2;
}

int main() {
	ios::sync_with_stdio(false);
	cin >> test;
	while (test--) {
		cin >> n >> k;
		id++;
		map<ll, ll> f;
		f[n] = 1;
		ll ans_min, ans_max;
		while (1) {
			auto x = f.end();
			x--;
			auto tmp = *x;
			if (tmp.second >= k) {
				update(tmp.first, ans_min, ans_max);
				break;
			}
			else {
				ll x, y;
				k -= tmp.second;
				f.erase(tmp.first);
				update(tmp.first, x, y);
				f[x] += tmp.second;
				f[y] += tmp.second;
			}
		}
		cout << "Case #" << id << ": " << ans_max << " " << ans_min << endl;
	}
	return 0;
}