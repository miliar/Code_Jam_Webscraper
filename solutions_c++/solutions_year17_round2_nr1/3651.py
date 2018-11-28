#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <list>
#include <set>
#include <cstdlib>
#include <vector>
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>
#include <stack>
#include <ctime>
#include <queue>
#include <map>
#include <cstring>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef bool bl;
typedef pair<bl, bl> pbl;
typedef pair<ld, ld> pld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
#define mp make_pair
#define ft first
#define sd second
#define forn(i, y, x) for(int i = y; i < x; i++)
#define ford(i, y, x) for(int i = y; i >= x; i--)
#define sz(x) (int)x.size()
#define all(x) x.begin(), x.end()
#define error exit(1)
const ll mod = (ll)1e9 + 7;
const int inf = (int)2e9;
const ll INF = (ll)1e18;
const int base = 1000 * 1000 * 1000;
const int maxn = 2005;
const ld pi = acosl(-1.0);
const ld eps = 1e-9;

void solve()
{
	int t;
	scanf("%d", &t);
	for (int tt = 0; tt < t; tt++){
		printf("Case #%d: ", tt + 1);

		int d, n;
		scanf("%d %d", &d, &n);
		vector<pii> p(n);
		for (int i = 0; i < n; i++){
			int a, b;
			scanf("%d %d", &a, &b);
			p[i] = mp(a, b);
		}
		p.push_back(mp(d, 0));
		sort(all(p));
		double time = 0;
		int cur = 0;
		while (cur != n){
			double newt = inf;
			int ind = -1;
			for (int i = cur + 1; i <= n; i++){
				if (p[i].sd < p[cur].sd){
					double tmp = (double)(p[i].ft - p[cur].ft) / (p[cur].sd - p[i].sd);
					if (tmp < newt){
						newt = tmp;
						ind = i;
					}
				}
			}
			time = newt;
			cur = ind;
		}
		printf("%.10lf\n", d / time);
	}
}

int main()
{
#ifdef _DEBUG
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	solve();
	return 0;
}