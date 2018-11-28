/******************************************
*    AUTHOR:         BHUVNESH JAIN        *
*    INSTITUITION:   BITS PILANI, PILANI  *
******************************************/
#include <bits/stdc++.h>
using namespace std;
 
typedef long long LL; 
typedef long double LD;
typedef pair<int,int> pii;
typedef pair<LL, LL> pll;

const long double PI = acos(-1.0);

bool cmp(pll a, pll b) {
	return a.first > b.first;
}

int main() {
	int t, n, k;
	scanf("%d", &t);
	for(int T = 1; T <= t; ++T) {
		printf("Case #%d: ", T);
		scanf("%d %d", &n, &k);
		vector<pll> x(n), y;
		for(int i = 0; i < n; ++i) {
			scanf("%lld %lld", &x[i].first, &x[i].second);
		}
		sort(x.begin(), x.end(), cmp);
		LL ans = 0;
		for(int i = 0; i < n; ++i) {
			LL temp = 0;
			vector<LL> vals;
			for(int j = i+1; j < n; ++j) {
				vals.push_back(2LL * x[j].first * x[j].second);
			}
			if (vals.size() >= (k-1)) {
				sort(vals.rbegin(), vals.rend());
				for(int j = 0; j < (k-1); ++j) {
					temp += vals[j];
				}
				temp += x[i].first * x[i].first;
				temp += 2LL * x[i].first * x[i].second;
				ans = max(ans, temp);
			}
		}
		// printf("%lld\n", ans);
		printf("%.10Lf\n", ans * PI);
	}
	return 0;
}