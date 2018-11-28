#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int TN=1; TN<=T; ++TN) {
		int n, p;
		scanf("%d%d", &n, &p);
		vector<int> r(n);
		for (int i=0; i<n; ++i)
			scanf("%d", &r[i]);
		vector<vector<int>> q(n, vector<int>(p));
		for (int i=0; i<n; ++i)
			for (int j=0; j<p; ++j)
				scanf("%d", &q[i][j]);
		int ans = 0;
		if (n == 1) {
			for (int i=0; i<p; ++i) {
				double rate = (double)q[0][i]/r[0];
				double low = rate*10/11, hi = rate*10/9;
				if (floor(low) == low || floor(hi) == hi || floor(low) < floor(hi)) ++ans;
			}
		} else {
			vector<int> per(p);
			for (int i=0; i<p; ++i)
				per[i] = i;
			do {
				int tmp = 0;
				for (int i=0; i<p; ++i) {
					double r1 = (double)q[0][i]/r[0], r2 = (double)q[1][per[i]]/r[1];
					double low = max(r1*10/11, r2*10/11);
					double hi = min(r1*10/9, r2*10/9);
					if (low > hi) continue;
					if (floor(low) == low || floor(hi) == hi) ++tmp;
					else if (floor(low) < floor(hi)) ++tmp;
				}
				ans = max(ans, tmp);
			} while (next_permutation(per.begin(), per.end()));
		}
		printf("Case #%d: ", TN);
		printf("%d\n", ans);
	}
	return 0;
}