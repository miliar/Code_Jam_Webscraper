#include<stdio.h>
int main()
{
	long long int d,s,p,n,t;
	double max,r;
	int i,j=0;
	scanf("%lld",&t);
	while(t--)
	{
		j++;
		max=0.0;
		scanf("%lld%lld",&d,&n);
		for(i=0;i<n;i++)
		{
			scanf("%lld%lld",&p,&s);
			r=(d-p)/(double)s;
			if(r>max)
			max=r;
		}
		printf("Case #%d: %.6lf\n",j,d/(double)max);
	}
}
