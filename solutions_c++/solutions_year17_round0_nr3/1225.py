#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <memory.h>

using namespace std;

#pragma comment(linker, "/STACK:128000000")

typedef pair<int, int> pii;
typedef long long int64;
typedef pair<int64, int64> pii64;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;
typedef pair<int,pii> piii;

#define y1 dsjfksdj_fks
#define y2 alksaad_sa

int nt;
int64 n, k;
priority_queue<int64> q;
map<int64, int64> cnt;

inline pii64 solve(int64 n, int64 k)
{
	while (!q.empty())
		q.pop();
	q.push(n);
	int64 last = n;
	for (int64 i = 0; i < k; ++i)
	{
		int64 cur = q.top();
		last = cur;
		q.pop();
		int64 x = cur / 2;
		int64 y = (cur - 1) / 2;
		if (x)
			q.push(x);
		if (y)
			q.push(y);
	}
	return pii64(last / 2, (last - 1) / 2);
}

inline pii64 solve_fast(int64 n, int64 k)
{
	while (!q.empty())
		q.pop();
	cnt.clear();

	q.push(n);
	cnt[n] = 1;
	int64 last = n;
	while (k)
	{
		int64 val = q.top();
		last = val;
		while (!q.empty() && q.top() == val)
			q.pop();
		int64 c = cnt[val];
		c = min(c, k);
		k -= c;
		int64 x = val / 2;
		int64 y = (val - 1) / 2;
		if (x)
		{
			q.push(x);
			cnt[x] += c;
		}
		if (y)
		{
			q.push(y);
			cnt[y] += c;
		}
	}

	return pii64(last / 2, (last - 1) / 2);
}

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

	int tn = 0;
	cin >> nt;
	for (;nt--;)
	{
		++tn;
		cin >> n >> k;
		pii64 res = solve_fast(n, k);
		cout << "Case #" << tn << ": " << res.first << " " << res.second << endl;
	}
    
    return 0;
}