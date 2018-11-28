#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <string>
#include <functional>
#include <numeric>
#define ll long long
using namespace std;
int main() {
	cin.tie(0); ios::sync_with_stdio(false);
	int T; cin >> T;
	for (int t = 1; t <= T;t++) {
		cout << "Case #" << t << ": ";

		ll N, K;cin >> N >> K;
		priority_queue<pair<ll, pair<ll, ll>>> q;
		q.push(make_pair(N + 1, make_pair(0, N + 1)));
		ll count = 0;
		while (!q.empty()) {
			auto p = q.top(); q.pop();
			ll l = p.second.first, r = p.second.second;
			ll mid = (l + r) / 2;
			if ((mid + r) / 2 != mid)q.push(make_pair(r - mid,make_pair(mid, r)));
			if ((mid + l) / 2 != l)q.push(make_pair(mid - l, make_pair(l, mid)));

			count++;
			if (count == K) {
				cout << max(r - mid - 1, mid - l - 1) << " " << min(r - mid - 1, mid - l - 1) << endl;
				break;
			}
		}
	}
}