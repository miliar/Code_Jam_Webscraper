#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <iostream>
using namespace std;

int main()
{
	int t, i;
	long long int n, k, stage, n1p, n2p, n1, n2, n1count, n2count, count, temp1, temp2, temp1count, temp2count;
	scanf("%d\n", &t);
	for(i=1;i<=t;i++)
	{
		scanf("%lld %lld\n", &n, &k);
		stage = 1;
		count = 1;
		n1 = n;
		n1count = 1;
		n2 = -1;
		n2count = 0;
		while(count<k)
		{
			if(n2 == -1)
			{
				temp1 = n1/2;
				temp1count = n1count;
				temp2 = n1-n1/2-1;
				temp2count = n1count;
				if(temp2==temp1)
				{
					temp2 = -1;
					temp1count += temp2count;
					temp2count = 0;
				}
				n1 = temp1;
				n2 = temp2;
				n1count = temp1count;
				n2count = temp2count;
				stage *= 2;
				count += stage;
			}
			else
			{
				if(n1%2)
				{
					temp1 = n1/2;
					temp1count = 2*n1count + n2count;
					temp2 = n2-n2/2-1;
					temp2count = n2count;
					n1 = temp1;
					n2 = temp2;
					n1count = temp1count;
					n2count = temp2count;
					stage *= 2;
					count += stage;
				}
				else
				{
					temp1 = n1/2;
					temp1count = n1count;
					temp2 = n2/2;
					temp2count = n1count + 2*n2count;
					n1 = temp1;
					n2 = temp2;
					n1count = temp1count;
					n2count = temp2count;
					stage *= 2;
					count += stage;
				}
			}
		}

		printf("Case #%d: ", i);
		if(k-(count-stage) <= n1count)
		{
			
			printf("%lld %lld", n1/2, n1-n1/2-1);
		}
		else
		{
			printf("%lld %lld", n2/2, n2-n2/2-1);
		}
		printf("\n");
	}

	return 0;
}
