#include <bits/stdc++.h>
using namespace::std;

int main() {
	long long t, caseno = 0;
	cin >> t;
	while (t--) {
		caseno++;
		double ans = 1.0;
		int n, k;
		cin >> n >> k;
		double u;
		cin >> u;
		vector <double> p;
		for (int i = 0; i < n; i++) {
			double temp;
			cin >> temp;
			p.push_back(temp);
		}
		p.push_back(1.000000000);
		int j = 0;
		sort(p.begin(), p.end());
		while (u > 0.000000000) {
			if (j + 1 >= p.size())
				break;
			double req = (p[j + 1] - p[j]) * (j + 1);
			if (u >= req) {
				u -= req;
				for (int i = 0; i <= j; i++)
					p[i] = p[j + 1];
				j++;
			} else {
				for (int i = 0; i <= j; i++)
					p[i] += (u * 1.0) / (j + 1);
				u = 0;
			}
		}
		for (int i = 0; i < p.size() - 1; i++)
			ans *= p[i];
		cout << fixed << setprecision(10) << "Case #" << caseno << ": " << ans << endl;
	}
	return 0;
}