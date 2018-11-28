#include <bits/stdc++.h>

using namespace std;

long long n, k;

void solve() {
	cin >> n >> k;
	map<long long, long long> cnt;
	cnt[n] = 1;
	while (k) {
		auto it = cnt.end();
		--it;
		long long len = it->first, num = it->second;
		cnt.erase(it);
		if (k <= num) {
			cout << len / 2 << " " << (len - 1) / 2 << endl;
			return ;
		} else {
			k -= num;
			cnt[len / 2] += num;
			cnt[(len - 1) / 2] += num;
		}
	}
	assert(false);
}

int main() {
	int test;
	scanf("%d", &test);
	while (test--) {
		static int test_count = 0;
		printf("Case #%d: ", ++test_count);
		solve();
	}
	return 0;
}
