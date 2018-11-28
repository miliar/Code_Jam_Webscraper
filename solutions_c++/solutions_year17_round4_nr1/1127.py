#include<bits/stdc++.h>
#include <unistd.h>
using namespace std;

#define sd(a) scanf("%d",&a)
#define ss(a) scanf("%s",&a)
#define sl(a) scanf("%lld",&a)
#define clr(a) memset(a,0,sizeof(a))
#define debug(a) printf("check%d\n",a)
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define ll long long
#define mod 1000000007 
#define N 10010

int dp[4][110][110][110];
int cnt[4];

int main()
{
	// freopen("A1.in","r",stdin);
	// freopen("A1.out","w",stdout);
	int t,i,j,k,l;
	
	sd(t);
	for(int tt=1;tt<=t;tt++)
	{
		clr(dp);
		clr(cnt);
		int n,p;
		sd(n);sd(p);

		for(i=0;i<n;i++)
		{
			int x;
			sd(x);
			x%=p;
			cnt[x]++;
		}

		
		for(i=0;i<=cnt[1];i++)
		for(j=0;j<=cnt[2];j++)
		for(k=0;k<=cnt[3];k++)
		for(l=0;l<p;l++)
		{
			if(i)
				dp[l][i][j][k] = max(dp[l][i][j][k],dp[(l+1)%p][i-1][j][k] + (l==0?1:0));
			if(j)
				dp[l][i][j][k] = max(dp[l][i][j][k],dp[(l+2)%p][i][j-1][k] + (l==0?1:0));
			if(k)
				dp[l][i][j][k] = max(dp[l][i][j][k],dp[(l+3)%p][i][j][k-1] + (l==0?1:0));

		}

		printf("Case #%d: %d\n",tt,dp[0][cnt[1]][cnt[2]][cnt[3]]+cnt[0]);
	}
}