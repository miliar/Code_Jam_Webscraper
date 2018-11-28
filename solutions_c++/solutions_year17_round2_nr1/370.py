#include <bits/stdc++.h>
using namespace std;
typedef long double ld;

int main() {
	int tc;
	scanf("%d", &tc);
	for (int i=1; i<=tc; i++) {
		int d,n;
		scanf("%d%d", &d, &n);
		ld maxspd=1e15;
		for (int j=0; j<n; j++) {
			int k,s;
			scanf("%d%d", &k, &s);
			k=d-k;
			ld t=(ld)k/(ld)s;
			maxspd=min(maxspd,d/t);
		}
		printf("Case #%d: %.8Lf\n", i, maxspd);
	}	
}
