#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <omp.h>
#include <algorithm>
#include <cmath>
using namespace std;

const int mn = 1010;
using ll = long long;

const double PI = acos(-1.0);
struct cake {
	int r, h;
} a[mn];

bool cmp(cake a, cake b) {
	return (ll) a.r * a.h < (ll) b.r * b.h;
}
int main() {
	int Tn;
	scanf("%d", &Tn);

	for (int Tc = 1; Tc <= Tn; ++Tc) {
		int n, k;
		scanf("%d%d", &n, &k);
		for (int i = 0; i < n; ++i)
			scanf("%d%d", &a[i].r, &a[i].h);
		sort(a, a + n, cmp);

		double ans = 0;
		for (int i = 0; i < n; ++i) {
			double curans = PI * a[i].r * a[i].r + 2 * PI * a[i].r * a[i].h;
			for (int j = n - 1, c = 1; j >= 0 && c < k; --j) {
				if (j != i && a[j].r <= a[i].r) {
					curans += 2 * PI * a[j].r * a[j].h;
					++c;
				}
			}
			if (curans > ans)
				ans = curans;

		}

		printf("Case #%d: ", Tc);
		printf("%.10f\n", ans);
	}
	return 0;
}
