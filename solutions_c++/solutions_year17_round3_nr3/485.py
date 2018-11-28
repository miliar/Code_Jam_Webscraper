#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

double u;
double p[55];

void sol() {
	int n, k; scanf("%d%d", &n, &k);
	scanf("%lf", &u);
	double l = 0, r = 1;
	for(int i = 0;i < n;i++) scanf("%lf", &p[i]);
	for(int k = 0;k < 200;k++) {
		double m = (l + r) / 2, s = 0;
		for(int i = 0;i < n;i++) s += max(0.0, m - p[i]);
		if(s < u) l = m;
		else r = m;
	}
	double a = 1;
	for(int i = 0;i < n;i++) a *= max(l, p[i]);
	printf("%.12lf\n", a);
}

int main() {
	int t; scanf("%d", &t);
	for(int i = 1;i <= t;i++) printf("Case #%d: ", i), sol();
}
