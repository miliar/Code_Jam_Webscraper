#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std;

struct THorse
{
	int k, s;
};

int D, N;
THorse h[1010];

bool Cmp(const THorse& A, const THorse& B)
{
	return A.k > B.k;
}

void Work()
{
	scanf("%d%d", &D, &N);
	for (int i = 0; i < N; i ++)
		scanf("%d%d", &h[i].k, &h[i].s);
	sort(h, h + N, Cmp);
	double duringtime = (D - h[0].k) / (double) h[0].s;
	double limitpos = D;
	double lastspeed = h[0].s;
	double Ans = limitpos / (double) duringtime;
	for (int i = 1; i < N; i ++)
	{
		duringtime = (D - h[i].k) / (double) h[i].s;
		limitpos = D;
		lastspeed = h[i].s;
		Ans = min(Ans, limitpos / (double) duringtime);
	}
	printf("%.6lf\n", Ans);
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; Case ++)
	{
		printf("Case #%d: ", Case);
		fprintf(stderr, "Case #%d: \n", Case);
		Work();
		fflush(stdout);
	}
	return 0;
}