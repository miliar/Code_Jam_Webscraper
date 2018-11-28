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
const int N = 1e3 + 10;
int cnt[N];
vector<int> v[N];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int ncase;
	scanf("%d", &ncase);
	int ks = 1;
	while (ncase--)
	{
		int n, m, c;
		scanf("%d%d%d", &n, &m, &c);
		int cur = 0;
		int rest = 0;
		for (int i = 1; i <= 1000; i++) v[i].clear();
		for (int i = 1; i <= c; i++)
		{
			int x, y;
			scanf("%d%d", &x, &y);
			v[x].push_back(y);
		}
		int l = 1, r = 1000;
		auto check = [&](int mid) -> int
		{
			MEM(cnt, 0);
			int rest = 0;
			int ret = 0;
			for (int i = 1; i <= n; i++)
			{
				int k = 0;
				for (auto &x : v[i])
				{
					if (cnt[x] == mid) return -1;
					if (k < mid) cnt[x]++;
					else if (rest == 0) return -1;
					else rest--, ret++, cnt[x]++;
					k++;
				}
				rest += mid - min(mid, k);
			}
			return ret;
		};
		int ans = r;
		while (l <= r)
		{
			int mid = (l + r) / 2;
			if (check(mid) != -1) ans = mid, r = mid - 1;
			else l = mid + 1;
		}
		printf("Case #%d: %d %d\n", ks++, ans, check(ans));
	}
	return 0;
}