#include <bits/stdc++.h>
using namespace std;
int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T = 0; 
	scanf("%d",&T);
	int D = 0,n = 0;
	double ti = 0;
	int k = 0,s = 0;
	for(int t = 1;t <= T;++ t) {
		scanf("%d%d",&D,&n);
		ti = 0;
		for(int i = 1;i <= n;++ i) {
			scanf("%d%d",&k,&s);
			ti = max(ti, 1.0F * (D-k) / (double)s);
		}
		printf("Case #%d: %.6lf\n",t,D/ti);
	} 
	return 0;
} 
