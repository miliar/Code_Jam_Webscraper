#include <stdio.h>
#include <string.h>
#include <algorithm>

#define TEST_NUM "ccc"
//#define DEBUGGGGGGGGGGGGGGGGGGGGGGGGGG

void process()
{
	long long n, k, l, c1, c2, t, r;
	scanf("%lld%lld", &n, &k);

	l = n;
	c1 = 1;
	c2 = 0;
	r = 0;

	while(1)
	{
		if(r+c1+c2 < k)
		{
			t = c1+c2;
			r += t;

			if(l%2)
				c1 += t;
			else
				c2 += t;

			l /= 2;
		}
		else if(r+c1 < k)
		{
			printf("%lld %lld", (l-1)/2, (l-2)/2);
			return;
		}
		else
		{
			printf("%lld %lld", l/2, (l-1)/2);
			return;
		}
	}
}

void pre_process()
{

}

int main()
{
#ifndef DEBUGGGGGGGGGGGGGGGGGGGGGGGGGG
#ifdef _DEBUG
	fprintf(stderr, "\nYou are using DEBUG MODE!!!\n\n");
#endif
	char inname[100];
	char outname[100];
	sprintf(inname, "%s.in", TEST_NUM);
	sprintf(outname, "%s.out", TEST_NUM);
	freopen(inname, "r", stdin);
	freopen(outname, "w", stdout);
#endif
	int tn, ti;
	scanf("%d", &tn);
	pre_process();
	for(ti = 1; ti<=tn; ti++)
	{
		fprintf(stderr, "Case %d/%d\n", ti, tn);
		printf("Case #%d: ", ti);
		process();
		printf("\n");
	}
	return 0;
}