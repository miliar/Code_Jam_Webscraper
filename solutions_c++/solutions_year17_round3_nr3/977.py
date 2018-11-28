#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <algorithm>
using namespace std;
#define NMAX 2000
int main()
{
	int t, i, j, n, k;
	long long int h[NMAX], r[NMAX], rmax, rh[NMAX];
	double max, sum;
	scanf("%d\n", &t);
	for(i=1;i<=t;i++)
	{
		scanf("%d %d\n", &n, &k);
		for(j=0;j<n;j++)
			scanf("%lld %lld\n", &(r[j]), &(h[j]));

		max = 0;
		for(j=0;j<n;j++)
		{
			rmax = r[j];
			int ptr = 0;
			for(int j1=0;j1<n;j1++)
				if(j1!=j && r[j1]<=rmax)
				{
					rh[ptr] = r[j1]*h[j1];
					ptr++;
				}
			sum = 0;
			if(ptr>=k-1)
			{
				sort(rh, rh + ptr);
				for(int j1=ptr-1;ptr-j1<k;j1--)
					sum += rh[j1];
			}
			if(M_PI*(rmax*rmax + 2*r[j]*h[j] + 2*sum) > max)
				max = M_PI*(rmax*rmax + 2*r[j]*h[j] + 2*sum);
		}
		printf("Case #%d: ", i);
		printf("%.9lf", max);
		printf("\n");
	}

	return 0;
}
