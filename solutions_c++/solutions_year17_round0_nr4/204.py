#include <bits/stdc++.h>

using namespace std;

#define REP(i, a, b) for (int i = (a), i##_end_ = (b); i < i##_end_; ++i)
#define debug(...) fprintf(stderr, __VA_ARGS__)
#define mp make_pair
#define x first
#define y second
#define pb push_back
#define SZ(x) (int((x).size()))
#define ALL(x) (x).begin(), (x).end()

template<typename T> inline bool chkmin(T &a, const T &b) { return a > b ? a = b, 1 : 0; }
template<typename T> inline bool chkmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }

typedef long long LL;

const int oo = 0x3f3f3f3f;

const int maxn = 510;

int n, m;
char a[maxn + 5][maxn + 5];

bool visrow[maxn + 5];
int linkrow[maxn + 5];
bool fixedcol[maxn + 5];

bool vismain[(maxn << 1) + 5];
int linkmain[(maxn << 1) + 5];
bool fixedanti[maxn + 5];

inline bool findrow(int x)
{
	if (fixedcol[x]) return 0;
	REP(y, 0, n) 
	{
		if (!visrow[y])
		{
			visrow[y] = 1;
			if (!~linkrow[y] || findrow(linkrow[y])) { linkrow[y] = x; return 1; }
		}
	}
	return 0;
}

inline bool findmain(int sum)
{
	if (fixedanti[sum]) return 0;
	REP(y, 0, n)
	{
		int x = sum - y;
		if (x < 0 || x >= n) continue;
		if (!vismain[x - y + n])
		{
			vismain[x - y + n] = 1;
			if (!~linkmain[x - y + n] || findmain(linkmain[x - y + n])) { linkmain[x - y + n] = x + y; return 1; }
		}
	}
	return 0;
}

int main()
{
#ifdef matthew99
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int case_count;
	scanf("%d", &case_count);
	for (int case_id = 1; case_id <= case_count; ++case_id)
	{
		printf("Case #%d: ", case_id);
		memset(a, '.', sizeof a);
		memset(linkrow, -1, sizeof linkrow);
		memset(linkmain, -1, sizeof linkmain);
		memset(fixedcol, 0, sizeof fixedcol);
		memset(fixedanti, 0, sizeof fixedanti);
		int ans = 0;
		scanf("%d%d", &n, &m);
		REP(i, 0, m)
		{
			static char s[10];
			int x, y;
			scanf("%s%d%d", s, &x, &y), --x, --y;
			a[x][y] = s[0];
			if (a[x][y] == '+') ++ans;
			else if (a[x][y] == 'x') ++ans;
			else ans += 2;
			if (a[x][y] != '+') linkrow[x] = y, fixedcol[y] = 1;
			if (a[x][y] != 'x') linkmain[x - y + n] = x + y, fixedanti[x + y] = 1;
		}
		REP(i, 0, n) if (!fixedcol[i])
		{
			memset(visrow, 0, sizeof visrow);
			if (findrow(i)) ++ans;
		}
		REP(i, 0, n << 1) if (!fixedanti[i])
		{
			memset(vismain, 0, sizeof vismain);
			if (findmain(i)) ++ans;
		}
		vector<pair<int, int> > changed;
		REP(i, 0, n) REP(j, 0, n)
		{
			bool flag = 0;
			if (!fixedcol[j] && linkrow[i] == j)
			{
				if (a[i][j] == '+') a[i][j] = 'o';
				else a[i][j] = 'x';
				flag = 1;
			}
			if (!fixedanti[i + j] && linkmain[i - j + n] == i + j)
			{
				if (a[i][j] == 'x') a[i][j] = 'o';
				else a[i][j] = '+';
				flag = 1;
			}
			if (flag) changed.pb(mp(i, j));
		}
		printf("%d %d\n", ans, SZ(changed));
		for (auto u : changed) printf("%c %d %d\n", a[u.x][u.y], u.x + 1, u.y + 1);
	}
	return 0;
}
