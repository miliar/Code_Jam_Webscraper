#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;

int n, d;
pii h[1005];
const double MAXD = 2000000000;

bool intersect(int c){
	int bp = MAXD;
	for(int i=c+1; i<n; i++){
		if(h[i].second - h[c].second != 0){
			double t = -(h[i].first - h[c].first) / (double)(h[i].second - h[c].second);
			double p = h[i].first + h[i].second * t;
			if(p > h[c].first && p < d){
				if(p < bp){
					bp = p;
				}
			}
		}
	}
	return bp != MAXD;
}

int main() {
	int T;
	scanf("%d", &T);
	for(int t=0; t<T; t++){
		scanf("%d %d", &d, &n);
		for(int i=0; i<n; i++){
			scanf("%d %d", &h[i].first, &h[i].second);
		}
		sort(h, h+n);

		double v;
		for(int i=0; i<=n; i++){
			if(!intersect(i)){
				int pos = h[i].first;
				int speed = h[i].second;
				double t = (d-pos) / (double) speed;
				v = d / t;
				break;
			}
		}
		printf("Case #%d: %.9lf\n", t+1, v);

	}
}
