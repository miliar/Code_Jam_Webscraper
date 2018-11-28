#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define bublic public
#define clr(x) memset((x), 0, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define sz size()
#define For(i, st, en) for(int i=(st); i<=(int)(en); i++)
#define Ford(i, st, en) for(int i=(st); i>=(int)(en); i--)
#define forn(i, n) for(int i=0; i<(int)(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)
#define fori(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); it++)

template <class _T> inline _T sqr(const _T& x) { return x * x; }
template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }

typedef long double ld;

// Constants
const ld PI = 3.1415926535897932384626433832795;
const ld EPS = 1e-11;

// Types
typedef long long i64;
typedef __int128 i128;
typedef unsigned long long u64;
typedef set < int > SI;
typedef vector < int > VI;
typedef map < string, int > MSI;
typedef pair < int, int > PII;

int qq;
int n, m;
int gs;
bool a[2][102][102];
bool b[2][102][102];
bool g[202][202];
int pa[202];
bool u[202];

bool find(int k)
{
	u[k] = true;
	forn(i, gs)
	{
		if (g[k][i] && (pa[i] < 0 || (!u[pa[i]] && find(pa[i]))))
		{
			pa[i] = k;
			return true;
		}
	}
	return false;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	scanf("%d", &qq);
	forn(ii, qq)
	{
		printf("Case #%d: ", ii+1);
		fprintf(stderr, "Case #%d:\n", ii+1);
		
		clr(a);
		clr(b);
		scanf("%d%d", &n, &m);
		int ans = 0;
		forn(i, m)
		{
			char cc;
			int x, y;
			scanf(" %c%d%d", &cc, &x, &y);
			x--;
			y--;
			if (cc == 'o' || cc == '+')
			{
				a[0][x][y] = true;
				ans++;
			}
			if (cc == 'o' || cc == 'x')
			{
				a[1][x][y] = true;
				ans++;
			}
		}
		int add_cnt = 0;
		bool u1[202] = {};
		bool u2[202] = {};
		forn(i, n)
		{
			forn(j, n)
			{
				if (a[0][i][j])
				{
					u1[i + j] = true;
					u2[i - j + n - 1] = true;
				}
			}
		}
		clr(g);
		forn(i, n)
		{
			forn(j, n)
			{
				if (!u1[i + j] && !u2[i - j + n - 1])
				{
					g[i + j][i - j + n - 1] = true;
				}
			}
		}
		gs = n + n - 1;
		memset(pa, 0xff, sizeof(pa));
		forn(i, gs)
		{
			clr(u);
			find(i);
		}
		forn(i, gs)
		{
			if (pa[i] >= 0)
			{
				int s = pa[i];
				int d = i;
				b[0][(s + d - n + 1) / 2][(s - d + n - 1) / 2] = true;
				ans++;
			}
		}
		clr(u1);
		clr(u2);
		forn(i, n)
		{
			forn(j, n)
			{
				if (a[1][i][j])
				{
					u1[i] = true;
					u2[j] = true;
				}
			}
		}
		clr(g);
		forn(i, n)
		{
			forn(j, n)
			{
				if (!u1[i] && !u2[j])
				{
					g[i][j] = true;
				}
			}
		}
		gs = n;
		memset(pa, 0xff, sizeof(pa));
		forn(i, gs)
		{
			clr(u);
			find(i);
		}
		forn(i, gs)
		{
			if (pa[i] >= 0)
			{
				int s = pa[i];
				int d = i;
				b[1][s][d] = true;
				ans++;
			}
		}

		forn(i, n)
		{
			forn(j, n)
			{
				if (b[0][i][j] || b[1][i][j])
				{
					add_cnt++;
				}
			}
		}

		printf("%d %d\n", ans, add_cnt);
		forn(i, n)
		{
			forn(j, n)
			{
				if (b[0][i][j] || b[1][i][j])
				{
					int mask = 0;
					if (b[0][i][j] || a[0][i][j]) mask |= 1;
					if (b[1][i][j] || a[1][i][j]) mask |= 2;
					char cc = mask == 1 ? '+' : mask == 2 ? 'x' : 'o';
					printf("%c %d %d\n", cc, i + 1, j + 1);
				}
			}
		}
		
		fflush(stdout);
	}

	return 0;
}
