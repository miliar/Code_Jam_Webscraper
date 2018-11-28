#include <iostream>
#include <ctgmath>
#include <utility>

using namespace std;



pair<int, int> reccall(int N, int k) {
	if (k == 1) {
		return pair<int, int>(N / 2, (N-1) / 2);
	}
	if (k % 2 == 0) {
		return reccall(N / 2, k / 2);
	}
	else {
		return reccall((N - 1) / 2, k / 2);
	}
}

void solve() {
	int N, k;
	cin >> N >> k;
	pair<int, int> p = reccall(N, k);
	cout << p.first << " " << p.second;
}

int  main() {
	int k;
	cin >> k;
	for (int i = 0; i < k; i++) {
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
	return 0;
}