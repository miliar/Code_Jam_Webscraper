#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <assert.h>
#include <algorithm>
#include <iomanip>
#include <time.h>
#include <math.h>
#include <bitset>

#pragma comment(linker, "/STACK:256000000")

using namespace std;

typedef long long int ll;
typedef long double ld;

const int INF = 1000 * 1000 * 1000 + 21;
const ll LLINF = (1ll << 60) + 5;
const int MOD = 1000 * 1000 * 1000 + 7;

int n, k;
char st[228228];

int main()
{
#ifdef CH_EGOR
	freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
#else
	//freopen("", "r", stdin);
	//freopen("", "w", stdout);
#endif 	

	int t;
	scanf("%d", &t);

	for (int _ = 1; _ <= t; ++_)
	{
		int ans = 0;
		scanf("%s %d", st, &k);
		n = strlen(st);

		for (int i = 0; i <= n - k; ++i)
		{
			if (st[i] == '-')
			{
				++ans;
				for (int j = 0; j < k; ++j)
				{
					if (st[i + j] == '+') st[i + j] = '-';
					else st[i + j] = '+';
				}
			}
		}

		bool good = true;
		for (int i = 0; i < n; ++i)
			if (st[i] != '+') good = false;
		
		if (good)
		{
			printf("Case #%d: %d\n", _, ans);
		}
		else
		{
			printf("Case #%d: IMPOSSIBLE\n", _);
		}
	}

	return 0;
}

