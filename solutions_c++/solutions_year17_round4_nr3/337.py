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

int nt;
int n, m;
vector<string> a;
pii cl[52][52];
pii vn[52][52];
pii hn[52][52];

inline int is_beam(char c)
{
	return (c == '|' || c == '-');
}

inline int is_wall(char c)
{
	return (c == '#');
}

inline int is_emp(char c)
{
	return (c == '.');
}

inline void init()
{
	cin >> n >> m;
	a.clear();
	a.resize(n);
	for (int i = 0; i < n; ++i)
		cin >> a[i];
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
		{
			if (is_emp(a[i][j]))
			{
				vn[i][j] = hn[i][j] = pii(-1, -1);
				for (int t = i - 1; t >= 0; --t)
				{
					if (is_wall(a[t][j])) break;
					if (!is_beam(a[t][j])) continue;
					vn[i][j] = pii(t, j);
					break;
				}
				for (int t = i + 1; t < n; ++t)
				{
					if (is_wall(a[t][j])) break;
					if (!is_beam(a[t][j])) continue;
					vn[i][j] = pii(t, j);
					break;
				}
				for (int t = j - 1; t >= 0; --t)
				{
					if (is_wall(a[i][t])) break;
					if (!is_beam(a[i][t])) continue;
					hn[i][j] = pii(i, t);
					break;
				}
				for (int t = j + 1; t < m; ++t)
				{
					if (is_wall(a[i][t])) break;
					if (!is_beam(a[i][t])) continue;
					hn[i][j] = pii(i, t);
					break;
				}
			}
			if (is_beam(a[i][j]))
			{
				cl[i][j] = pii(1, 1);
				for (int t = i - 1; t >= 0; --t)
				{
					if (is_wall(a[t][j])) break;
					if (!is_beam(a[t][j])) continue;
					cl[i][j].first = 0;
					break;
				}
				for (int t = i + 1; t < n; ++t)
				{
					if (is_wall(a[t][j])) break;
					if (!is_beam(a[t][j])) continue;
					cl[i][j].first = 0;
					break;
				}
				for (int t = j - 1; t >= 0; --t)
				{
					if (is_wall(a[i][t])) break;
					if (!is_beam(a[i][t])) continue;
					cl[i][j].second = 0;
					break;
				}
				for (int t = j + 1; t < m; ++t)
				{
					if (is_wall(a[i][t])) break;
					if (!is_beam(a[i][t])) continue;
					cl[i][j].second = 0;
					break;
				}
				continue;
			}
		}
}

const int dx[4] = {-1, 1, 0, 0};
const int dy[4] = {0, 0, -1, 1};
int was[52][52];
vector<pii> pts;

inline int solve()
{
	memset(was, 0, sizeof was);
	pts.clear();
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
		{
			if (!is_emp(a[i][j])) continue;
			if (hn[i][j].first == -1 && vn[i][j].first == -1) return 0;
			pts.push_back(pii(i, j));
		}
	for (;;)
	{
		int k = static_cast<int>(pts.size());
		if (!k) break;
		for (int i = 0; i < k; ++i)
		{
			int x = pts[i].first;
			int y = pts[i].second;
			if (vn[x][y].first != -1 && hn[x][y].first != -1) continue;
			if (vn[x][y].first != -1)
			{
				int nx = vn[x][y].first;
				int ny = vn[x][y].second;
				if (!cl[nx][ny].first) return 0;
				cl[nx][ny].second = 0;
			} else {
				int nx = hn[x][y].first;
				int ny = hn[x][y].second;
				if (!cl[nx][ny].second) return 0;
				cl[nx][ny].first = 0;
			}
		}
		int fnd = 0;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
			{
				if (was[i][j]) continue;
				if (!is_beam(a[i][j])) continue;
				if (!cl[i][j].first && !cl[i][j].second) return 0;
				if (cl[i][j].first && cl[i][j].second) continue;
				fnd = 1;
				was[i][j] = 1;
				if (cl[i][j].first)
				{
					a[i][j] = '|';
					for (int t = 0; t < k; ++t)
					{
						int nx = pts[t].first;
						int ny = pts[t].second;
						if (hn[nx][ny] == pii(i, j))
						{
							hn[nx][ny] = pii(-1, -1);
							continue;
						}
						if (vn[nx][ny] == pii(i, j))
						{
							swap(pts[t], pts[k - 1]);
							pts.pop_back();
							--k;
							--t;
						}
					}
				} else {
					a[i][j] = '-';
					for (int t = 0; t < k; ++t)
					{
						int nx = pts[t].first;
						int ny = pts[t].second;
						if (vn[nx][ny] == pii(i, j))
						{
							vn[nx][ny] = pii(-1, -1);
							continue;
						}
						if (hn[nx][ny] == pii(i, j))
						{
							swap(pts[t], pts[k - 1]);
							pts.pop_back();
							--k;
							--t;
						}
					}
				}
			}
		if (fnd) continue;
		sort(pts.begin(), pts.end());
		int x = pts[0].first;
		int y = pts[0].second;
		hn[x][y] = pii(-1, -1);
	}
	return 1;
}

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

	cin >> nt;
	for (int tn = 1; tn <= nt; ++tn)
	{
		init();
		int res = solve();
		if (!res)
		{
			printf("Case #%d: IMPOSSIBLE\n", tn);
		} else {
			printf("Case #%d: POSSIBLE\n", tn);
			for (int i = 0; i < n; ++i)
				printf("%s\n", a[i].c_str());
		}
		//memset(f, -1, sizeof f);
		//int res = rec(0, m, 0);
	}

    return 0;
}