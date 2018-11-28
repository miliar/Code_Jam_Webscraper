#include <bits/stdc++.h>
using namespace std;

int main() {
	int ncases;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		double D;
		int N;
		cin >> D >> N;
		double tmax = 0;
		for (int i = 0; i < N; i++) {
			double k, s;
			cin >> k >> s;
			double t = (D-k)/s;
			tmax = max(tmax, t);
		}
		
		double ans = D/tmax;
		
		cout << "Case #" << icase << ": ";
		cout << fixed << setprecision(9) << ans << endl;
	}
	return 0;
}
