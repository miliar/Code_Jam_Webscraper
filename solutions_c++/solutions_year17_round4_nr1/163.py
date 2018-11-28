#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int p;
int dp[4][111][111][111];
int d(int m,int n1,int n2,int n3){
	int&res = dp[m][n1][n2][n3];
	if(res != -1)return res;
	res = 0;
	if(n1)res = max(res, d((m+1)%p,n1-1,n2,n3) + (m==0?1:0));
	if(n2)res = max(res, d((m+2)%p,n1,n2-1,n3) + (m==0?1:0));
	if(n3)res = max(res, d((m+3)%p,n1,n2,n3-1) + (m==0?1:0));
	return res;
}
int main(){
	int _,T;
	scanf("%d",&_);
	for(T=1; T<=_; T++){
		int n;
		scanf("%d%d",&n,&p);
		int r=0,n1=0,n2=0,n3=0;
		for(int i=1; i<=n; i++){
			int x;
			scanf("%d",&x);
			if(x%p==0)r++;else
			if(x%p==1)n1++;else
			if(x%p==2)n2++;else
			if(x%p==3)n3++;
		}
		memset(dp,-1,sizeof(dp));
		printf("Case #%d: %d\n",T,d(0,n1,n2,n3)+r);
	}
	return 0;
}
