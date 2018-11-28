/**
 * Problem: inverse-matrix
 * Correct solution (must be OK).
 * Author: pkhaustov
 */

#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES

#include <algorithm>
#include <cstdio>
#include <ctime>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <cassert>
#include <iostream>
#include <cmath>
#include <sstream>
#include <complex>
#include <memory.h>

using namespace std;

#pragma comment(linker, "/STACK:64000000")

typedef long long int64;
typedef unsigned long long uint64;

#define y1 _dsfkjdsfksdj
#define y0 _sfsdkfdop

typedef unsigned uint;
typedef vector<int64> vi64;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef pair<int,string> pis;
typedef pair<int64,int64> pii64;
typedef pair<pii,int> piii;
typedef pair<pii,pii> piiii;
typedef pair<int64,pii> qelem;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;
typedef pair<double,int> pdi;
typedef pair<double,double> pdd;

const int maxn = 102;

int nt;
int tp;
int n, p;
vi a;

int f[3][maxn][maxn][maxn][4];

inline void init()
{
	scanf("%d%d", &n, &p);
	a.resize(n);
	for (int i = 0; i < n; ++i)
		scanf("%d", &a[i]);
}

int rec(int k1, int k2, int k3, int md)
{
	if (f[tp][k1][k2][k3][md] != -1) return f[tp][k1][k2][k3][md];

	if (!k1 && !k2 && !k3)
	{
		return f[tp][k1][k2][k3][md] = 0;
	}

	int res = 0;

	if (k1)
	{
		res = max(res, rec(k1 - 1, k2, k3, (md + 1) % p));
	}

	if (k2)
	{
		res = max(res, rec(k1, k2 - 1, k3, (md + 2) % p));
	}

	if (k3)
	{
		res = max(res, rec(k1, k2, k3 - 1, (md + 3) % p));
	}

	if (!md) ++res;
	return f[tp][k1][k2][k3][md] = res;
}

inline int solve()
{
	tp = p - 2;
	vector<int> cnts(4, 0);
	for (int i = 0; i < n; ++i)
		++cnts[a[i] % p];
	int res = cnts[0];
	res += rec(cnts[1], cnts[2], cnts[3], 0);
	return res;
}

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

	memset(f, -1, sizeof f);

	scanf("%d", &nt);
	for (int tn = 1; tn <= nt; ++tn)
	{
		init();
		int res = solve();
		printf("Case #%d: %d\n", tn, res);
	}

    return 0;
}