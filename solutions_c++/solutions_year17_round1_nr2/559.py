#include <bits/stdc++.h>
using namespace std;

#define ceil(x, y) ((x)%(y)==0 ? (x)/(y) : (x)/(y)+1)

int t;
int n, p;
int r[1234];
int q[1234][1234];
int a[1234][1234];
int b[1234][1234];
int last[1234];
int cur[1234];

int main()
{
	scanf("%d", &t);
for(int x=1; x<=t; x++) {
	scanf("%d%d", &n, &p);
	for(int i=0; i<n; i++) {
		scanf("%d", &r[i]);
	}
	for(int i=0; i<n; i++) {
		for(int j=0; j<p; j++) {
			scanf("%d", &q[i][j]);
			q[i][j]*=10;
		}
		sort(q[i], q[i]+p);
		for(int j=0; j<p; j++) {
			a[i][j]=ceil(q[i][j], 11*r[i]);
			b[i][j]=q[i][j]/(9*r[i]);
		}
	}
	for(int i=0; i<n; i++) last[i]=-1;
	int ans=0;
	for(int j=0; j<p; j++) {
		if(!(a[0][j]<=b[0][j])) {
			last[0]++;
			continue;
		}
		for(int i=0; i<n; i++) {
			cur[i]=last[i]+1;
		}
		int cura=a[0][j], curb=b[0][j];
		int ok=1;
		for(int i=1; ok && i<n; i++) {
			while(cur[i]<p && (curb<a[i][cur[i]] || b[i][cur[i]]<cura || a[i][cur[i]]>b[i][cur[i]])) cur[i]++;
			if(cur[i]==p) {
				ok=0;
				break;
			}
			cura=max(cura, a[i][cur[i]]);
			curb=min(curb, b[i][cur[i]]);
		}
		if(ok) {
			ans++;
			for(int i=0; i<n; i++) {
				last[i]=cur[i];
			}
		} else {
			last[0]++;
		}
	}
	printf("Case #%d: %d\n", x, ans);
}

	return 0;
}
