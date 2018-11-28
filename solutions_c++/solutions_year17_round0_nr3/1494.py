#include <bits/stdc++.h>
using namespace std;

void solve() {
	long long n, k, c[] = {1, 0};
	cin >> n >> k;
	while(k > c[0] + c[1]) {
		k -= c[0] + c[1];
		c[~n & 1] = c[~n & 1] * 2 + c[n & 1];
		n >>= 1;
	}
	if(k <= c[0]) {
		cout << ' ' << (n >> 1) << ' ' << (n >> 1) - (~n & 1) << '\n';
	} else {
		cout << ' ' << (n >> 1) - (~n & 1) << ' ' << (n >> 1) - 1 << '\n';
	}
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ':';
		solve();
	}
	return 0;
}
