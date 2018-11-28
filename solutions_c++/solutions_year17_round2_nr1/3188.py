#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

FILE* in = fopen("input.in", "r");
FILE* out = fopen("output.out", "w");

int D, N;
vector<int> S, V;

double solve();
bool decision(double);
void init()
{
	S.clear();	V.clear();
	fscanf(in, "%d %d", &D, &N);
	S.resize(N); V.resize(N);
	for (int i = 0; i < N; ++i)
	{
		fscanf(in,"%d %d", &S[i], &V[i]);
	}
}

int main()
{
	int T;	fscanf(in, "%d", &T);
	for (int tc = 1; tc <= T; ++tc)
	{
		fprintf(out,"Case #%d: %.6lf\n", tc, solve());
	}
}


double solve()
{
	init();
	double lo = -1, hi = 1e15;
	for (int iter = 0; iter < 100; ++iter)
	{
		double mid = (lo + hi) / 2;
		if (decision(mid))	lo = mid;
		else
		{
			hi = mid;
		}
	}
	return lo;
}

bool decision(double d)
{
	for (int i = 0; i < N; ++i) 
	{
		if (((double)(D - S[i])/V[i])*d > D)	return false;
	}
	return true;
}