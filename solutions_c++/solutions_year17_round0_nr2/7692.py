#include <iostream>
#include <string>

using namespace std;

long long tend[100];

bool pr(long long x) {
	long long mx = 0;
	for (long long i = 18; i >= 0; i--) {
		long long a = (x / tend[i]) % 10;
		if (a < mx) {
			return 0;
		}
		mx = a;
	}
	return 1;
}

signed main() {
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	tend[0] = 1;
	for (long long i = 1; i < 50; i++) {
		tend[i] = 10 * tend[i - 1];
	}
	long long t;
	cin >> t;
	for (long long tt = 1; tt <= t; tt++) {
		cout << "Case #" << tt << ": ";
		long long s;
		cin >> s;
		while (!pr(s)) {
			long long mx = 0;
			for (long long i = 18; i >= 0; i--) {
				long long a = (s / tend[i]) % 10;
				if (a < mx) {
					s = s / tend[i + 1];
					s = s * tend[i + 1];
					s--;
				
					break;
				}
				mx = a;
			}
		}
		cout << s << "\n";
	}
}