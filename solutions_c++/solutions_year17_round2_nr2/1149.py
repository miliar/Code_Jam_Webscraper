#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <cstdlib>
#include <set>
#include <cassert>
#include <map>
using namespace std;

#pragma comment(linker, "/STACK:567772160")

#define mp(x, y) make_pair(x, y)
#define sc(x) scanf("%d", &x)
#define sc2(x, y) scanf("%d %d", &x, &y)
#define scl(x) scanf("%I64d", &x)
#define scl2(x, y) scanf("%I64d %I64d", &x, &y)
#define forn(i, a, b) for(int i=a; i<b; ++i)
#define ford(i, a, b) for(int i=b-1; i>=a; --i)
#define all(x) x.begin(), x.end()
#define pr(x) printf("%d ", x)

typedef pair<int, int> pii;
typedef long long ll;
typedef long double ld;

const long double EPS = 1e-8;
const long double PI = atan((long double)1) * 4;
const int inf = (int)1e9;
const ll INF = (ll)1e18;

map<char, char> m;

int cnt = 0;

void print(string s)
{
	cnt += s.size();
	forn(i, 0, s.size())
		cout << m[s[i]];
}

void solve()
{
	int t;
	sc(t);
	forn(tt, 0, t)
	{
		cnt = 0;
		m.clear();
		m['R'] = 'R';
		m['Y'] = 'Y';
		m['B'] = 'B';
		m['O'] = 'O';
		m['G'] = 'G';
		m['V'] = 'V';
		cout << "Case #" << tt + 1 << ": ";
		int n, r, o, y, g, b, v;
		cin >> n >> r >> o >> y >> g >> b >> v;
		if (o == 0 && g == 0 && v == 0)
		{
			if(y>r)
			{
				swap(m['Y'], m['R']);
				swap(y, r);
			}
			if(b>r)
			{
				swap(m['B'], m['R']);
				swap(b, r);
			}
			if(b>y)
			{
				swap(m['Y'], m['B']);
				swap(y, b);
			}

			if (r > y + b)
			{
				cout << "IMPOSSIBLE\n";
				continue;
			}

			int delta = y + b - r;
			forn(i, 0, delta)
				print("RYB");
			forn(i, 0, y - delta)
				print("RY");
			forn(i, 0, b - delta)
				print("RB");
		}
		cout << "\n";
		assert(cnt == n);
	}
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	solve();
#ifndef ONLINE_JUDGE
	fprintf(stderr, "Time: %.2lf\n", (double)clock() / CLOCKS_PER_SEC);
#endif
	return 0;
}