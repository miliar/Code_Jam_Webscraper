#pragma comment(linker,"/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <sstream>
#include <stdio.h>

#include <algorithm>
#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <queue>
#include <deque>
#include <stack>

#include <cmath>
#include <string>

#include <cassert>
#include <time.h>
#include <memory.h>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a,b) memset( (a), b, sizeof( a ) )
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()

#define fi(n) for (int i = 0; i < (n); ++ i)
#define fj(n) for (int j = 0; j < (n); ++ j)
#define fin() for (int i = 0; i < n; ++ i)
#define fjm() for (int j = 0; j < m; ++ j)
#define forv(i, v) for (int i = 0; i < sz((v)); ++ i)


#ifdef _DEBUG
#define dbg(...) {fprintf(stderr, __VA_ARGS__); fflush(stderr);}
#define dbgx(x) {cerr << #x << " = " << x << endl;}
#else
#define dbg(...) { }
#define dbgx(x) { }
#endif

typedef unsigned long long ull;
typedef long long lint;
typedef pair < int, int > pii;
typedef long double ld;

const int INF = 1000 * 1000 * 1000;
const lint LINF = 1000000000000000000LL;
const double eps = 1e-9;

void prepare(string s)
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	if (sz(s) > 0)
	{
		freopen((s + ".in").c_str(), "r", stdin);
		freopen((s + ".out").c_str(), "w", stdout);
	}
#endif
}
int n, q;

const int MAXN = 141;

lint d[MAXN][MAXN];
lint strength[MAXN];
lint speed[MAXN];
int q1[MAXN];
int q2[MAXN];

ld ans[MAXN];

void read()
{
	cin >> n >> q;
	fi(n) {
		cin >> strength[i] >> speed[i];
	}

	fi(n)
		fj(n)
	{
		cin >> d[i][j];
		if (d[i][j] == -1)
			d[i][j] = LINF;
	}

	fi(q)
	{
		cin >> q1[i] >> q2[i];
		q1[i]--;
		q2[i]--;
	}

}

bool upd(lint &a, lint val)
{
	if (a > val)
	{
		a = val;
		return true;
	}
	return false;
}


bool upd(ld &a, ld val)
{
	if (a > val)
	{
		a = val;
		return true;
	}
	return false;
}

void solve()
{
	for (int k = 0; k < n; ++k)
	{
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < n; ++j)
			{
				upd(d[i][j], d[i][k] + d[k][j]);
			}
		}
	}

	for (int qi = 0; qi < q; ++qi)
	{
		set<pair<ld, int> > s;

		int start = q1[qi];
		int finish = q2[qi];

		fi(n)
			ans[i] = 1e15;

		ans[start] = 0.;
		s.insert(mp(0., start));

		while (!s.empty())
		{
			int v = s.begin()->second;
			s.erase(s.begin());

			for (int next = 0; next < n; ++next)
			{
				if (d[v][next] > strength[v])
					continue;
				if (upd(ans[next], ans[v] + ((ld)d[v][next] / speed[v])))
				{
					s.insert(mp(ans[next], next));
				}
			}
		}

		printf("%.8llf ", ans[finish]);
		//cerr << ans[finish] << ' ';
	}

}

int main()
{
	prepare("");

	int T;
	cin >> T;
	fi(T)
	{
		read();
		cout << "Case #" << i + 1 << ": ";
		cerr << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
		cerr << endl;
	}

	return 0;
}
