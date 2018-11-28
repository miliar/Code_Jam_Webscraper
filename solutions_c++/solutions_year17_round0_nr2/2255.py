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

ll n;

int solve(int T)
{
	scanf("%lld", &n);
	vi a;
	ll c = n;
	while (c)
		a.inb(c % 10), c /= 10;
	ll ans = 0;
	for (int i = 0; i < a.size() - 1; ++i)
	{
		if (a[i] < a[i + 1])
		{
			for (int j = 0; j <= i; ++j)
				a[j] = 9;
			--a[i + 1];
		}
	}
	reverse(all(a));
	for (int i = 0; i < a.size(); ++i)
	{
		ans = ans * 10ll + a[i];
	}
	printf("%lld\n", ans);
	return 0;
}