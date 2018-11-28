#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cassert>
#include <vector>
#include <map>
#include <functional>

using namespace std;

void solve(int testid) {
	long long n, k;
	cin >> n >> k;

	map<long long, long long, greater<long long>> mp;
	mp[n] = 1;
	while (k > 0) {
		auto it = mp.begin();
		long long w = it->first;
		long long cnt = it->second;
		long long L = (w - 1) / 2;
		long long R = w / 2;
		mp.erase(it);
		if (k - cnt > 0) {
			if (L > 0) {
				mp[L] += cnt;
			}
			if (R > 0) {
				mp[R] += cnt;
			}
			k -= cnt;
		} else {
			printf("Case #%d: %lld %lld\n", testid, R, L);
			return;
		}
	}
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		solve(i + 1);
	}
}