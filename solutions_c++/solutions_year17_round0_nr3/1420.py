#include <iostream>
#include <cstdio>
#include <cstring>
#include <map>

using namespace std;

typedef long long LL;

map<LL, LL> a, b;

int main() {
	int testCases;
	cin >> testCases;
	for (int _ = 1; _ <= testCases; ++_) {
		a.clear();

		LL n, k;
		cin >> n >> k;
		LL cnt = 1LL;
		a[n] = 1LL;
		while (k > cnt) {
			k -= cnt;
			b.clear();
			for (auto p: a) {
				LL x = p.first;
				LL c = p.second;
				LL l = (x - 1) / 2LL;
				LL r = x - 1 - l;
				b[l] += c;
				b[r] += c;
			}
			swap(a, b);
			cnt <<= 1;
		}
		LL c0 = a.begin()->second, c1 = cnt - c0;
		if (k <= c1) {
			n = a.begin()->first + 1;
		} else {
			n = a.begin()->first;
		}
		LL l = (n - 1) / 2LL, r = n - 1 - l;
		printf("Case #%d: %lld %lld\n", _, r, l);
	}
	return 0;
}
