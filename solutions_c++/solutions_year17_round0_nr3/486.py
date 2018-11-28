#include <iostream>
using namespace std;

#define debug(x) cout <<  #x  << ": " << x << endl

int main() {
	int t; cin >> t;

	for (int i=1; i<=t; ++i) {
		long long n; cin >> n;
		long long k; cin >> k;

		long long mn;
		long long mx;

		while (true) {
			mx = n/2;
			mn = (n-1)/2;
			--k;

			// debug(k);
			if (k & 1) {
				k = (k+1)/2;
				n = mx;
			} else {
				k = k/2;
				n = mn;
			}

			// debug(mn);
			// debug(mx);
			// debug(n);
			// debug(k);
			// debug("--");

			if (k == 0) {
				break;
			}

			// mn = n/2;
			// mx = (n-1)/2;
		}

		cout << "Case #" << i << ": " << mx << " " << mn << endl;
	}

}