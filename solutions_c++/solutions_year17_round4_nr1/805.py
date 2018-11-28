#define _CRT_SECURE_NO_DEPRECATE
#pragma comment (linker, "/stack:256000000")

#include <iostream>
#include <cstdio>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <queue>
#include <deque>
#include <set>
#include <bitset>
#include <map>
#include <memory.h>
#undef NDEBUG
#include <cassert>
#include <ctime>

using namespace std;

#define fo(a,b,c) for (int a = (b); a < (c); a++)
#define fr(a,b) fo(a, 0, (b))
#define fi(n) fr(i, (n))
#define fj(n) fr(j, (n))
#define fk(n) fr(k, (n))
#define fd(a,b,c) for (int a = (b); a >= (c); a--)
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define _(a,b) memset((a), (b), sizeof(a))
#define __(a) memset((a), 0, sizeof(a))
#define sz(a) (int)(a).size()
#define mp make_pair
#define pb push_back

typedef long long lint;
typedef unsigned long long ull;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int, int> pii;

const int INF = 1000000000;
const lint LINF = 4000000000000000000LL;
const double eps = 1e-9;

int ni() { int a; scanf( "%d", &a ); return a; }
double nf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; string ns() { scanf( "%s", sbuf ); return sbuf; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }

void prepare()
{
	freopen("input.txt", "r", stdin);
	freopen("a-small.in", "r", stdin);
	freopen("a-small.out", "w", stdout);
	freopen("a-large.in", "r", stdin);
	freopen("a-large.out", "w", stdout);
}

const int maxn = 105;

int n, p, a[maxn];
int dp[maxn][maxn][maxn][5];
int cnt[5];

void read()
{
	n = ni();
	p = ni();
	fi(n)
		a[i] = ni();
}

int modp(int x)
{
	while (x >= p)
		x -= p;
	return x;
}

int getOne(int x)
{
	return x == 0 ? 1 : 0;
}

void upd(int &d, int nd)
{
	d = max(d, nd);
}

void solve(int test_num)
{
	//cerr << test_num << endl;
	printf("Case #%d: ", test_num);
	__(cnt);
	_(dp, -1);
	fi(n)
		cnt[a[i] % p]++;
	dp[0][0][0][0] = 0;
	fi(cnt[1] + 1)
	{
		fj(cnt[2] + 1)
		{
			fk(cnt[3] + 1)
			{
				fo(rem, 0, p)
				{
					if (dp[i][j][k][rem] < 0)
						continue;
					int p1 = modp(rem + 1);
					int p2 = modp(rem + 2);
					int p3 = modp(rem + 3);
					upd(dp[i + 1][j][k][p1], dp[i][j][k][rem] + getOne(rem));
					upd(dp[i][j + 1][k][p2], dp[i][j][k][rem] + getOne(rem));
					upd(dp[i][j][k + 1][p3], dp[i][j][k][rem] + getOne(rem));
				}
			}
		}
	}
	int res = 0;
	fi(p)
	{
		res = max(res, dp[cnt[1]][cnt[2]][cnt[3]][i]);
	}
	res += cnt[0];
	printf("%d\n", res);
}

int main()
{
	prepare();
	int number_of_tests;
	scanf("%d\n", &number_of_tests);
	fi(number_of_tests)
	{
		read();
		solve(i + 1);
	}
	return 0;
}