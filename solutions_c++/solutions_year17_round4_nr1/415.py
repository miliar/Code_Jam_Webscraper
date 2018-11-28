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
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
#define MEM(x, y) memset((x),(y),sizeof(x))
const LL INF = 1e9 + 7;
const int N = 1e2 + 10;
int dp[N][N][N][4][5];
int getans(int x, int y, int z, int o, int mod)
{
	if (x == 0 && y == 0 && z == 0) return 0;
	if (dp[x][y][z][o][mod] != -1) return dp[x][y][z][o][mod];
	int &ret = dp[x][y][z][o][mod] = 0;
	int tmp = 0;
	if (x > 0) tmp = max(tmp, getans(x - 1, y, z, (1 + o) % mod, mod));
	if (y > 0) tmp = max(tmp, getans(x, y - 1, z, (2 + o) % mod, mod));
	if (z > 0) tmp = max(tmp, getans(x, y, z - 1, (3 + o) % mod, mod));
	if (o == 0) tmp++;
	ret = tmp;
	return ret;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int ncase;
	scanf("%d", &ncase);
	MEM(dp, -1);
	int ks = 1;
	while (ncase--)
	{
		int n, mod;
		int a[5];
		scanf("%d%d", &n, &mod);
		MEM(a, 0);
		for (int i = 0; i < n; i++)
		{
			int x;
			scanf("%d", &x);
			a[x%mod]++;
		}
		printf("Case #%d: %d\n", ks++, a[0] + getans(a[1], a[2], a[3], 0, mod));
	}
	return 0;
}