#include <bits/stdc++.h>
using namespace std;
int num[2][9][2];
int dp[1<<9][1<<9];
int n,p;

int rec(int x, int y) {
	if (dp[x][y]!=-1) return dp[x][y];
	vector<int> v;
	dp[x][y]=0;
	//printf("%d %d\n", x, y);
	for (int i=0; i<p; i++) {
		if ((1<<i) & x) continue;
		if (num[0][i][0]>num[0][i][1]) continue;
		v.push_back(i);
		if (n==1) {
			dp[x][y]=max(dp[x][y],1+rec((1<<i)|x,0));
		}
	}
	if (n==1) return dp[x][y];
	for (int i=0; i<p; i++) {
		if ((1<<i) & y) continue;
		if (num[1][i][0]>num[1][i][1]) continue;
		for (int j=0; j<v.size(); j++) {
			if (num[1][i][0]<=num[0][v[j]][0] && num[1][i][1]>=num[0][v[j]][0]) {
				dp[x][y]=max(dp[x][y],1+rec((1<<v[j])|x,(1<<i)|y));
			}
			else if (num[1][i][0]<=num[0][v[j]][1] && num[1][i][0]>=num[0][v[j]][0]) {
				dp[x][y]=max(dp[x][y],1+rec((1<<v[j])|x,(1<<i)|y));
			}
		}
	}
	return dp[x][y];
}

int main() {
	int tc;
	scanf("%d", &tc);
	for (int t=1; t<=tc; t++) {
		scanf("%d%d", &n, &p);
		int r[n];
		for (int i=0; i<n; i++) scanf("%d", &r[i]);
		int q[n][p];
		for (int i=0; i<n; i++) {
			for (int j=0; j<p; j++) scanf("%d", &q[i][j]);
		}
		for (int i=0; i<n; i++) {
			for (int j=0; j<p; j++) {
				int tot=q[i][j];
				int upp=(tot*10)/(r[i]*9);
				int low=ceil((double)(tot*10)/((double)(r[i]*11)));
				num[i][j][0]=low, num[i][j][1]=upp;
				//printf("%d %d %d\n", j, low, upp);
			}
		}
		memset(dp,-1,sizeof(dp));
		printf("Case #%d: %d\n", t, rec(0,0));
		/*for (int i=0; i<1<<p; i++) {
			for (int j=0; j<1<<p; j++) printf("%d ", dp[i][j]);
			printf("\n");
		}*/
	}
}
