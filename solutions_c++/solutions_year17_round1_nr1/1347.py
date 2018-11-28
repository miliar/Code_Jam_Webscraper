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

int n, m;
char st[30][30];



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
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i)
			scanf("%s", st[i]);
		
		int x, y;
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < m; ++j)
			{
				if (st[i][j] != '?')
				{
					x = i;
					y = j;
					goto kek;
				}
			}
		}
		kek:;
		for (int i = x; i < n; ++i)
		{
			if (i == x)
			{
				for (int j = 0; j < m; ++j)
				{
					if (st[i][j] == '?')
					{
						for (int k = j; k < m; ++k)
						{
							if (st[i][k] != '?')
							{
								st[i][j] = st[i][k];
								break;
							}
						}
					}
					if (st[i][j] == '?')
					{
						for (int k = j; k >= 0; --k)
						{
							if (st[i][k] != '?')
							{
								st[i][j] = st[i][k];
								break;
							}
						}
					}
				}
			}
			else
			{
				bool ok = true;
				for (int j = 0; j < m; ++j)
				{
					if (st[i][j] != '?') ok = false;
				}
				if (ok)
				{
					for (int j = 0; j < m; ++j)
					{
						st[i][j] = st[i - 1][j];
					}
				}
				else
				{
	for (int j = 0; j < m; ++j)
				{
					if (st[i][j] == '?')
					{
						for (int k = j; k < m; ++k)
						{
							if (st[i][k] != '?')
							{
								st[i][j] = st[i][k];
								break;
							}
						}
					}
					if (st[i][j] == '?')
					{
						for (int k = j; k >= 0; --k)
						{
							if (st[i][k] != '?')
							{
								st[i][j] = st[i][k];
								break;
							}
						}
					}
				}
				}
			}
		}

for (int i = x; i >=0; --i)
		{
			if (i == x)
			{
				for (int j = 0; j < m; ++j)
				{
					if (st[i][j] == '?')
					{
						for (int k = j; k < m; ++k)
						{
							if (st[i][k] != '?')
							{
								st[i][j] = st[i][k];
								break;
							}
						}
					}
					if (st[i][j] == '?')
					{
						for (int k = j; k >= 0; --k)
						{
							if (st[i][k] != '?')
							{
								st[i][j] = st[i][k];
								break;
							}
						}
					}
				}
			}
			else
			{
				bool ok = true;
				for (int j = 0; j < m; ++j)
				{
					if (st[i][j] != '?') ok = false;
				}
				if (ok)
				{
					for (int j = 0; j < m; ++j)
					{
						st[i][j] = st[i + 1][j];
					}
				}
				else
				{
	for (int j = 0; j < m; ++j)
				{
					if (st[i][j] == '?')
					{
						for (int k = j; k < m; ++k)
						{
							if (st[i][k] != '?')
							{
								st[i][j] = st[i][k];
								break;
							}
						}
					}
					if (st[i][j] == '?')
					{
						for (int k = j; k >= 0; --k)
						{
							if (st[i][k] != '?')
							{
								st[i][j] = st[i][k];
								break;
							}
						}
					}
				}
				}
			}
		}
	
		printf("Case #%d:\n", it);
		for (int i = 0; i < n; ++i)
			printf("%s\n", st[i]);
	}

	return 0;
}

