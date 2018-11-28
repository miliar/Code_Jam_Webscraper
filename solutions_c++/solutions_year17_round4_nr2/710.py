#include <bits/stdc++.h>
using namespace std;

int main() {
	int tc;
	scanf("%d", &tc);
	for (int t=1; t<=tc; t++) {
		int n,c,m;
		scanf("%d%d%d", &n,&c,&m);
		int cust[c];
		int seat[n];
		memset(cust,0,sizeof(cust));
		memset(seat,0,sizeof(seat));
		for (int i=0; i<m; i++) {
			int p, b;
			scanf("%d%d", &p, &b);
			p--; b--;
			seat[p]++;
			cust[b]++;
		}
		/*for (int i=0; i<c; i++) printf("%d ", cust[i]);
		printf("\n");
		for (int i=0; i<n; i++) printf("%d ", seat[i]);
		printf("\n");*/
		int opt=0;
		for (int i=0; i<c; i++) opt=max(opt,cust[i]);
		opt=max(opt,max((m-1)/n+1,seat[0]));
		int need=0;
		for (int i=n-1; i>0; i--) {
			if (seat[i]>opt) {
				need+=seat[i]-opt;
			}
		}
		printf("Case #%d: %d %d\n", t, opt, need);
	}
}
		
