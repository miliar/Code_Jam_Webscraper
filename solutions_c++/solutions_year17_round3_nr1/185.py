#include<bits/stdc++.h>
using namespace std;
#define ALL(v) (v).begin(),(v).end()
int main() {
	int T; cin >> T;
	for(int tc=1;tc<=T;tc++) {
		int N, K; cin >> N >> K;
		vector<pair<int,int>> items;
		for (int i=0; i<N; i++) {
			int r, h; cin >> r >> h;
			items.push_back(make_pair(r,h));
		}
		sort(items.begin(),items.end());
		vector<int> rr (N), hh (N);
		for (int i=0; i<N; i++) rr[i] = items[i].first, hh[i] = items[i].second;
		double answer = 0;
		for (int last=K-1; last<N; last++) {
			double cand = M_PI * rr[last] * rr[last] + 2 * M_PI * rr[last] * hh[last];
			vector<double> rest;
			for (int i=0; i<last; i++) rest.push_back(2 * M_PI * rr[i] * hh[i]);
			sort(rest.begin(),rest.end(),greater<double>());
			for (int it=0; it<K-1; it++) cand += rest[it];
			answer = max(answer, cand);
		}
		printf("Case #%d: %.9lf\n", tc, answer);
	}
}
