#include <iostream>

using namespace std;

int main() {
	long long tps[100] = {0, 1};
	int tpscnt = 1;
	for (int i = 2; i < 100; i++) {
		if (2 * tps[i - 1] < 1000000000000000000) {
			tps[i] = 2 * tps[i - 1] + 1;
			tpscnt++;
		}
		else break;
	}
	int t;
	long long n, k;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		int ans1 = 0, ans2 = 0;
		cin >> n >> k;
		for (int j = tpscnt; j >= 0; j--) {
			if (tps[j] < k) {
				long long tp = tps[j] + 1;
				n -= tps[j];
				k -= tps[j];
				int q = n / tp;
				if (k > n - q * tp) q--;
				ans1 = max(q / 2, (q + 1) / 2);
				ans2 = min(q / 2, (q + 1) / 2);
				break;
			}
		}
		cout << "Case #" << i << ": " << ans1 << " " << ans2 << endl;
	}
	return 0;
}