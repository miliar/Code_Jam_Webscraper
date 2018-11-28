#include <iostream>
#include <cstdio>
#include <map>

using namespace std;

int main() {
	int t, tc = 0;
	long long int n, k, x, ct;
	cin >> t;
	while (t--) {
		cin >> n >> k;

		// map<#stalls in a region, #regions with same stalls count>
		map<long long int, long long int> m;
		map<long long int, long long int>::iterator it;

		m[n] = 1;
		while (1) {
			it = --m.end();
			x = it->first;
			ct = it->second;
			if (k <= ct)
				break;
			k -= ct;
			m[x / 2] += ct;
			m[(x - 1) / 2] += ct;
			m.erase(it);
		}
		printf("Case #%d: %lld %lld\n", ++tc, x / 2, (x - 1) / 2);
	}
	return 0;
}