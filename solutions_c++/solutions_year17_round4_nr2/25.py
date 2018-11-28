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

const int N = 1005;
int cntMen[N], cntPos[N];


void clear()
{
	memset(cntMen, 0, sizeof cntMen);
	memset(cntPos, 0, sizeof cntPos);
}

int n, c, m;

pair <int, int> solve(int sz)
{
	int over = 0, sum = 0;
	for (int i = n; i >= 1; i--)
	{
		int cur = cntPos[i] + over;
		int nover = max(0, cur - sz);
		sum += max(0, nover - over);
		over = nover;
	}
	return make_pair(over, sum);
}

void solve()
{
	clear();

	scanf("%d%d%d", &n, &c, &m);
	for (int i = 0; i < m; i++)
	{
		int pos, men;
		scanf("%d%d", &pos, &men);
		cntPos[pos]++;
		cntMen[men]++;
	}
	int lb = 1;
	for (int i = 1; i <= c; i++)
		lb = max(lb, cntMen[i] );
	lb--;
	int rb = m;
	while (rb - lb > 1)
	{
		int mb = (lb + rb) / 2;
		pair <int, int> p = solve(mb);
		if (p.first == 0)
			rb = mb;
		else
			lb = mb;
	}
	pair <int, int> p = solve(rb);
	printf("%d %d\n", rb, p.second);
}

void multitest()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int nt;
	scanf("%d", &nt);
	for (int i = 1; i <= nt; i++)
	{
		printf("Case #%d: ", i);
		eprintf("Case #%d .. %d\n", i, nt);
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


