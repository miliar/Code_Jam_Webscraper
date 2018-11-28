#include <bits/stdc++.h>
#define EPS 1e-8
using namespace std;

int main() {
	int tc;
	scanf("%d", &tc);
	for (int i=1; i<=tc; i++) {
		int n,q;
		scanf("%d%d", &n, &q);
		long long e[n], s[n];
		for (int j=0; j<n; j++) scanf("%lld%lld", &e[j], &s[j]);
		long long route[n][n];
		for (int j=0; j<n; j++) {
			for (int k=0; k<n; k++) {
				scanf("%lld", &route[j][k]);
			}
		}
		for (int p=0; p<n; p++) {
			for (int j=0; j<n; j++) {
				for (int k=0; k<n; k++) {
					if (route[j][p]==-1 || route[p][k]==-1) continue;
					if (route[j][k]==-1) route[j][k]=route[j][p]+route[p][k];
					else route[j][k]=min(route[j][k],route[j][p]+route[p][k]);
				}
			}
		}
		
		
		long double tm[n][n];
		for (int j=0; j<n; j++) {
			for (int k=0; k<n; k++) {
				//printf("%lld %lld\n ", e[j], route[j][k]);
				if (route[j][k]!=-1 && e[j]>=route[j][k]) {
					tm[j][k]=(long double)route[j][k]/(long double)s[j];
				}
				else tm[j][k]=-1;
			}
		}

		
		for (int p=0; p<n; p++) {
			for (int j=0; j<n; j++) {
				for (int k=0; k<n; k++) {
					if (tm[j][p]<0 || tm[p][k]<0) continue;
					if (tm[j][k]<0) tm[j][k]=tm[j][p]+tm[p][k];
					else tm[j][k]=min(tm[j][k],tm[j][p]+tm[p][k]);
				}
			}
		}
		printf("Case #%d:", i);
		for (int j=0; j<q; j++) {
			int v,u;
			scanf("%d%d", &v, &u);
			v--; u--;
			printf(" %Lf", tm[v][u]);
		}
		printf("\n");
	}
}
