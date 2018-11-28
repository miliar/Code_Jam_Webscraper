#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
	int nCase;
	cin>>nCase;
	for (int iCase = 1; iCase <= nCase; ++iCase) {
		int n, k;
		cin>>n>>k;
		double u;
		cin>>u;
		double p[100];
		for (int i = 0; i < n; ++i) {
			cin>>p[i];
		}
		double ans = 1;
		sort(p, p+n);
		int x = 1;
		while (x < n && u > p[x]-p[0]) {
			if (u > x*(p[x]-p[0])) {
				u -= x*(p[x]-p[0]);
				for (int i = 0; i < x; ++i) {
					p[i] = p[x];
				}
			}
			else {
				double d = u/x;
				u = 0;
				for (int i = 0; i < x; ++i) {
					p[i] += d;
				}
			}
			++x;
		}
		if (u > 0) {
			double d = u/n;
			if (p[0]+d > 1) {
				for (int i = 0; i < n; ++i) {
					p[i] = 1;
				}
			}
			else {
				for (int i = 0; i < n; ++i) {
					p[i] += d;
				}
			}
		}
		for (int i = 0; i < n; ++i) {
			ans *= p[i];
		}
		printf("Case #%d: %.6lf\n", iCase, ans);
	}
}
