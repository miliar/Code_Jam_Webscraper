#include<stdio.h>
#include<queue>
#define PI 3.1415926535897932384626433832795

using namespace std;

priority_queue<double> Q;

int n, k;
double dy[1005][1005];
double r[1005];
double h[1005];

int main(void)
{
	int t, T, i, j, l;
	double tmp;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%d %d",&n,&k);
		for(i=1;i<=n;i++)
			scanf("%lf %lf",&r[i], &h[i]);

		for(i=1;i<=n;i++)
		{
			for(j=i+1;j<=n;j++)
			{
				if(r[i]>r[j])
				{
					tmp = r[i];
					r[i]=r[j];
					r[j]=tmp;
					tmp = h[i];
					h[i]=h[j];
					h[j]=tmp;
				}
			}
		}

		double sum, ans=0;
		for(i=k;i<=n;i++)
		{
			while(!Q.empty())
				Q.pop();

			for(j=1;j<i;j++)
				Q.push(2*PI*h[j]*r[j]);

			sum = PI * r[i]*r[i] + 2*PI*h[i]*r[i];
			for(j=1;j<k;j++)
			{
				sum+=Q.top();
				Q.pop();
			}
			
			if(ans<sum)
				ans=sum;
		}

		printf("Case #%d: %.9lf\n",t,ans);
	}
}