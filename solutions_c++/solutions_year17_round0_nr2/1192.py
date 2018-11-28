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
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;
typedef pair<int,pii> piii;

#define y1 dsjfksdj_fks
#define y2 alksaad_sa

int64 n;
int nt;
vector<int> a;
int64 p10[19];
int64 f[20][10][2];

int64 rec(int x, int y, int z)
{
	if (x == (int)a.size()) return 0;

	if (f[x][y][z] != -1)
		return f[x][y][z];

	int64 res = -2;

	int st = y;
	int fn = 9;
	if (!z)
		fn = a[x];
	for (int i = st; i <= fn; ++i)
	{
		int nz = z;
		if (i < fn)
			nz = 1;
		int64 cur = rec(x + 1, i, nz);
		if (cur == -2) continue;
		cur += static_cast<int64>(i) * p10[(int)a.size() - x - 1];
		res = max(res, cur);
	}

	// cout << x << " " << y << " " << z << " --> " << res << endl;
	return f[x][y][z] = res;
}

inline int64 solve(int64 n)
{
	a.clear();
	int64 x = n;
	while (x)
	{
		a.push_back(x % 10);
		x /= 10;
	}
	reverse(a.begin(), a.end());
	memset(f, -1, sizeof f);
	int64 res = rec(0, 0, 0);
	return res;
}

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    
	p10[0] = 1;
	for (int i = 1; i < 19; ++i)
		p10[i] = p10[i - 1] * 10LL;

	int tn = 0;
	cin >> nt;
	for (;nt--;)
	{
		++tn;
		cin >> n;
		int64 res = solve(n);
		cout << "Case #" << tn << ": " << res << endl;
	}
    
    return 0;
}