#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("C-small-1.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int TN=1; TN<=T; ++TN) {
		int n, k;
		double u;
		scanf("%d%d%lf", &n, &k, &u);
		vector<double> p(n);
		for (int i=0; i<n; ++i)
			scanf("%lf", &p[i]);
		sort(p.begin(), p.end());
		p.push_back(1.);
		for (int i=0; i<n; ++i) {
			if ((p[i+1]-p[i]) * (i+1) <= u) {
				u -= (p[i+1]-p[i]) * (i+1);
				for (int j=0; j<=i; ++j)
					p[j] = p[i+1];
			} else {
				for (int j=0; j<=i; ++j)
					p[j] += u/(i+1);
				break;
			}
			if (u < 1e-8) break;
		}
		double ans = 1;
		for (int i=0; i<n; ++i)
			ans *= p[i];
		printf("Case #%d: ", TN);
		printf("%.10f\n", ans);
	}
	return 0;
}