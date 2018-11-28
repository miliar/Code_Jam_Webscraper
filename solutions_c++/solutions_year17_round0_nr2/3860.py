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

char n[40];
char st[40];
bool dp[40][20][2];
int last[40][20][2];
int lastk[40][40][2];

ll recover(int i, int j, int k)
{
	if (i < 0) return 0;
	else
	{
		return 10ll * recover(i - 1, last[i][j][k], lastk[i][j][k]) + j;
	}
}

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

	for (int it = 1; it <= t; ++it)
	{
		scanf("%s", n);
		ll ans = 0;
		
		int k = strlen(n);
		if (k == 1)
		{
			printf("Case #%d: %s\n", it, n);
			continue;
		}
		else
		{
			ans = 0;
			for (int i = 0; i < k - 1; ++i)
				ans = 10 * ans + 9;
			
			memset(dp, 0, sizeof(dp));
			for (int i = 0; i < n[0]; ++i)
			{
				dp[0][i][0] = true;
				last[0][i][0] = -1;
			}
			
			dp[0][n[0]][1] = true;
			last[0][n[0]][1] = -1;

			for (int i = 1; i < k; ++i)
			{
				for (int j = 0; j <= 9; ++j)
				{
					for (int l = 0; l < 2; ++l)
					{
						for (int p = 0; p <= j; ++p)
						{
							for (int q = 0; q < 2; ++q)
							{
								continue;
							}
						}
					}
				}
			}
	
			for (int i = 0; i < k - 1; ++i)
			{
				if (n[i] > n[i + 1])
				{
					--n[i];
					for (int p = i + 1; p < k; ++p)
						n[p] = '9';
					i = -1;
				}
			}
			if (n[0] == '0')
				printf("Case #%d: %s\n", it, n + 1);
			else
				printf("Case #%d: %s\n", it, n);
		}
	}
	
	return 0;
}

