#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <queue>

#define TEST_NUM "cc"
//#define DEBUGGGGGGGGGGGGGGGGGGGGGGGGGG

int e[110];
int s[110];
int d[110][110];
long long t[110][110];
double tt[110][110];
int qq[110][2];

const long long MAX = 1000000000000;

void process()
{
	int n, q, i, j, k;
	scanf("%d%d", &n, &q);
	for (i = 1; i <= n; i++)
		scanf("%d%d", &e[i], &s[i]);

	for (i = 1; i <= n; i++)
		for (j = 1; j <= n; j++)
			scanf("%d", &d[i][j]);

	for (i = 0; i < q; i++)
		scanf("%d%d", &qq[i][0], &qq[i][1]);

	for (i = 1; i <= n; i++)
		for (j = 1; j <= n; j++)
			t[i][j] = d[i][j] == -1 ? MAX : d[i][j];

	for (k = 1; k <= n; k++)
		for (i = 1; i <= n; i++)
			for (j = 1; j <= n; j++)
				t[i][j] = std::min(t[i][j], t[i][k] + t[k][j]);

	for (i = 1; i <= n; i++)
		for (j = 1; j <= n; j++)
			tt[i][j] = t[i][j] > e[i] ? MAX : 1.0 * t[i][j] / s[i];

	for (k = 1; k <= n; k++)
		for (i = 1; i <= n; i++)
			for (j = 1; j <= n; j++)
				tt[i][j] = std::min(tt[i][j], tt[i][k] + tt[k][j]);

	for (i = 0; i < q; i++)
		printf("%.10lf ", tt[qq[i][0]][qq[i][1]]);
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