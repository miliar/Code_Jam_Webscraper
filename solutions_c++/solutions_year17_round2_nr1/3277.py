#include <bits/stdc++.h>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int t, tc=0;
	cin >> t;

	while(t--) {
		int des, n;
		cin >> des >> n;

		int st[n], v[n];
		for(int i=0; i<n; ++i) cin >> st[i] >> v[i];

		double lo = 0, hi = 1e18, mid;
		int cnt = 0;

		while(++cnt < 100) {
			bool ok = true;
			mid = (lo + hi) / 2;
			double tm = (double) des / mid;

			for(int i=0; i<n; ++i) {
				double tempTime = (double) st[i] / (mid - v[i]);
				// cout << tempTime << " - ";
				if(tempTime > 0 && tempTime < tm) {
					ok = false;
					break;
				}
			} // cout << endl;

			if(!ok) hi = mid;
			else lo = mid;
			// cout << mid << " " << tm << "\n";
		}

		cout << "Case #" << ++tc << ": " << fixed << setprecision(6) << mid << "\n";
	}

	return 0;
}