/*
PROG: gcj5304486a
LANG: C++
 */
#include <cstdlib>
#include <csignal>
#include <csetjmp>
#include <cstdarg>
#include <typeinfo>
#include <bitset>
#include <functional>
#include <utility>
#include <ctime>
#include <cstddef>
#include <new>
#include <memory>
#include <climits>
#include <cfloat>
#include <limits>
#include <exception>
#include <cassert>
#include <cerrno>
#include <cctype>
#include <cwctype>
#include <cstring>
#include <cwchar>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <iterator>
#include <cmath>
#include <complex>
#include <valarray>
#include <numeric>
#include <iosfwd>
#include <ios>	
#include <istream>	
#include <ostream>
#include <iostream>
#include <fstream>	
#include <strstream>	
#include <iomanip>	
#include <streambuf>
#include <cstdio>
#include <locale>	
#include <clocale>

#define MP make_pair
#define PB push_back

#define SINF 10001
#define INF 1000000001
#define LLINF 1000000000000000001ll
#define EPS 0.000000000000001
#define PI ((4.0) * atan(1.0))
#define MAXN 400

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<int, long long> pil;
typedef pair<long long, int> pli;
typedef pair<long long, long long> pll;

int T;
int N, M;
char grid[MAXN][MAXN];
int lt[MAXN], rt[MAXN], u[MAXN], d[MAXN];

void can(int x, int y, char c)
{
	int newlt = min(lt[c], y);
	int newrt = max(rt[c], y);
	int newu = min(u[c], x);
	int newd = max(d[c], x);
	for (int i = newu; i <= newd; i++)
	{
		for (int j = newlt; j <= newrt; j++)
		{
//			if (x == 1 && y == 3 && c == 'A')
//			{
//				cerr << i << ' ' << j << ' ' << grid[i][j] << endl;
//			}
			if (grid[i][j] != c && grid[i][j] != '?')
			{
				return;
			}
		}
	}
//	cerr << x << ' ' << y << ' ' << c << endl;
	grid[x][y] = c;
	lt[c] = newlt;
	rt[c] = newrt;
	u[c] = newu;
	d[c] = newd;
	for (int i = newu; i <= newd; i++)
	{
		for (int j = newlt; j <= newrt; j++)
		{
			grid[i][j] = c;
		}
	}
	return;
}

int32_t main()
{
	ios_base::sync_with_stdio(false);
	if (fopen("gcj5304486a.in", "r"))
	{	
		freopen ("gcj5304486a.in", "r", stdin);
		freopen ("gcj5304486a.out", "w", stdout);
	}
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ":\n";
		cin >> N >> M;
		for (int i = 0; i < N; i++)
		{
			string s;
			cin >> s;
			for (int j = 0; j < M; j++)
			{
				grid[i][j] = s[j];
			}
		}
		//		for (int i = 0; i < N; i++)
		//		{
		//			for (int j = 0; j < M; j++)
		//			{
		//				cerr << grid[i][j];
		//			}
		//			cerr << endl;
		//		}
		for (int i = 0; i < 300; i++)
		{
			lt[i] = INF;
			rt[i] = -INF;
			u[i] = INF;
			d[i] = -INF;
		}
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				char c = grid[i][j];
				if (c == '?')
				{
					continue;
				}
				u[c] = min(u[c], i);
				d[c] = max(d[c], i);
				lt[c] = min(lt[c], j);
				rt[c] = max(rt[c], j);
			}
		}
		for (char c = 'a'; c <= 'z'; c++)
		{
			for (int i = u[c]; i <= d[c]; i++)
			{
				for (int j = lt[c]; j <= rt[c]; j++)
				{
					grid[i][j] = c;
				}
			}
		}
//		cerr << u['A'] << ' ' << d['A'] << endl;
		//				for (int i = 0; i < N; i++)
		//				{
		//					for (int j = 0; j < M; j++)
		//					{
		//						cerr << grid[i][j];
		//					}
		//					cerr << endl;
		//				}
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				for (char c = 'A'; c <= 'Z'; c++)
				{
					if (u[c] == INF)
					{
						continue;
					}
					if (grid[i][j] != '?')
					{
						continue;
					}
					can(i, j, c);
				}
			}
		}
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				cout << grid[i][j];
			}
			cout << '\n';
		}
	}
	return 0;
}
