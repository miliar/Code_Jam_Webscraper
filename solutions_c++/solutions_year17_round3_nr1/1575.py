#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <unordered_map>
using namespace std;

const double PI = 2.0 * acos(0.0);

FILE* in = fopen("input.in", "r");
FILE* out = fopen("output.out", "w");


double solve();

int main()
{
	int T;	fscanf(in, "%d", &T);
	for (int tc = 1; tc <= T; ++tc)
	{
		fprintf(out, "Case #%d: %.9lf\n", tc, solve());
	}
}

double solve()
{
	long long ret = 0;
	int N, K; fscanf(in, "%d %d", &N, &K);
	vector<pair<long long,long long> > RH;
	for (int i = 0; i < N; ++i)
	{
		long long a, b;	fscanf(in, "%lld %lld", &a, &b);
		RH.push_back(make_pair(a, b));
	}
	sort(RH.begin(), RH.end());
	vector<long long> RHS;
	for (int i = 0; i < K - 1; ++i)	RHS.push_back(-2*RH[i].first*RH[i].second);
	for (int i = K - 1; i < N; ++i)
	{
		long long tmp = -RH[i].first*RH[i].first - 2*RH[i].first*RH[i].second;
		sort(RHS.begin(), RHS.end());
		for (int j = 0; j < K-1; ++j)
			tmp += RHS[j];
		ret = max(ret, -tmp);
		RHS.push_back(-2*RH[i].first*RH[i].second);
	}
	return PI*ret;
}
