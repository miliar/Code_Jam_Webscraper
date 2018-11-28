#include <iostream>
#include <algorithm> 
#include <queue>
#include <vector>
#include <string>
#include <string.h>
#include <stdlib.h>
#include <map>
using namespace std;

struct mode
{
	int e,s;
};

double min(double a,double b)
{
	if(a<b) return a;
	return b;
}

int city[100][100];
int sum[100];
mode horse[100];
double dp[100][100];

int main()
{
	int T,n,q,i,j,u,v,x=0;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d",&n,&q);
		for(i=0;i<n;i++) scanf("%d%d",&horse[i].e,&horse[i].s);
		for(i=0;i<n;i++)
			for(j=0;j<n;j++) scanf("%d",&city[i][j]);
		for(i=1,sum[0]=0;i<n;i++) sum[i]=sum[i-1]+city[i-1][i];
		while(q--) scanf("%d%d",&u,&v);
		for(i=0;i<n;i++)
			for(j=0;j<i;j++) dp[i][j]=100000000000000;
		for(j=1,dp[0][0]=0;j<n;j++)
			if(horse[0].e>=sum[j]) dp[0][j]=dp[0][j-1]+city[j-1][j]/(double)horse[0].s;
			else dp[0][j]=100000000000000;
		for(i=1;i<n;i++)
		{
			dp[i][i]=100000000000000;
			for(j=0;j<i;j++) dp[i][i]=min(dp[i][i],dp[j][i]);
			for(j=i+1;j<n;j++)
				if(horse[i].e>=sum[j]-sum[i]) dp[i][j]=dp[i][j-1]+city[j-1][j]/(double)horse[i].s;
				else dp[i][j]=100000000000000;
		}
		/*for(i=0;i<n;printf("\n"),i++)
			for(j=0;j<n;j++) printf("dp[%d][%d]=%.6lf ",i,j,dp[i][j]);*/
		printf("Case #%d: %.6lf\n",++x,dp[n-1][n-1]);
	}
}
