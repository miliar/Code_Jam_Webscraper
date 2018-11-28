#include <bits/stdc++.h>

using namespace std;

#define int long long
typedef map<int, int, greater<int>> Map;

Map Cut(Map arg) {
	Map ret;
	for(auto p : arg) {
		ret[p.first / 2] += p.second;
		ret[(p.first - 1) / 2] += p.second;
	}
	ret.erase(0);
	return ret;
}
int GetSize(Map arg) {
	int ret = 0;
	for(auto p : arg) 
		ret += p.second;
	return ret;
}

int32_t main() {
	int t;
	cin >> t;
	for(int tt = 1; tt <= t; ++tt) {
		int n, k;
		cin >> n >> k;

		Map now;
		now[n] = 1;
		while(GetSize(now) < k) {
			k -= GetSize(now);
			now = Cut(now);
		}

		int ans = -1;
		for(auto p : now) {
			if(p.second >= k) {
				ans = p.first;
				break;
			}
			k -= p.second;
		}

		assert(ans != -1);
		cout << "Case #" << tt << ": " << ans / 2 << " " << (ans - 1) / 2 << endl;
	}
	return 0;
}