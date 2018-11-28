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


const int N = 55;
int R[N];
int Q[N][N];

bool used[N][N];
const int MX = (int) 1e6;
int ch[N];

bool good(long long correct, long long have)
{
	return correct * 90 <= have * 100 && correct * 110 >= have * 100;
}

void solve()
{
	memset(used, false, sizeof used);
	int n, p;
	scanf("%d%d", &n, &p);
	for (int i = 0; i < n; i++)
		scanf("%d", &R[i] );
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < p; j++)
			scanf("%d", &Q[i][j] );
		sort(Q[i], Q[i] + p);
	}
	int ans = 0;
	for (int x = 1; x <= MX; x++)
	{
		while (true)
		{
			bool win = true;
			for (int i = 0; i < n; i++)
			{
				win = false;
				for (int j = 0; j < p; j++)
					if (!used[i][j] && good(R[i] * 1LL * x, Q[i][j] ) )
					{
						win = true;
						ch[i] = j;
						break;
					}
				if (!win) break;
			}
			if (!win) break;
			for (int i = 0; i < n; i++)
				used[i][ch[i] ] = true;
			ans++;
		}
	}
	printf("%d\n", ans);
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


