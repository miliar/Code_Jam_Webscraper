#include <bits/stdc++.h>
using namespace std;

long long bin(long long val) {
	long long st = 1;
	while(st <= val) {
		st <<= 1;
	}
	st >>= 1;
	return --st;
}

int main() {
	int t;
	scanf("%d", &t);
	for(int tc = 1; tc <= t; ++tc) {
		long long n, k;
		scanf("%lld %lld", &n, &k);

		long long prev = bin(k);

		k -= prev;

		long long small = (n - prev) / (prev + 1); 
		long long large = small + 1;

		long long numlarge = (n - prev) % (prev + 1);
		long long numsmall = prev + 1 - numlarge;

		long long curr = 0;
		if(k <= numlarge) {
			curr = large;
		}
		else {
			curr = small;
		}

		long long mx = curr >> 1;
		long long mn = (curr - 1) >> 1;

		printf("Case #%d: %lld %lld\n", tc, mx, mn);

	}
}