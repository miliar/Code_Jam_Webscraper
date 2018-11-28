#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <iostream>
#include <cmath>
#include <queue>
#include <string.h>
#include <string>

#define PI acos(-1)

struct tmp {
	long long R, H;
};
bool operator<(tmp p1, tmp p2) {
	return -p1.R*p1.H  <- p2.R * p2.H;
}

long double get_v(std::vector<tmp>& D, int idx, int K, long double maxi, long double nu) {
	if (K == 0) return nu + maxi * maxi*PI;
	if (idx >= D.size()) return 0;
	long double ret = 0;
	for (int i = idx; i < D.size(); i++) {
		ret = std::max(ret, get_v(D, i + 1, K - 1, std::max(maxi, (long double)D[i].R), nu + 2 * PI*D[i].H*D[i].R));
	}
	return ret;
}
int main(void) {
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		printf("Case #%d: ", tc);
		int N, K;
		scanf("%d%d", &N, &K);

		std::vector<tmp> D(N);
		long double ans = 0;
		for (int i = 0; i < N; i++) {
			scanf("%lld %lld", &D[i].R, &D[i].H);
		}

		std::sort(D.begin(), D.end());
		
		for (int i = 0; i < N; i++) {
			int lim = K - 1;
			if (i < K) lim++;
			long double tot = 2 * PI * D[i].H * D[i].R;
			long double maxR = D[i].R;

			for (int j = 0; j < lim; j++) {
				if (i == j) continue;
				if (D[j].R >= maxR) maxR = D[j].R;
				tot += 2 * PI * D[j].R * D[j].H;
			}
			ans = std::max(ans, tot + PI * maxR*maxR );
		}
		//long double v = get_v(D, 0, K, 0, 0);
		printf("%.9Lf\n", ans );
	}
}