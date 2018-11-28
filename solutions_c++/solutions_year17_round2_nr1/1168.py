#include<stdio.h>
int main()
{
	int i, j, t, d, n, k, s;
	double m;
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		scanf("%d %d",&d, &n);
		m=0;
		for(j=0;j<n;j++)
		{
			scanf("%d %d", &k, &s);
			if(m<(d-k)/(double)s)
				m=(d-k)/(double)s;
		}
		printf("Case #%d: %f\n",i+1, d/m);
	}

	return 0;
}
