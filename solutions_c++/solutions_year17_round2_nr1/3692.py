#include <iostream>
#include <cstdio>

using namespace std;

int tc, n, d, x, v;
double fx, fv, t;

int main() {
	cin >> tc;
	for (int i = 1; i <= tc; ++i) {
		cin >> d >> n;
		cin >> fx >> fv;
		while (--n) {
			cin >> x >> v;
			t = (fx - x) / (v - fv);
			if (t < 0 || v*t + x >= d) {
				if (x < fx)
					fx = x, fv = v;
			}
			else {
				if (x > fx)
					fx = x, fv = v;
			}
		}
		t = (d - fx) / fv;
		printf("Case #%d: %.06lf\n", i, d / t);
	}
	return 0;
}