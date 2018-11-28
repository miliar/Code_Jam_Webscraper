#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <cassert>
#include <numeric>
#include <string>
#include <cstring>
#include <cmath>
using namespace std;

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif

typedef long long int int64;

map <long long, long long> len2cnt;

void solve()
{
	len2cnt.clear();
	long long n, k;
	scanf("%lld%lld", &n, &k);
	len2cnt[n]++;
	
	while (true)
	{
		auto p = *len2cnt.rbegin();
		len2cnt.erase(p.first);
		long long len = p.first;
		long long cnt = p.second;
		if (cnt >= k)
		{
			printf("%lld %lld\n", len / 2, (len - 1) / 2);
			break;
		}
		k -= cnt;
		len2cnt[len / 2] += cnt;
		len2cnt[(len - 1) / 2] += cnt;
	}
}

void multitest()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		printf("Case #%d: ", i);
		eprintf("Case #%d .. %d\n", i, n);
		solve();
	}


}

int main(int argc, char **)
{
	if (argc == 1)
		multitest();
	else
		solve();

	return 0;
}


