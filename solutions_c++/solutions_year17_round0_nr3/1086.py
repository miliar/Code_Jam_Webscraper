#include <iostream>
#include <vector>

using namespace std;

void solve() {
	long long n, k;
	vector<long long> v(500, -1), cnt(500, 0);
	cin >> n >> k;
	v[0] = n, cnt[0] = 1;
	int p = 0, q = 0;
	long long sum = cnt[p], a = (v[p] - 1) / 2 + (v[p] - 1) % 2, b = v[p] - 1 - a;
	while (sum < k) {
		while (v[q] != -1 && v[q] != a)
			q++;
		v[q] = a;
		cnt[q] += cnt[p];
		while (v[q]  != -1 && v[q] != b)
			q++;
		v[q] = b;
		cnt[q] += cnt[p];
		p++;
		sum += cnt[p];
		a = (v[p] - 1) / 2 + (v[p] - 1) % 2, b = v[p] - 1 - a;
	}
	cout << a << " " << b << endl;
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}
