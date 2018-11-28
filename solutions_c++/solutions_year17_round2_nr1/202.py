#include<bits/stdc++.h>
using namespace std;

long long k[1005], s[1005];

int main() {
	ios::sync_with_stdio(false);
	freopen("/home/ahmed/Desktop/fiewojfe/A-large.in", "r", stdin);
	freopen("/home/ahmed/Desktop/fiewojfe/A-large.out", "w", stdout);

	int t; cin >> t;
	int id = 1;
	while (t--) {
		long long D;
		int n; cin >> D >> n;
		for (int i = 0; i < n; i++)
			cin >> k[i] >> s[i];
		double low = 0, high = 1e100;
		for (int x = 0; x < 1000; x++) {
			double mid = (low + high) / 2;
			bool valid = true;
			for (int i = 0; i < n; i++) {
				double t1 = D / mid;
				double pos = k[i] + t1 * s[i];
				if (pos + 1e-15 < D)
					valid = false;
			}
			if (valid)
				low = mid;
			else
				high = mid;
		}

		printf("Case #%d: %.13lf\n", id++, low);
	}

	return 0;
}
