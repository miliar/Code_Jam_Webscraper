
#include "stdafx.h"
#include <bits\stdc++.h>
#include <algorithm>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define LOCAL_TEST false

using namespace std;

set<long long> occupied;

void calculate(long long n, long long k, long long &maxMin, long long &maxMax)
{
	for (int i = 0; i < k; ++i)
	{
		int index = 0;
		maxMin = 0;
		maxMax = 0;
		for (set<long long>::iterator it = occupied.begin(); it != (--occupied.end());)
		{
			long long start = *it;
			long long end = *(++it);
			long long mid = start + (end - start) / 2;
			long long L = mid - start - 1;
			long long R = end - mid - 1;
			long long minLR = min(L, R);
			long long maxLR = max(L, R);
			if (maxMin < minLR || (maxMin == minLR && maxMax < maxLR))
			{
				maxMin = minLR;
				maxMax = maxLR;
				index = mid;
			}
		}
		occupied.insert(index);
	}
}

void solve()
{
	long long n, k, maxMin = 0, maxMax = 0;
	cin >> n >> k;
	occupied.clear();
	occupied.insert(0);
	occupied.insert(n + 1);
	calculate(n, k, maxMin, maxMax);
	cout << maxMax << " " << maxMin << endl;
}

int MAIN()
{
	int TestCase;
	cin >> TestCase;
	for (int caseID = 1; caseID <= TestCase; caseID++)
	{
		cout << "Case #" << caseID << ": ";
		solve();
	}
	return 0;
}

int main()
{
	int start = clock();
#if LOCAL_TEST
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	cout << fixed << setprecision(16);
	int ret = MAIN();
#if LOCAL_TEST
	//cout << "[Finished in " << clock() - start << " ms]" << endl;
#endif
	return ret;
}

