#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	int nt; cin >> nt;
	for (int tc = 1; tc <= nt; ++tc) {
		int n, c, m; cin >> n >> c >> m;
		vector<int> booked (n);
		vector<int> bought (c);
		for (int i = 0; i < m; ++i) {
			int p, b; cin >> p >> b; --p; --b;
			++booked[p];
			++bought[b];
		}
		int maxBooked = *max_element(booked.begin(), booked.end());
		int maxBought = *max_element(bought.begin(), bought.end());
		int res = max(maxBooked, maxBought);
		int move = 0;
		for (int lim = maxBooked - 1; lim >= maxBought; --lim) {
			bool ok = true;
			vector<int> cnt = booked;
			int moved = 0;
			for (int i = n - 1, j = n - 1; ok && i >= 0; --i) {
				while (cnt[i] > lim) {
					if (j >= i) j = i - 1;
					while (j >= 0 && cnt[j] >= lim) --j;
					if (j < 0) {
						ok = false;
						break;
					}
					--cnt[i];
					++cnt[j];
					++moved;
				}
			}
			if (ok) {
				res = lim;
				move = moved;
			}
		}
		cout << "Case #" << tc << ": " << res << ' ' << move << '\n';
	}
	return 0;
}
