#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

const double eps = 1e-8;
double k[2005], d, s[2005];
int n, m;

int comp(double a, double b) {
	if (fabs(a - b) < eps)
		return 0;
	if (a - b < eps)
		return -1;
	return 1;
}

bool check(double v) {
	for (int i = 1; i <= n; ++i) 
	if (comp(v, s[i]) > 0) {
		double t = k[i] / (v - s[i]);
		if (comp(v * t, d) < 0)
			return false;
	}

	return true;
}

int main() {
	#ifdef LOCAL	
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	#endif
	cin >> m;
	for (int t = 1; t <= m; ++t) {
		cout << "Case #" << t <<": ";
		cin >> d >> n;
		double L = 0, R = 1e15, res = 0;
		for (int i = 1; i <= n; ++i) 
			cin >> k[i] >> s[i];
		
		int z = 200;
		while (z--) {
			double mid = (L + R) / 2.0;
			if (check(mid)) {
				res = mid;
				L = mid;
			} else 
				R = mid;
		}
		printf("%.6f\n", res);
  }  
	return 0;
}




