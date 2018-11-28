#include <iostream>
#include <vector>

using namespace std;

typedef long long int64;

int MSB(int64 x) {
	for (int i = 60; i >= 0; --i) {
		if ((x>>i)&1) {
			return i;
		}
	}
}

void solve(int test) {
	cout << "Case #" << test << ": ";

	int64 n, k;
	cin >> n >> k;

	int bit = MSB(k);
	// cout << bit << "\n";

	int64 big = n-1, small = n-1;
	int64 bigCount = 1, smallCount = 0;

	for (int i = bit-1; i >= 0; --i) {
		int64 newBig = max(big>>1, big - (big>>1));
		int64 newSmall = min(small>>1, small - (small>>1));
		int64 newBigCount = 0;
		int64 newSmallCount = 0;

		auto add = [&](int64 wh, int64 amount) {
			if (newBig == wh) {
				newBigCount += amount;
			} else {
				newSmallCount += amount;
			}
		};

		add(big>>1, bigCount);
		add(big - (big>>1), bigCount);
		add(small>>1, smallCount);
		add(small - (small>>1), smallCount);

		big = newBig - 1;
		small = newSmall - 1;
		// cout << small + 1 << " " << big + 1 << ": " << newBigCount << " " << newSmallCount << "\n";
		bigCount = newBigCount;
		smallCount = newSmallCount;
		if (big == small) {
			smallCount = 0;
		}
	}

	k -= (1LL<<bit);
	k += 1;

	int64 fin;

	if (k <= bigCount) {
		fin = big;
	} else {
		fin = small;
	}

	int64 minv = min(fin/2, fin - fin/2);
	// minv = max(minv, 0LL);
	int64 maxv = max(fin/2, fin - fin/2);

	cout << maxv << " " << minv << "\n";
}

int main() {
	int tests;
	cin >> tests;

	for (int k = 1; k <= tests; ++k) {
		solve(k);
	}
}