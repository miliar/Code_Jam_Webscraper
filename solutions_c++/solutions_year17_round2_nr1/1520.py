#include <stdio.h>
#include <bits/stdc++.h>
#define ll long long
#define ull unsigned long long
using namespace std;
const int N = 1500;
int f(int w)
{

}

int main()
{
	int i, t, k;
	char s[N];
	scanf("%d", &t);
	for (i = 0; i < t; i++)
	{
		int d, n;
		double bestTime = -1.0;
		scanf("%d %d", &d, &n);
		for (auto j = 0; j < n; j++)
		{
			int k, s;
			scanf("%d %d", &k, &s);
			int dist = d - k;
			long double time = static_cast<long double >(dist) / static_cast<long double >(s);
			if (time > bestTime)
				bestTime = time;
		}
		long double ans = d / bestTime;
		printf("Case #%d: %.15lf\n", i + 1, ans);
	}
	return 0;
}
// s = v*t;