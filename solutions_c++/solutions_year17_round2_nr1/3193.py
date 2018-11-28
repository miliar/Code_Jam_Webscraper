
// ~/BAU/ACM-ICPC/Teams/A++/BlackBurn95
// ~/sudo apt-get Accpeted

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <memory.h>
#include <limits.h>
#include <math.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <limits.h>
#include <limits>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

const double EPS = 1e-8;

int main() {
	std::ios::sync_with_stdio(false);

#ifdef LOCAL
	//freopen("input.txt", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
#endif

	int tc,n;
	double D, k[1001], s[1001];

	scanf("%d", &tc);
	for (int c = 1; c <= tc; c++) {
		scanf("%lf%d", &D, &n);
		for (int i = 0; i < n; i++) 
			scanf("%lf%lf", k + i, s + i);
		
		double l = 0.0, r = 1e18, m, ans = -1;
		int it = 0;

		while ((l < r || abs(l - r) < EPS) && it <= 100) {
			m = (l + r) / 2.0;

			bool f = 1;
			for (int i = 0; i < n; i++) {
				if (s[i] > m || abs(s[i]-m)<EPS) continue;
				double d1 = (m*k[i]) / (m - s[i]);
				if (d1 < D) {
					f = 0;
					break;
				}
			}


			if (f) {
				ans = m;
				l = m;
			}
			else r = m;

			it++;
		}

		printf("Case #%d: %.6lf\n", c, ans);
	}
	return 0;
}