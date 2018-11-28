#include <iostream>
#include <cstdio>
#include <map>

#define Node pair<long long,long long>
#define len first
#define ct second

using namespace std;

int main() {
	int Cases;
	cin >> Cases;

	for (int Case = 1; Case <= Cases; ++Case) {
		long long n, k;
		cin >> n >> k;

		map<long long, long long> ct;
		ct[n] = 1;

		long long L, r;

		while(1) {
			map<long long, long long>::iterator mi = ct.end(); --mi;
			L = mi->first;
			// cout << L << ' ' << r << '\n';
			r = mi->second;
			if (k <= r) {
				break;
			}
			else {
				ct.erase(mi);
				k -= r;

				ct[L/2] += r;
				ct[(L-1)/2] += r;
			}
		}

		long long u, v;
		u=L/2;
		v=(L-1)/2;
		printf("Case #%d: %lld %lld\n", Case, u, v);
	}

	return 0;
}