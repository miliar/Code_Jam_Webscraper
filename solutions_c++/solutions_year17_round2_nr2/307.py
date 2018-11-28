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
int n, R, O, Y, G, B, V;

inline void init()
{
	scanf("%d%d%d%d%d%d%d", &n, &R, &O, &Y, &G, &B, &V);
}

vector< pair<int, char> > a;
int f[1 << 10][1 << 10];

inline void check(string &s)
{
	int l = static_cast<int>(s.length());
	for (int i = 0; i < l; ++i)
	{
		int ni = (i + 1) % l;
		if (s[i] == s[ni])
		{
			s = "IMPOSSIBLE";
			return;
		}
	}
}

inline string solve_small()
{
	a.clear();
	a.resize(3);
	a[0] = make_pair(R, 'R');
	a[1] = make_pair(Y, 'Y');
	a[2] = make_pair(B, 'B');
	sort(a.begin(), a.end());
	int cnt = a[0].first;
	if (!cnt)
	{
		if (!a[1].first)
		{
			return "IMPOSSIBLE";
		} else {
			if (a[2].first != a[1].first)
				return "IMPOSSIBLE";
			string res = "";
			for (int i = 0; i < n; ++i)
			{
				if (i & 1)
					res += a[1].second;
				else
					res += a[2].second;
			}
			return res;
		}
	}
	vector<string> resv(cnt);
	for (int i = 0; i < cnt; ++i)
	{
		resv[i] += a[0].second;
	}
	for (int i = 0; i < cnt; ++i)
	{
		if (a[2].first > a[1].first)
		{
			--a[2].first;
			resv[i] += a[2].second;
		}
	}
	if (a[2].first != a[1].first)
		return "IMPOSSIBLE";
	for (int i = 0; i < cnt; ++i)
	{
		resv[i] += a[1].second;
		resv[i] += a[2].second;
	}
	a[1].first -= cnt;
	a[2].first -= cnt;
	while (a[1].first)
	{
		--a[1].first;
		--a[2].first;
		resv[0] += a[1].second;
		resv[0] += a[2].second;
	}
	string res = "";
	for (int i = 0; i < cnt; ++i)
		res += resv[i];
	return res;
}

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

	scanf("%d", &nt);
	for (int tn = 1; tn <= nt; ++tn)
	{
		init();
		printf("Case #%d: ", tn);
		string res = solve_small();
		check(res);
		cout << res << "\n";
	}

	return 0;
}