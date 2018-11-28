#include <bits/stdc++.h>
using namespace std;

void run() {
	long long n, k; cin >> n >> k;
	map<long long, long long> cnt;
	cnt[n] = 1;
	while (true) {
		long long x = cnt.rbegin()->first;
		if (cnt.size() > 1 && (prev(cnt.rbegin())->first - 1) / 2 >= (x - 1) / 2) {
			x = prev(cnt.rbegin())->first;
		}
		if (k <= cnt[x]) {
			cout << (x - 1) - (x - 1) / 2 << ' ' << (x - 1) / 2;
			return;
		}
		k -= cnt[x];
		if ((x - 1) / 2 > 0) cnt[(x - 1) / 2] += cnt[x];
		cnt[(x - 1) - (x - 1) / 2] += cnt[x];
		cnt.erase(cnt.find(x));
	}
}

int main() {
	int n; cin >> n;
	for (int i = 1; i <= n; ++i) {
		cout << "Case #" << i << ": ";
		run();
		cout << '\n';
	}
	return 0;
}
