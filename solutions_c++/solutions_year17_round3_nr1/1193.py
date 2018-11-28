#include <bits/stdc++.h>

using namespace std;

double contrib(const pair<pair<int,int>,int> &pancake, pair<pair<int,int>,int> &mrpancake) {
	return max(0.0, M_PI * pancake.first.first * pancake.first.first - M_PI * mrpancake.first.first * mrpancake.first.first)
		   + 2 * M_PI * pancake.first.first * pancake.first.second;
}

int main() {
	int T, t, N, K, n, r, h, mrp, bst;
	vector<pair<pair<int,int>,int> > rh;
	double ans, vcontrib;
	scanf("%d", &T);
	for(t = 0; t < T; ++t) {
		scanf("%d %d", &N, &K);
		rh.clear();
		rh.push_back(make_pair(make_pair(0,0),0));
		for(n = 0; n < N; ++n) {
			scanf("%d %d", &r, &h);
			rh.push_back(make_pair(make_pair(r,h),1));
		}
		ans = 0;
		mrp = 0;
		while(K--) {
			bst = 0;
			for(n = 0; n < N; ++n) {
				if(rh[n+1].second && contrib(rh[n+1], rh[mrp]) > contrib(rh[bst], rh[mrp])) {
					bst = n+1;
				}
			}
			ans += contrib(rh[bst], rh[mrp]);
			if(rh[bst].first.first > rh[mrp].first.first) {
				mrp = bst;
			}
			rh[bst].second = 0;
		}
		printf("Case #%d: %.9lf\n", t+1, ans);
	}
	return 0;
}
