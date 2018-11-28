#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:259000000")

#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <ctime>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <deque>
#include <cassert>
#include <cstdlib>
#include <bitset>
#include <algorithm>
#include <string>
#include <list>
#include <fstream>
#include <cstring>
#include <climits>
#include <stack>
#include <unordered_map>
#include <unordered_set>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<pii> vpii;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<pair<ll, ll> > vpll;
typedef long double ld;

#define mk make_pair
#define inb push_back
#define outb pop_back
#define all(v) v.begin(), v.end()
#define X first
#define Y second
#define sqr(x) (x) * (x)
#define TIME clock() * 1.0 / CLOCKS_PER_SEC

const ld EPS = 1e-9;
const ld pi = acos(-1.0);

void mkfile();
int solve(int T);

int main()
{
#define TASK "theatre"
#ifdef _DEBUG
	mkfile();
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	freopen("test.txt", "w", stderr);
	ld tstart = TIME;
	srand(2299);
#else
	//freopen(TASK".in", "r", stdin), freopen(TASK".out", "w", stdout);
	//freopen("input.txt", "r", stdin), freopen("output.txt", "w", stdout), freopen("test.txt", "w", stderr);
	srand(228);
#endif
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i)
	{
		printf("Case #%d: ", i);
		solve(i);
	}
#ifdef _DEBUG
	ld tend = TIME;
	cerr << tend - tstart << " s.\n";
#endif
	return 0;
}

void mkfile()
{
	freopen("input.txt", "a+", stdout);
	srand(time(0));
	return;
}

bool equal(double a, double b)
{
	return abs(a - b) < EPS;
}

const int MAXN = (int)1e3 + 7;
const int INF = (int)2e9 + 7;
const ll LINF = (ll)7e18;
const ll MOD = (ll)1e9 + 7;

ll n, k;
map <pll, ll> cnt;

int solve(int T)
{
	cnt.clear();
	scanf("%lld %lld", &n, &k);
	queue <pll> q;
	cnt[mk(n / 2, (n - 1) / 2)] = 1;
	q.push(mk(n / 2, (n - 1) / 2));
	while (!q.empty() && k > 0)
	{
		pll cur = q.front();
		q.pop();
		k -= cnt[cur];
		if (k <= 0)
		{
			printf("%lld %lld\n", cur.X, cur.Y);
			return 0;
		}
		{
			pll nxt = mk(cur.X / 2, (cur.X - 1) / 2);
			if (cnt.find(nxt) == cnt.end())
				q.push(nxt);
			cnt[nxt] += cnt[cur];
		}
		{
			pll nxt = mk(cur.Y / 2, (cur.Y - 1) / 2);
			if (cnt.find(nxt) == cnt.end())
				q.push(nxt);
			cnt[nxt] += cnt[cur];
		}
	}
	return 0;
}