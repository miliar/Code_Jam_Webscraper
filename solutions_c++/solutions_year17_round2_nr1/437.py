#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>

#define TEST_NUM "aa"
//#define DEBUGGGGGGGGGGGGGGGGGGGGGGGGGG

int k[1010];
int s[1010];


void process()
{
	int d, n, i, j;
	double res;
	scanf("%d%d", &d, &n);
	for (i = 0; i < n; i++)
		scanf("%d%d", &k[i], &s[i]);

	res = 1.0 * (d - k[0]) / s[0];

	for (i = 1; i < n; i++)
		res = std::max(res, 1.0 * (d - k[i]) / s[i]);

	printf("%.10lf", 1.0 * d/res);
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
	for (ti = 1; ti <= tn; ti++)
	{
		fprintf(stderr, "Case %d/%d\n", ti, tn);
		printf("Case #%d: ", ti);
		process();
		printf("\n");
	}
	return 0;
}