#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <iostream>
using namespace std;

int main()
{
	int t, i, n, s;
	long long int k, d;
	scanf("%d\n", &t);
	double time, max;
	for(i=1;i<=t;i++)
	{
		scanf("%lld %d\n", &d, &n);
		max = 0;
		for(int j=0; j<n; j++)
		{
			scanf("%lld %d\n", &k, &s);
			time = (float)(d-k)/(float)s;
			if(time>max)
				max = time;
		}

		printf("Case #%d: ", i);
		printf("%.6lf", (float)d/max);
		printf("\n");
	}

	return 0;
}
