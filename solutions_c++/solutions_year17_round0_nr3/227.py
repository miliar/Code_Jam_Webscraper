#include <bits/stdc++.h>
using namespace std;

long long n, k;

map<long long, long long> avail;

void solve() {
	scanf("%lld%lld", &n, &k);
	avail.clear();
	avail[n] = 1;
	long long y, z;
	while (k > 0) {
		long long x = avail.rbegin()->first;
		long long cx = avail[x];
		avail.erase(x);
		z = (x - 1) / 2;
		y = x - 1 - z;
		if (y > 0) avail[y] += cx;
		if (z > 0) avail[z] += cx;
		k -= cx;
	}
	printf("%lld %lld\n", y, z);
}

int main() {
	freopen("C.out", "w", stdout);
	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		solve();
	}
}