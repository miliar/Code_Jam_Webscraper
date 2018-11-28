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

const int N = 30;
char f[N][N];



void solve()
{
	int n, m;
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; i++)
		scanf("%s", f[i] );

	for (int it = 0; it < 2; it++)
	{
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j + 1 < m; j++)
				if (f[i][j] != '?' && f[i][j + 1] == '?')
					f[i][j + 1] = f[i][j];
			for (int j = m - 1; j > 0; j--)
				if (f[i][j] != '?' && f[i][j - 1] == '?')
					f[i][j - 1] = f[i][j];
		}
		for (int i = 0; i < max(n, m); i++)
			for (int j = 0; j < i; j++)
				swap(f[i][j], f[j][i] );
		swap(n, m);
	}

	printf("\n");
	for (int i = 0; i < n; i++)
		printf("%s\n", f[i] );
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


