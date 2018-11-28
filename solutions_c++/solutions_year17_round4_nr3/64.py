#include <cstdio>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <memory.h>
#include <sstream>
#include <ctime>
#include <bitset>
#include <random>
using namespace std;

#pragma comment(linker, "/stack:640000000")

typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;

typedef vector<int> vi;
typedef vector<pair<int, int > > vii;
typedef vector<ll> vll;
typedef vector<string> vs;
typedef vector<ld> vld;

typedef vector<vi> vvi;
typedef vector<vii> vvii;
typedef vector<vll> vvll;
typedef vector<vs> vvs;

typedef map<int, int> mpii;
typedef map<int, string> mpis;
typedef map<string, int> mpsi;
typedef map<string, string> mpss;

#define all(a) (a).begin(),(a).end()
#define rall(a) (a).rbegin(),(a).rend()
#define sz(a) (int)((a).size())
#define len(a) (int)((a).length())

#define forr(i,n) for (int i = 0; i < (n); ++i)
#define fori(n) forr(i,n)
#define forj(n) forr(j,n)
#define fork(n) forr(k,n)
#define forin fori(n)
#define forjn forj(n)
#define forjm forj(m)
#define forkm fork(m)
#define foria(a) fori(sz(a))
#define foriv foria(v)
#define foris fori(len(s))
#define forja(a) forj(sz(a))
#define forjv forj(v)
#define forjs forj(len(s))

#define read cin>>
#define write cout<<
#define writeln write endl

#define readt int aaa; read aaa;
#define gett (bbb+1)
#define fort forr(bbb,aaa)


ld dis(ld x, ld y) { return sqrt(x*x + y*y); }
const ld PI = acos(ld(0.0)) * 2;

ll gcd(ll a, ll b) { return b ? gcd(b, a%b) : a; }

int n, m;
char mp[100][100];

int code(int idx, int idy, int idd)
{
	return ((0 + idx) * m + idy) * 2 + idd;
}

struct info_type
{
	int code = 0; //0 undefined, 1 loop, 2 wall, 3 generator
	int idx;
	int idy;
	int idd;
	int icode() 
	{
		return ::code(idx, idy, idd);
	}
} info[4][100][100];

char get_mp(int x, int y)
{
	if (!(0 <= x && x < n && 0 <= y && y < m))
		return '#';
	return mp[x][y];
}

int dir_dx[] = { 1, -1, 0, 0 };
int dir_dy[] = { 0, 0, 1, -1 };
int dir_m1[] = { 3, 2, 1, 0 };
int dir_m2[] = { 2, 3, 0, 1 };

info_type dfs(int dir, int x, int y)
{
	info_type &result = info[dir][x][y];

	if (result.code != 0)
		return result;

	result.code = 1; // loop
	
	x += dir_dx[dir];
	y += dir_dy[dir];
	switch (get_mp(x, y))
	{
		case '#':
			result.code = 2; //wall
			break;
		case '-':
		case '|':
			result.code = 3; //generator
			result.idx = x;
			result.idy = y;
			result.idd = dir / 2;
			break;
		case '/':
			dir = dir_m1[dir];
			result = dfs(dir, x, y);
			break;
		case '\\':
			dir = dir_m2[dir];
			result = dfs(dir, x, y);
			break;
		case '.':
			result = dfs(dir, x, y);
			break;
	}

	return result;
}

int sat_visit[20000];
vi sat_child[20000];

int sat_visit_reversed[20000];
vi sat_child_reversed[20000];

vi sat_order;
int sat_id[20000];

bool dfs_sat(int x)
{
	if (sat_visit[x])
		return false;

	sat_visit[x] = true;
	for (auto t : sat_child[x])
		dfs_sat(t);
	sat_order.push_back(x);
	return true;
}

bool dfs_sat_reversed(int x, int id)
{
	if (sat_visit_reversed[x])
		return false;

	sat_visit_reversed[x] = true;
	sat_id[x] = id;
	for (auto t : sat_child_reversed[x])
		dfs_sat_reversed(t, id);
	return true;
}

int main()
{
	ios::sync_with_stdio(false);

#ifdef _MSC_VER
	ifstream cin("input.txt");
	ofstream cout("output.txt");
#else
#endif

	cout.setf(ios::fixed);
	cout.precision(20);

	readt;
	fort
	{
		read n >> m;
		forin 
		{
			string s;
			read s;
			forjs mp[i][j] = s[j];
		}

		bool fail = false;

		fork(4) forin forjm info[k][i][j].code = 0; //undefined

		forin forjm fork(2) sat_visit[code(i, j, k)] = false;
		forin forjm fork(2) sat_visit_reversed[code(i, j, k)] = false;
		forin forjm fork(2) sat_child[code(i, j, k)].clear();
		forin forjm fork(2) sat_child_reversed[code(i, j, k)].clear();
		forin forjm fork(2) sat_id[code(i, j, k)] = -1;
		sat_order.clear();

		forin forjm 
			if (mp[i][j] == '.' || mp[i][j] == '-' || mp[i][j] == '|')
			{
				fork(4) dfs(k, i, j);

				auto &c0 = info[0][i][j];
				auto &c1 = info[1][i][j];
				auto &c2 = info[2][i][j];
				auto &c3 = info[3][i][j];

				if (mp[i][j] == '.')
				{
					vector<info_type> options;

					if (c0.code == 3 && c1.code != 3)
						options.push_back(c0);
					if (c0.code != 3 && c1.code == 3)
						options.push_back(c1);
					if (c2.code == 3 && c3.code != 3)
						options.push_back(c2);
					if (c2.code != 3 && c3.code == 3)
						options.push_back(c3);

					if (options.size() == 0)
					{
						fail = true;
					}
					else if (options.size() == 1)
					{
						sat_child[code(options[0].idx, options[0].idy, 1 - options[0].idd)].push_back(
							code(options[0].idx, options[0].idy, options[0].idd)
						);
					}
					else
					{
						options[0].idd = 1 - options[0].idd;
						sat_child[options[0].icode()].push_back(options[1].icode());
						options[0].idd = 1 - options[0].idd;

						options[1].idd = 1 - options[1].idd;
						sat_child[options[1].icode()].push_back(options[0].icode());
						options[1].idd = 1 - options[1].idd;
					}
				}
				else
				{
					if (c0.code != 2 || c1.code != 2)
						sat_child[code(i, j, 0)].push_back(code(i, j, 1));
					if (c2.code != 2 || c3.code != 2)
						sat_child[code(i, j, 1)].push_back(code(i, j, 0));
				}
			}

		forin forjm fork(2)
		{
			int f = code(i, j, k);
			for (auto t : sat_child[f])
				sat_child_reversed[t].push_back(f);
		}

		forin forjm if (mp[i][j] == '-' || mp[i][j] == '|') fork(2) dfs_sat(code(i, j, k));
		reverse(all(sat_order));

		int id = 0;
		foria(sat_order) dfs_sat_reversed(sat_order[i], ++id);

		forin forjm if (mp[i][j] == '-' || mp[i][j] == '|')
		{
			int c0 = code(i, j, 0), c1 = code(i, j, 1);
			if (sat_id[c0] < sat_id[c1])
				mp[i][j] = '-';
			else if (sat_id[c0] > sat_id[c1])
				mp[i][j] = '|';
			else
				fail = true;
		}

		write "Case #" << gett << ": " << (fail ? "IMPOSSIBLE" : "POSSIBLE");
		writeln;
		if (!fail)
		{
			forin
			{
				forjm write mp[i][j];
				writeln;
			}
		}
	}

	return 0;
}