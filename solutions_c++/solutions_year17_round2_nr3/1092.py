#include<stdio.h>
#include<float.h>

double minz(double a, double b)
{
	if(a<b)
		return a;
	return b;
}

int main()
{
	int i, j, k, t, n, q, e[100], s[100], d[100][100], uv[100][2], dist;
	double min[100];
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		scanf("%d %d",&n, &q);
		for(j=0;j<n;j++)
			min[j]=DBL_MAX;
		for(j=0;j<n;j++)
			scanf("%d %d", e+j, s+j);
		for(j=0;j<n;j++)
		{
			for(k=0;k<n;k++)
				scanf("%d",&(d[j][k]));
		}
		for(j=0;j<q;j++)
			scanf("%d %d",uv[j], uv[j]+1);
		min[n-1]=0;
		min[n-2]=d[n-2][n-1]/(double)s[n-2];
		for(j=n-2;j>=0;j--)
		{
			dist=0;
			for(k=j+1;k<=n;k++)
			{
				dist+=d[k-2][k-1];
				if(dist<=e[j-1])
					min[j-1]=minz(min[j-1],min[k-1]+dist/(double)s[j-1]);
				else
					break;
			}
		}		
		printf("Case #%d: %f\n", i+1, min[0]);
	}

	return 0;
}
