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

const int MAXN = 10 * 1000 + 41;

int n, p;
int a[MAXN];
int cnt[MAXN];

void print(lint x)
{
	cout << x;
	cerr << x;
}

void read()
{
	cin >> n >> p;
	fi(n)
		cin >> a[i];
}

void solve()
{
	int ans = 0;
	int rest = 0;

	fi(p + 1)
		cnt[i] = 0;

	fi(n)
		cnt[a[i] % p] ++;

	if (p == 2)
	{
		ans = cnt[0] + (cnt[1] + 1) / 2;
	} 
	else if (p == 3)
	{
		int d = max(cnt[1], cnt[2]) - min(cnt[1], cnt[2]);
		ans = cnt[0] + min(cnt[1], cnt[2]) + (d + 2) / 3;
	}
	else if (p == 4)
	{
		ans = cnt[0];
		int m = min(cnt[1], cnt[3]);
		cnt[1] -= m;
		cnt[3] -= m;
		int rest = max(cnt[1], cnt[3]);
		ans += m;

		ans += cnt[2] / 2;
		cnt[2] %= 2;

		if (cnt[2] == 0)
		{
			ans += (rest + 3) / 4;
		}
		else
		{
			ans++;
			if (rest > 2)
			{
				rest -= 2;
				ans += (rest + 3) / 4;
			}
		}
	}
	
	print(ans);
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
