#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ULL;

ULL calcGroup(ULL k)
{
	int x = 63;
	while((k >> x) != ULL(1)) --x;
	return x;
}

pair<ULL, ULL> getRes(int gidx)
{
	if(gidx == 1) return make_pair(0, 0);
	else
	{
		ULL u1 = gidx / 2;
		ULL u2;
		if(gidx % 2 == 0) u2 = u1 - 1;
		else u2 = u1;
		return make_pair(u1, u2);
	}
}

int main()
{
	int t;
	scanf("%d", &t);
	ULL n, k;
	for(int i = 0; i != t; ++i)
	{
		scanf("%llu %llu", &n, &k);
		ULL grouplen = (ULL)1 << calcGroup(k);
		ULL gidx = (n - k + 1) / grouplen;
		if((n - k + 1) % grouplen != 0) ++gidx;
		auto res = getRes(gidx);
		printf("Case #%d: %llu %llu\n", i + 1, res.first, res.second);
	}
	return 0;
}
