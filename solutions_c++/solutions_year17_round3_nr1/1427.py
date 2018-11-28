#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
int T;

struct P {
	long double r, h;
	bool operator <(const P & t) const {
		return t.r * t.h < r * h;
	}
}a[1013];

int main() {
	scanf("%d", &T);

	for (int t = 0; t < T; t++) {
		int n, k;
		scanf("%d%d", &n, &k);

		for (int i = 0; i < n; i++) {
			scanf("%Lf%Lf", &a[i].r, &a[i].h);
		}

		sort(a, a+n);
		long double ans = 0;
		for (int i = 0; i < n; i++) {
			long double tmpans = (long double) 2 * a[i].r * a[i].h + a[i].r * a[i].r;
			int choose = 1;
			for (int j = 0; j < n && choose < k; j++) {
				if (a[i].r >= a[j].r && i != j) {
					tmpans += (long double) 2 * a[j].r * a[j].h;
					choose ++;
				}
			}
			if (choose == k && tmpans > ans) {
				ans = tmpans;
			}
		}
		printf("Case #%d: %.6Lf\n", t + 1, (long double) ans*acos(-1));
	}	
	return 0;
}
