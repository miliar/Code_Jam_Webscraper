#include <stdio.h>
#include <algorithm>
using namespace std;

double m[50];

int main()
{
	int t,x=0,n,k,i,j;
	double u;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d%lf",&n,&k,&u);
		for(i=0;i<n;i++) scanf("%lf",&m[i]);
		sort(m,m+n);
		for(i=1;i<n;i++)
		{
			if(u>=(m[i]-m[i-1])*(double)i)
				for(u-=(m[i]-m[i-1])*(double)i,j=0;j<i;j++) m[j]=m[i];
			else
			{
				for(j=0;j<i;j++)
					m[j]+=u/(double)i;
				u=0;
				break;
			}
		}
		if(u>0)
		{
			for(i=0;i<n;i++)
				m[i]+=u/(double)n;
		}
		for(u=1,i=0;i<n;i++) u*=m[i];
		printf("Case #%d: %.6lf\n",++x,u);
	}
}
