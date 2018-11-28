#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long int llu;

int isOK(llu num, llu n)
{
	llu temp=num;
	llu base=10e+18;
	llu gene=0;
	int cur_max=0;
	int cur;

	while(base)
	{
		cur=temp/base;

		if(cur>cur_max)
			cur_max=cur;
		
		gene=gene*10+cur_max;
		temp=temp%base;
		base/=10;
	}

	//printf("!%llu\n",gene);

	if(gene<=n)
		return 1;

	return 0;
}

llu find(llu num)
{
	llu temp=num;
	llu base=10e+18;
	llu gene=0;
	int cur_max=0;
	int cur;

	while(base)
	{
		cur=temp/base;

		if(cur>cur_max)
			cur_max=cur;
		
		gene=gene*10+cur_max;
		temp=temp%base;
		base/=10;
	}

	return gene;
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		llu n;
		llu step=1l<<63;
		scanf("%llu",&n);
		//printf("%llu\n",step);
		llu temp=0;
		while(step)
		{
			if(step+temp>n)
			{
				step>>=1;
				continue;
			}

			//printf("#%llu\n",step+temp);

			if(isOK(step+temp,n))
			{
				temp+=step;
			}

			step>>=1;
		}

		printf("Case #%d: %llu",t,find(temp));

		if(t!=T) printf("\n");

	}

	return 0;
}