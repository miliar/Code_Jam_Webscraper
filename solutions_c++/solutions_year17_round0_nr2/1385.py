#include <iostream>
#include <cstdio>

using namespace std;

typedef long long LL;

const int L = 18 + 1;

int a[L];

int main() {
	int testCases;
	cin >> testCases;
	for (int _ = 1; _ <= testCases; ++_) {
		LL ret = 0;
		LL n;
		cin >> n;
		int l;
		for (l = 0; n > 0; n /= 10, ++l) {
			a[l] = n % 10;
		}
		bool stop = false;
		while (!stop) {
			stop = true;
			for (int i = l - 1; i > 0; --i) {
				if (a[i] > a[i - 1]) {
					--a[i];
					for (int j = i - 1; j >= 0; --j) {
						a[j] = 9;
					}
					stop = false;
					break;
				}
			}
		}
		for (int i = l - 1; i >= 0; --i) {
			n = n * 10 + a[i];
		}
		printf("Case #%d: %lld\n", _, n);
	}
	return 0;
}
