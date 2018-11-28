#include <iostream>
#include <cstdio>
#include <algorithm>
#include <map>
using namespace std;

#define pi 3.14159265358979

int main() {
	int nCase;
	cin>>nCase;
	for (int iCase = 1; iCase <= nCase; ++iCase) {
		int k, n;
		cin>>n>>k;
		pair<double, double> p[1005];
		double r, h;
		for (int i = 0; i < n; ++i) {
			cin>>r>>h;
			p[i] = make_pair(r, h);
		}
		sort(p, p+n);
		double f[1005];
		for (int i = 0; i <= k; ++i) {
			f[i] = 0;
		}
		for (int i = n-1; i>=0; --i) {
			for (int j = k; j > 0; --j) {
				r = p[i].first;
				h = p[i].second;
				if (j == 1) {
					f[j] = max(f[j], pi*r*r+2*pi*r*h);
				}
				else {
					f[j] = max(f[j], f[j-1]+2*pi*r*h);
				}
			}
		}
		printf("Case #%d: %.9lf\n", iCase, f[k]);
	}
}
