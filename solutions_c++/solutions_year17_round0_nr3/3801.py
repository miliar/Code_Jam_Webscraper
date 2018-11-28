#include <bits/stdc++.h>

using namespace std;

int main() {
	//freopen("C-small-2-attempt0.in", "r", stdin);
	//freopen("C-small2.out", "w", stdout);
	int t, kase = 1;
	long long n, k;
	cin >> t;
	while(t--) {
		cin >> n >> k;
		long long d = (long long)log2(k) + 1;
		long long mod = (n - ( (long long )pow(2, d) - 1 ) ) % ( (long long)pow(2, d));
		long long min = (n - ( (long long )pow(2, d) - 1 ) ) / ( (long long)pow(2, d));
		long long max = min;
		long long pos = k - (long long)(pow(2, d - 1));
		if(pos < mod) max++;
		mod -= (long long)(pow(2, d - 1));
		if(pos < mod) min++;
		printf("Case #%d: %lld %lld\n", kase++, max, min);
	}
	return 0;
}