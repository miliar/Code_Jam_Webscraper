#include <bits/stdc++.h>

using namespace std;

struct node{
	int x,y;
	node(){}
	bool operator<(const node& b)const{
		if (x==b.x) return y>b.y;
		return x>b.x;
	}
}a[1010];

int n,k;
const double pi=acos(-1);
double dp[1010][1010];

double gao(int p){
	return pi*a[p].x*a[p].x+pi*2*a[p].x*a[p].y;
}

int main(){
	int T;
	scanf("%d", &T);
	for (int ti=1;ti<=T;ti++){
		scanf("%d%d",&n,&k);
		for (int i=0;i<n;i++){
			scanf("%d%d",&a[i].x,&a[i].y);
		}
		sort(a,a+n);
		memset(dp,0,sizeof(dp));
		dp[0][1]=gao(0);
		for (int i=1;i<n;i++){
			dp[i][1] = max(dp[i-1][1],gao(i));
			for (int j=2;j<=k;j++){
				dp[i][j]=dp[i-1][j];
				double zz= dp[i-1][j-1]+2*pi*a[i].x*a[i].y;
				dp[i][j]=max(dp[i][j], zz);
			}
		}
		double ans=0;
		for (int i=0;i<n;i++)
			for (int j=0;j<=k;j++)
				ans=max(ans,dp[i][j]);
		printf("Case #%d: %.10f\n", ti, ans);
	}
	return 0;
}