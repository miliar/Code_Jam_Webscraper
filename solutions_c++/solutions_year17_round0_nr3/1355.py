#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <bitset>
#include <cstdio>
#include <queue>

using namespace std;

void precalc() {

}

void solve() {
	long long n, k;
	cin >> n >> k;
	--k;

	map<long long, long long> mp;
	mp[n] = 1;

	int iteration = 0;
	while (!mp.empty() && k > 0) {
		++iteration;
		auto it = mp.rbegin();

		long long len = it->first;
		long long cnt = min(it->second, k);

		long long l1 = (len - 1) / 2;
		long long l2 = len - 1 - l1;

		k -= cnt;
		mp[len] -= cnt;
		if (l1 > 0) {
			mp[l1] += cnt;
		}
		if (l2 > 0) {
			mp[l2] += cnt;
		}
		if (mp[len] == 0) {
			mp.erase(len);
		}
	}
	cerr << "Iterations: " << iteration << endl;

	auto it = mp.rbegin();
	long long len = it->first;

	long long l1 = (len - 1) / 2;
	long long l2 = len - 1 - l1;
	if (l1 < l2) swap(l1, l2);

	cout << l1 << " " << l2 << endl;
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	precalc();

	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test) {
		cout << "Case #" << test << ": ";
		cerr << test << endl;
		solve();
	}
	return 0;
}
