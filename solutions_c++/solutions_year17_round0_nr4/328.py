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
using namespace std;

#pragma comment(linker, "/stack:64000000")

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

void assert(bool b)
{
	if (!b)
		throw 0;
}

struct bigraph
{
	vvi edges;
	vi xy;
	vi yx;
	
	void init(int n)
	{
		edges.assign(n, vi());
		xy.assign(n, -1);
		yx.assign(n, -1);
	}

	void add(int from, int to)
	{
		assert(0 <= from && from < (int)xy.size());
		assert(0 <= to && to < (int)yx.size());
		edges[from].push_back(to);
	}

	vi visitx;

	int max_match()
	{
		int k = 0;
		foria(edges)
		{
			init_run();
			if (tryx(i))
				++k;
		}
		return k;
	}

	void init_run()
	{
		visitx.assign(edges.size(), 0);
	}

	bool tryy(int y)
	{
		if (yx[y] == -1)
			return true;
		return tryx(yx[y]);
	}

	bool tryx(int x)
	{
		if (visitx[x])
			return false;

		visitx[x] = true;
		for (auto y : edges[x])
			if (tryy(y))
			{
				xy[x] = y;
				yx[y] = x;
				return true;
			}
		return false;
	}
};

int main()
{
	ios::sync_with_stdio(false);

#ifdef _MSC_VER
	ifstream cin("input.txt");
	ofstream cout("output.txt");
#else
	ifstream cin("input.txt");
	ofstream cout("output.txt");
#endif
	
	readt;
	fort
	{
		set<int> f_x, f_y, f_plus, f_minus;
		std::map<ii, int> cert;

		int score = 0;

		int n, k;
		read n >> k;

		fori(k)
		{
			char c;
			int x, y;
			read c >> x >> y;
			--x;
			--y;
			if (c == 'x' || c == 'o')
			{
				f_x.insert(x);
				f_y.insert(y);
				++score;
				cert[{x, y}] |= 1;
			}
			if (c == '+' || c == 'o')
			{
				f_plus.insert(x + y);
				f_minus.insert(x - y);
				++score;
				cert[{x, y}] |= 2;
			}
		}

		set<ii> changed;

		bigraph g1;
		g1.init(n);
		forin forjn
			if (f_x.count(i) == 0 && f_y.count(j) == 0)
				g1.add(i, j);

		score += g1.max_match();

		foria(g1.xy)
			if (g1.xy[i] != -1)
			{
				ii current = { i, g1.xy[i] };
				cert[current] |= 1;
				changed.insert(current);
			}

		bigraph g2;
		g2.init(n + n);
		forin forjn
			if (f_plus.count(i + j) == 0 && f_minus.count(i - j) == 0)
				g2.add(i + j, i - j + n);

		score += g2.max_match();
		foria(g2.xy)
			if (g2.xy[i] != -1)
			{
				ii current = { i, g2.xy[i] };
				current = {(current.first + current.second - n) / 2, (current.first - current.second + n) / 2 };
				cert[current] |= 2;
				changed.insert(current);
			}

		char legend[] = { '.', 'x', '+', 'o' };

		write "Case #" << gett << ": ";
		write score << " " << changed.size();
		for (auto current : changed)
		{
			writeln;
			write legend[cert[current]] << " " << current.first + 1 << " " << current.second + 1;
		}
		writeln;
	}

	return 0;
}