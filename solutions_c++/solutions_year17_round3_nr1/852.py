#include <cstdio>
#include <cmath>
#include <vector>
#include <numeric>
#include <algorithm>
using namespace std;
typedef pair<int, int> ii;

const double PI = acos(-1);

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int TN=1; TN<=T; ++TN) {
		int n, k;
		scanf("%d%d", &n, &k);
		vector<ii> rh(n);
		for (int i=0; i<n; ++i)
			scanf("%d%d", &rh[i].first, &rh[i].second);
		sort(rh.begin(), rh.end());
		double ans = 0;
		for (int i=n-1; i>=k-1; --i) {
			int r = rh[i].first;
			int h = rh[i].second;
			vector<double> rxh;
			for (int j=0; j<i; ++j)
				rxh.push_back((double)rh[j].first * rh[j].second);
			sort(rxh.begin(), rxh.end());
			ans = max(ans, PI*r*r + 2*PI*(accumulate(rxh.begin()+(i-k+1), rxh.end(), 0.) + (double)r*h));
		}
		printf("Case #%d: ", TN);
		printf("%.10f\n", ans);
	}
	return 0;
}