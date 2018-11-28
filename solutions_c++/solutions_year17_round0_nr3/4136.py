#include <bits/stdc++.h>

using namespace std; 

typedef pair<int, int> pii;
typedef long long ll;
#define mp make_pair
#define pb push_back;


set < pair<int, pii > > s;

void solve() {
	s.clear();
	int n, k;
	cin >> n >> k;
	
	s.insert(mp(n, mp(1, n)));
	int mn = 0, mx = 0;
	for (int i = 0; i < k; i++) {
		int v = s.rbegin() -> first;
		auto tmp = s.lower_bound(mp(v, mp(0, 0)));
		int l = tmp -> second.first;
		int r = tmp -> second.second;
		int mid = (l + r) >> 1;
		mn = (mid - l), mx = (r - mid);
		s.erase(tmp);
		s.insert(mp(mn, mp(l, mid - 1)));
		s.insert(mp(mx, mp(mid + 1, r)));
	}
	cout << mx << " " << mn << "\n";
}

int main () {
#ifdef LOCAL
	freopen ("test.in", "r", stdin);
	freopen ("test.out", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}