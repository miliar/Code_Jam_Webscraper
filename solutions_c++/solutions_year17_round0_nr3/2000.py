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
const int N = 2e5 + 10;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int ncase;
	cin >> ncase;
	int ks = 1;
	while (ncase--)
	{
		map<LL, LL> m;
		LL n, k;
		cin >> n >> k;
		priority_queue<LL> pq;
		pq.push(n);
		m[n] = 1;
		LL x = n;
		while (!pq.empty())
		{
			x = pq.top();
			pq.pop();
			LL cnt = m[x];
			if (cnt >= k) break;
			k -= cnt;
			x--;
			LL l = x / 2;
			LL r = x - x / 2;
			if (!m.count(l)) pq.push(l), m[l] = 0;
			if (!m.count(r)) pq.push(r), m[r] = 0;
			m[l] += cnt;
			m[r] += cnt;
		}
		x--;
		LL l = x / 2;
		LL r = x - x / 2;
		printf("Case #%d: %lld %lld\n", ks++, r, l);
	}
	return 0;
}

