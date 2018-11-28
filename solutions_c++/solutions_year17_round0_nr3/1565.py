#include <bits/stdc++.h>
using namespace std;

#define rep(i, k, n) for (int i = (k); i < (n); i++)

void solve() {
	long long n, k;
	cin >> n >> k;

	map<long long, long long> cnt;
	cnt[n] = 1;
	while (true) {
		long long len, has;
		tie(len, has) = *cnt.rbegin();

		assert(len != 0);
		assert(has != 0);

		long long a = (len-1)/2;
		long long b = len-1 - a;

		k -= has;
		if (k <= 0) {
			cout << b << " " << a;
			return;
		}

		cnt.erase(len);
		cnt[a] += has;
		cnt[b] += has;
	}
}

int main() {
	ios::sync_with_stdio(false);

	int n; cin >> n;
	rep(i, 0, n) {
		cout << "Case #" << (i+1) << ": ";
		solve();
		cout << endl;
	}

	return 0;
}

