#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
#include <cassert>
#include <iterator>
#include <complex>
#include <random>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
#define MEM(x, y) memset((x),(y),sizeof(x))
const LL INF = 1e9 + 7;
const int N = 1e2 + 10;
int a[N][N];
double d[N][N];
int dis[N];
int speed[N];
template <typename Type>
void floyd(int n, Type T[N][N])
{
	for (int k = 1; k <= n; k++)
	{
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= n; j++)
			{
				T[i][j] = min(T[i][j], T[i][k] + T[k][j]);
			}
		}
	}
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int ncase;
	scanf("%d", &ncase);
	int ks = 1;
	while (ncase--)
	{
		int n, q;
		scanf("%d%d", &n, &q);
		MEM(d, 0x60);
		for (int i = 1; i <= n; i++)
		{
			scanf("%d%d", &dis[i], &speed[i]);
		}
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= n; j++)
			{
				scanf("%d", &a[i][j]);
				if (a[i][j] == -1) a[i][j] = 0x3f3f3f3f;
			}
		}
		floyd(n, a);
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= n; j++)
			{
				if (a[i][j] <= dis[i])
				{
					d[i][j] = min(d[i][j], 1.0*a[i][j] / speed[i]);
				}
			}
		}
		floyd(n, d);
		printf("Case #%d:", ks++);
		while (q--)
		{
			int u, v;
			scanf("%d%d", &u, &v);
			printf(" %.15f", d[u][v]);
		}
		puts("");
	}
	return 0;
}