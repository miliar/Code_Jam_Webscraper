#include <stdio.h>

int max[100],speed[100];
int dist[100];
double dp[100];

FILE* in = fopen("C-small-attempt0.in","r");
FILE* out = fopen("C-small-attempt0.out","w");

void solve()
{
	int n,q,i,j;
	double t;
	fscanf(in,"%d %d",&n,&q);
	for(i=0;i<n;i++)
		fscanf(in,"%d %d",max+i,speed+i);
	
	for(i=0;i<n;i++) for(j=0;j<n;j++)
	{
		fscanf(in,"%d",&q);
		if(i+1==j) dist[i]=q;
	}
	fscanf(in,"%d %d",&i,&j);
	
	for(i=0;i<n;i++) dp[i]=0;
	
	
	long long sum;
	for(i=0;i<n-1;i++)
	{
		sum=0;
		for(j=i;j<n-1;j++)
		{
			sum+=dist[j];
			if(sum>max[i]) break;
			
			t=dp[i]+(double)sum/speed[i];
			if(dp[j+1]==0 || dp[j+1]>t) dp[j+1]=t;
		}
	}
	fprintf(out,"%lf\n",dp[n-1]);
}

int main()
{
	int i,T;
	fscanf(in,"%d",&T);
	for(i=1;i<=T;i++)
	{
		fprintf(out,"Case #%d: ",i);
		solve();
	}
}
