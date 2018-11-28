#include <bits/stdc++.h>

using namespace std;

vector<long long> Gen(long long lim) {
	vector<long long> ret;
	for(int i = 1; i < 10; ++i)
		ret.push_back(i);

	for(int i = 0; i < ret.size(); ++i) {
		long long now = ret[i];
		if(now > lim / 10 + 5) continue;

		for(int dig = now % 10; dig < 10; ++dig) {
			ret.push_back(now * 10 + dig);
		}
	}

	assert(is_sorted(ret.begin(), ret.end()));
	return ret;
}

int main() {
	auto useful = Gen(1e18);
	cerr << "Size: " << useful.size() << endl;

	int t;
	cin >> t;
	for(int tt = 1; tt <= t; ++tt) {
		long long x;
		cin >> x;
		auto it = upper_bound(useful.begin(), useful.end(), x) - 1;
		cout << "Case #" << tt << ": " << *it << endl;
	}
	return 0;
}