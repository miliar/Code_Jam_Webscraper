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
#include <ctime>
#include <hash_map>

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
typedef pair<int64,pii> piii64;
typedef pair<pii,pii> piiii;
typedef pair<double, double> pdd;

#define y1 dsjfksdj_fks
#define y2 alksaad_sa
#define y0 _sdkfsjfs__
#define tm _dskfjskdfjksdf

int nt;
int D, n;
vector<int> K;
vector<int> S;

inline void init()
{
	scanf("%d%d", &D, &n);
	K.clear();
	S.clear();
	K.resize(n);
	S.resize(n);
	for (int i = 0; i < n; ++i)
	{
		scanf("%d%d", &K[i], &S[i]);
	}
}

inline int check(double mid)
{
	double d = static_cast<double>(D);
	double v1 = mid;
	double t = d / v1;
	for (int i = 0; i < n; ++i)
	{
		double v2 =	static_cast<double>(S[i]);
		double p2 = static_cast<double>(K[i]);
		double s2 = p2 + t * v2;
		if (s2 < d)
			return 0;
	}
	return 1;
}

inline double solve()
{
	double l = 0.0, r = 1e+18;
	for (int it = 0; it < 128; ++it)
	{
		double mid = (l + r) / 2.0;
		if (check(mid))
			l = mid;
		else
			r = mid;
	}
	return (l + r) / 2.0;
}

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

	scanf("%d", &nt);
	for (int tn = 1; tn <= nt; ++tn)
	{
		init();
		double res = solve();
		printf("Case #%d: %.15lf\n", tn, res);
	}

	return 0;
}