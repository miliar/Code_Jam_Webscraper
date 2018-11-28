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
	freopen("b-small.in", "r", stdin);
	freopen("b-small.out", "w", stdout);
	freopen("b-large.in", "r", stdin);
	freopen("b-large.out", "w", stdout);
}

const int maxn = 10100;

int ac, aj, cs[maxn], ce[maxn], js[maxn], je[maxn];
int dp[2][900][2];
int w[maxn];

void read()
{
	scanf("%d%d", &ac, &aj);
	fi(ac)
		scanf("%d%d", &cs[i], &ce[i]);
	fi(aj)
		scanf("%d%d", &js[i], &je[i]);
}

void upd(int &d, int nv)
{
	d = min(d, nv);
}

void solve(int test_num)
{
	cerr << test_num << endl;
	printf("Case #%d: ", test_num);
	__(dp);
	__(w);
	fi(ac)
	{
		fo(j, cs[i], ce[i])
			w[j] = 1;
	}
	fi(aj)
	{
		fo(j, js[i], je[i])
			w[j] = 2;
	}
	int start = -1;
	fi(24 * 60)
	{
		if (w[i])
		{
			start = i;
			break;
		}
	}
	if (start < 0)
	{
		printf("2\n");
		return;
	}
	int tt = 24 * 60;
	int cr = 0, nx = 1;
	_(dp, 63);
	dp[0][0][0] = 0;
	dp[0][0][1] = 0;
	fi(tt)
	{
		int curT = (i + start) % tt;
		int nextT = (curT + 1) % tt;
		_(dp[nx], 63);
		fk(721)
		{
			fj(2)
			{
				int curV = dp[cr][k][j];
				if (w[curT] != 1)
					upd(dp[nx][k + 1][0], curV + (j == 0 ? 0 : 1));
				if (w[curT] != 2)
					upd(dp[nx][k][1], curV + (j == 1 ? 0 : 1));
			}
		}
		swap(nx, cr);
	}
	int res = INF;
	res = min(res, dp[cr][720][0] + (w[start] == 2 ? 0 : 1));
	res = min(res, dp[cr][720][1] + (w[start] == 1 ? 0 : 1));
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