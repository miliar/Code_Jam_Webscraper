#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

pair<long long, long long> get(long long n, long long k) {
	if (k == 1) {
		return make_pair ((n - 1) / 2, n - (n - 1) / 2 - 1);
	}
	if (n % 2 == 1) {
		n /= 2;
	        k = k / 2;
		return get(n, k);
	} else {
		long long l = n / 2, r = n - 1 - l;
		if (l > r) swap(l, r);
		if (k % 2 == 0)
			return get(r, (k+1) / 2);
		return get(l, k / 2);
	}
}

int main() {
	int tt;
	cin >> tt;
	for (int t = 0; t < tt; ++t) {
		long long n, k;
		cin >> n >> k;
		pair<long long, long long> p = get(n, k);
		if (p.first < p.second)swap(p.first, p.second);
		cout << "Case #" << (t + 1) << ": " << p.first << " " << p.second << endl;
	}
	return 0;
}
