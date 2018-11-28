#include <iostream>
#include <unordered_map>
#include <utility>

using namespace std;

pair<long long, long long> calc(long long n, long long k) {
	if (k == 0) return {n, n};

	unordered_map<long long, long long> um;
	long long a, b;
	long long a_n, b_n;
	long long cnt = 2;

	k--;
	a_n = (n-1)/2;
	b_n = n-1-a_n;
	a = max(a_n, b_n);
	b = min(a_n, b_n);
	um[a] += 1;
	um[b] += 1;
	while (k > cnt) {
		unordered_map<long long, long long> um_n;
		long long k_1, k_2;

		a_n = (a-1)/2;
		b_n = a-1-a_n;
		um_n[a_n] += um[a];
		um_n[b_n] += um[a];
		k_1 = max(a_n, b_n);
		k_2 = min(a_n, b_n);

		if (a != b) {
			a_n = (b-1)/2;
			b_n = b-1-a_n;
			um_n[a_n] += um[b];
			um_n[b_n] += um[b];
			k_1 = max(k_1, max(a_n, b_n));
			k_2 = min(k_2, min(a_n, b_n));
		}

		um.swap(um_n);

		k -= cnt;
		cnt *= 2;

		a = k_1;
		b = k_2;
	}

	if (k != 0) {
		n = (k <= um[a]) ? a : b;
		if (n == 0) return {0, 0};

		a_n = (n-1)/2;
		b_n = n-1-a_n;
		return {max(a_n, b_n), min(a_n, b_n)};
	}

	return {a, b};
}

int main() {
	int t;
	long long n, k;

	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.

	for (int i = 1; i <= t; ++i) {
		cin >> n >> k;
		pair<long long, long long> ret = calc(n, k);
		cout << "Case #" << i << ": " <<  ret.first << " " << ret.second << endl;
	}

	return 0;
}


