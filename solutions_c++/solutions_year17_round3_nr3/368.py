#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int n, k; 
		cin >> n >> k;
		double u;
		cin >> u;
		vector<double> p(n);
		for (int j = 0; j < n; j++) {
			cin >> p[j];
		}
		sort(p.begin(), p.end());
		while (u > 0.0000001) {
			int c = 1;
			double p2 = -1;
			for (int j = 1; j < n; j++) {
				if (p[j] == p[j - 1]) {
					c++;
				}
				else {
					p2 = p[j];
					break;
				}
			}
			//cout << p[0] << ' ' << p2 << ' ' << u << endl;
			if (p2 == -1) {
				if (p[0] == 1.0) {
				}
				else {
					for (int j = 0; j < n; j++) {
						p[j] += u / (double)n;
					}
				}
				break;
			}
			else {
				if ((p2 - p[0])*c <= u) {
					u -= (p2 - p[0])*c;
					for (int j = 0; j < c; j++) {
						p[j] = p2;
					}
				}
				else {
					for (int j = 0; j < c; j++) {
						p[j] += u / (double)c;
					}
					break;
				}
			}
		}
		double ans = 1.0;
		for (int j = 0; j < n; j++) {
			ans *= p[j];
		}
		printf("Case #%d: %.9f\n",i+1, ans);
	}
	return 0;
}