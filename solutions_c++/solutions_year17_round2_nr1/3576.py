#include <cstdio>
#include <vector>
#include <string.h>
#include <math.h>
#define feq(x,y) (fabs((x)-(y))<eps)
#define flt(x,y) ((x)<(y)-eps)
#define fgt(x,y) ((x)>(y)+eps)
#define fle(x,y) ((x)<(y)+eps)
#define fge(x,y) ((x)>(y)-eps)
const double inf = 1e40, eps = 1e-9;

using namespace std;

struct r {
	double k, s;
	double h;
	r() {}
	r(double k,  double s, double h): k(k), s(s), h(h) {}
	bool operator<(const r &a) const {
		return k < a.k;
	}
};

double solve() {
	long long d, n;
	scanf("%lld%lld", &d, &n);
	// printf("%ldd %lld \n", d, n);
	vector< r > a;  a.clear();
	for (int i = 0; i < n; i++) {
		long long k, s;
		scanf("%lld%lld", &k, &s);
		a.push_back(r(k, s, (d - k) * 1.0 / s));
	}
	sort(a.begin(), a.end());

	// for (int i = 0; i < n; i++) {
	// 	printf("%lf %lf %lf\n", a[i].k, a[i].s, a[i].h);
	// }

	double time = (d - a[0].k) * 1.0 / a[0].s;
	for (int i = n - 2; i >= 0; i--) {
		int len = a.size();
		// printf("%d\n",len);

		// printf("$$$$$$$$$$\n");
		// for (int q = 0; q < len; q++) {
		// 	printf("%lf %lf %lf\n", a[q].k, a[q].s, a[q].h);
		// }
		// printf("<<<$$$$$$$$$$\n");

		for (int j = i + 1; j < len; j++) {
			if (flt(a[i].h , a[j].h)) {
				double h = (a[j].k - a[i].k) * 1.0 / (a[i].s - a[j].s);
				double h2 = (d - h * a[i].s - a[i].k) / a[j].s;
				if (fgt(h + h2 , time)) {
					time = h + h2;
				}
				// printf("%lf %lf %lf\n", h, h2, time);
				double kk = h * a[i].s + a[i].k;
				// a.push_back( r(kk, a[j].s, (d - kk) * 1.0 / a[j].s) );
			} else {
				// time = (d - a[i].k) * 1.0 / a[i].s;
				// printf("%lf\n", time);
			}
		}
	}

	// printf("%lf\n", time);
	return (feq(time, 0)) ? d : d / time;
}

int main() {
	int T, ca = 0;
	scanf("%d", &T);
	while (T--) {
		// printf("-------------\n");
		double ans = solve();
		printf("Case #%d: %lf\n", ++ca, ans);
	}
	return 0;
}
