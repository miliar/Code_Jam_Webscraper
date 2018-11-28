#include <stdio.h>
#include <bits/stdc++.h>

using namespace std;

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

#ifdef ROOM_311
__attribute__((destructor)) void fini_main()
{
	fprintf(stderr, "Execution time = %0.0lf ms\n", clock() * 1000.0 / CLOCKS_PER_SEC);
}
#endif

#define MY_RAND 1
#if MY_RAND
uint64_t rnd_data = 0xDEADBEEFDULL;
inline void my_srand(int seed) { rnd_data = ((uint64_t)seed << 16) | 0x330E; }
inline int my_rand() { rnd_data = rnd_data * 0x5DEECE66DULL + 0xB; return (rnd_data >> 17) & 0x7FFFFFFF; }
#define rand my_rand
#define srand my_srand
template <typename T> void my_random_shuffle(T b, T e) { for(ssize_t i = 1; i < (e - b); i++) { swap(b[i], b[rand() % (i + 1)]); } }
#define random_shuffle my_random_shuffle
#endif

template <class _T> inline _T sqr(const _T &x) { return x * x; }

// Types
typedef long double ld;
typedef long long i64;
typedef __int128 i128;
typedef unsigned long long u64;
typedef set < int > SI;
typedef vector < int > VI;
typedef map < string, int > MSI;
typedef pair < int, int > PII;

// Constants
const ld PI = 3.1415926535897932384626433832795;
const ld EPS = 1e-9;

const int dx[4] = {-1, 0, 1, 0};
const int dy[4] = {0, 1, 0, -1};

int qq;
int n, m, k, kk;
char a[52][52];
int b[102][2];
int c[52][52][2];
VI g[202];
VI rg[202];
int u[52][52];
int t[202];
int tt;
bool u1[202];
int col[202];
VI comp[202];
int cs;
int e[202];

int go(int &x, int &y, int &dir)
{
	int xn = x + dx[dir];
	int yn = y + dy[dir];
	if (xn < 0 || xn >= n || yn < 0 || yn >= m || a[xn][yn] == '#') return 0;
	x = xn;
	y = yn;
	if (a[x][y] == '|' || a[x][y] == '-') return -1;
	if (a[x][y] == '/')
	{
		static const int dd[4] = {1, 0, 3, 2};
		dir = dd[dir];
	}
	if (a[x][y] == '\\')
	{
		static const int dd[4] = {3, 2, 1, 0};
		dir = dd[dir];
	}
	return 1;
}

void check(int x0, int y0, int v)
{
	forn(i, 2)
	{
		clr(u);
		forn(j, 2)
		{
			int x = x0;
			int y = y0;
			int dir = i + j * 2;
			int t;
//			cerr << x << " " << y << " " << dir << endl;
			while ((t = go(x, y, dir)) > 0)
			{
//				cerr << x << " " << y << " " << dir << endl;
				u[x][y] = (dir & 1) ? 1 : 2;
			}
//			cerr << "t = " << t << endl;
			if (t < 0)
			{
//				cerr << x0 << " " << y0 << " " << v << " " << i << " " << j << endl;
				g[v + k * i].pb(v + k * (1 - i));
			}
		}
		forn(x, n)
		{
			forn(y, m)
			{
				if (a[x][y] == '.' && u[x][y])
				{
					c[x][y][u[x][y] - 1] = v + i * k;
				}
			}
		}
	}
}

void dfs1(int v)
{
	u1[v] = true;
	fori(it, g[v])
	{
		if (u1[*it]) continue;
		dfs1(*it);
	}
	t[tt++] = v;
}

void dfs2(int v, int cc)
{
	u1[v] = true;
	col[v] = cc;
	comp[cc].pb(v);
	fori(it, rg[v])
	{
		if (u1[*it]) continue;
		dfs2(*it, cc);
	}
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
		
		scanf("%d%d", &n, &m);
		forn(i, n)
		{
			scanf("%s", a[i]);
		}
		k = 0;
		forn(i, n)
		{
			forn(j, m)
			{
				if (a[i][j] == '-' || a[i][j] == '|')
				{
					b[k][0] = i;
					b[k][1] = j;
					k++;
				}
			}
		}
		memset(c, 0xff, sizeof(c));
		forn(i, k)
		{
			check(b[i][0], b[i][1], i);
		}
		bool ok = true;
		forn(x, n)
		{
			forn(y, m)
			{
				if (a[x][y] == '.')
				{
					int v1, v2;
					if (c[x][y][0] < 0 && c[x][y][1] < 0) ok = false;
					else if (c[x][y][0] >= 0 && c[x][y][1] >= 0)
					{
						v1 = c[x][y][0];
						v2 = c[x][y][1];
					}
					else
					{
						v1 = v2 = max(c[x][y][0], c[x][y][1]);
					}
					g[(v1 + k) % (k * 2)].pb(v2);
					g[(v2 + k) % (k * 2)].pb(v1);
				}
			}
		}
		kk = k * 2;
		forn(i, kk)
		{
			fori(it, g[i])
			{
				rg[*it].pb(i);
			}
		}
		memset(e, 0xff, sizeof(e));
		clr(u1);
		tt = 0;
		forn(i, kk)
		{
			if (u1[i]) continue;
			dfs1(i);
		}
		clr(u1);
		cs = 0;
		ford(i1, kk)
		{
			int i = t[i1];
			if (u1[i]) continue;
			dfs2(i, cs);
			int r[202] = {};
			fori(it, comp[cs])
			{
				int v = *it;
				r[v % k]++;
				if (e[v] < 0)
				{
					e[v] = 0;
					e[(v + k) % kk] = 1;
				}
			}
			forn(j, kk)
			{
				if (r[j] > 1) ok = false;
			}
			cs++;
		}
		if (!ok) printf("IM");
		puts("POSSIBLE");
		if (ok)
		{
			forn(i, k)
			{
				int x = b[i][0];
				int y = b[i][1];
				if (e[i] < 0)
				{
					cerr << "Botwa !!!" << endl;
				}
				a[x][y] = e[i] ? '|' : '-';
			}

			forn(i, n)
			{
				puts(a[i]);
			}
		}

		forn(i, kk)
		{
			g[i].clear();
			rg[i].clear();
		}
		forn(i, cs)
		{
			comp[i].clear();
		}
		
		fflush(stdout);
	}

	return 0;
}
