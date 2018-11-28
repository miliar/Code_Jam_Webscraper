#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;
void solve(int t) {
	int d, n;
	int k[1234], s[1234];
	scanf("%d%d",&d,&n);
	vector<pair<int,int>> h;
	for(int i=0;i<n;i++) {
		scanf("%d%d", &k[i],&s[i]);
		h.push_back(make_pair(k[i], s[i]));
	}
	sort(h.begin(), h.end());
	double ttl_t=0;
	while(true) {
		double min_t=2147483647;
		for(int i=0;i<n-1;i++) {
			if(h[i].second>h[i+1].second) {
				//printf("%d %d %d %d\n", h[i].first, h[i].second, h[i+1].first, h[i+1].second);
				double catch_t=(double)(h[i+1].first-h[i].first)/(h[i].second-h[i+1].second);
				//printf("%lf\n", catch_t);
				if (h[i+1].first + h[i+1].second*catch_t>d) catch_t=2147483647;
				if(catch_t<min_t) min_t=catch_t;
				//printf("%lf\n", catch_t);
			}
			
		}
		if(min_t==2147483647) {
			ttl_t += (double)(d-h[0].first)/h[0].second;
			break;
		}
		for(int i=0;i<n;i++) {
			h[i].first += h[i].second*min_t;
		}
		for(int i=0;i<n-1;i++) {
			if(h[i].second>h[i+1].second) h[i].second=h[i+1].second;
		}
		ttl_t+=min_t;
	}
	printf("Case #%d: %lf\n", t, (double)d/ttl_t);
}

int main() {
	int T;
	scanf("%d", &T);

	for(int i=1; i<=T; i++) {
		solve(i);
	}

	return 0;
}
