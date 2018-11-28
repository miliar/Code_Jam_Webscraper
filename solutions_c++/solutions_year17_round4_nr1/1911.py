#include<bits/stdc++.h>
using namespace std;
int f[105][105];
int g[105][105][105];
int a[10];
int main() {
	freopen("1.txt","r",stdin);
	freopen("1.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i=0;i<=100;i++)
		for (int j=0;j<=100;j++) {
			if (i > 0 && j > 0) f[i][j] = max(f[i][j],f[i-1][j-1] + 1);
			if (i >= 3) f[i][j] = max(f[i][j],f[i-3][j] + 1);
			if (j >= 3) f[i][j] = max(f[i][j],f[i][j-3] + 1);
		}
	for (int i=0;i<=100;i++)
		for (int j=0;j<=100;j++) 
			for (int k=0;k<=100;k++) {
				if (i>=4) g[i][j][k] = max(g[i][j][k],g[i-4][j][k] + 1);
				if (i>=2 && j>=1) g[i][j][k] = max(g[i][j][k],g[i-2][j-1][k] + 1);
				if (j>=2) g[i][j][k] = max(g[i][j][k],g[i][j-2][k] + 1);
				if (i>=1 && k>=1) g[i][j][k] = max(g[i][j][k],g[i-1][j][k-1] + 1);
				if (k>=4) g[i][j][k] = max(g[i][j][k],g[i][j][k-4] + 1);
			}
	for (int _t = 1;_t <= T; _t++) {
		printf("Case #%d: ",_t);
		int n,p,sum = 0;
		memset(a,0,sizeof a);
		scanf("%d%d",&n,&p);
		for (int i=0;i<n;i++) {
			int x;
			scanf("%d",&x);
			sum += x;
			a[x % p]++;
		}
		//cout<<a[0]<<' '<<a[1]<<' '<<a[2]<<' '<<a[3]<<' ';
		int flag = 0;
		if (sum % p == 0) flag = -1;
		if (p == 2) {
			printf("%d\n",a[0] + 1 + a[1] / 2 + flag);
		}
		else if (p == 3) {
			printf("%d\n",f[a[1]][a[2]] + a[0] + 1 + flag);
		}
		else if (p == 4) {
			printf("%d\n",g[a[1]][a[2]][a[3]] + a[0] + 1 + flag);
		}
	}
} 
