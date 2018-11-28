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

struct Horse
{
	ll e, s;
	double t;

	Horse(ll e, ll s, double t) : e(e), s(s), t(t)
	{}
};

void solve()
{
	int t;
	sc(t);
	forn(tt, 0, t)
	{
		cout << "Case #" << tt + 1 << ": ";
		int n, q;
		sc2(n, q);
		vector<ll> e(n+1), s(n+1);
		forn(i, 1, n+1)
			cin >> e[i] >> s[i];
		vector<vector<ll> > d(n+1, vector<ll>(n+1));
		forn(i, 1, n+1)
			forn(j, 1, n+1)
			cin >> d[i][j];
		while(q--)
		{
			int u, v;
			sc2(u, v);
			vector<vector<Horse> > h(n+1);
			vector<bool> used(n+1, false);
			h[u].push_back(Horse(0, 0, 0));
			forn(i, 0, n)
			{
				int cur = -1;
				double tCur = 1e18;
				forn(j, 1, n+1)
					if(!used[j])
						for(auto &horse : h[j])
							if(horse.t < tCur)
							{
								cur = j;
								tCur = horse.t;
							}
				assert(cur != -1);
				used[cur] = true;
				h[cur].push_back(Horse(e[cur], s[cur], tCur));
				forn(j, 1, n + 1)
					if (!used[j] && d[cur][j] != -1)
						for (auto &horse : h[cur])
							if (horse.e >= d[cur][j])
								h[j].push_back(Horse(horse.e - d[cur][j], horse.s, horse.t + (double)d[cur][j] / horse.s));
			}
			double ans = 1e18;
			for (auto &horse : h[v])
				ans = min(ans, horse.t);
			printf("%.10lf", ans);
		}
		cout << "\n";
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