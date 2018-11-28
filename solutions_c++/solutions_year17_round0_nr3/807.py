#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C_large.out", "w", stdout);

	long long nCases;
	cin >> nCases;

	for (long long cnt = 1; cnt <= nCases; cnt++) {
		long long N, K;
		cin >> N >> K;

		long long t = 1;
		while (t + t <= K) {
			t <<= 1;
		}

		t--;

		long long units = (N - t) / (t + 1);
		long long mods = (N - t) % (t + 1);
		long long places = K - t;

		long long last_len = units;
		if (places <= mods)
			last_len++;

		cout << "Case #" << cnt << ": " << last_len / 2 << ' ' << (last_len - 1) / 2 << endl;
	}

	return 0;
}