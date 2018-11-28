#include <cstdio>
#include <iostream>
#include <cstring>
#define db(x) cout<<#x<<"="<<(x)<<" "
#define el cout<<endl
#define c0 first
#define c1 second
#define tr(p) for(edge *lk = p; lk; lk=lk->next)
#define su lk->t
using namespace std;

const int MXN = 210;
char sgnmap[4] = {'\0', 'x', '+', 'o'};
typedef long long ll;
typedef pair<int, int> PII;

struct edge
{
	int t;edge *next;
}epool[(MXN * MXN)<<1], *ecnt = epool;

edge *E[MXN];

void addedge(int x, int y)
{
	*ecnt = (edge){y, E[x]}, E[x] = ecnt++;
}



int cas, tcas;

int N, M;


int px[MXN], py[MXN], pxy[MXN], pyx[MXN];



int start[MXN][MXN], ans[MXN][MXN];


void init()
{
	scanf("%d %d\n", &N, &M);
	memset(px, 0, sizeof(px));
	memset(py, 0 ,sizeof(py));
	memset(pxy, 0, sizeof(pxy));
	memset(pyx, 0 ,sizeof(pyx));

	for(int i = 1; i <= N; ++i)
		for(int j = 1; j <= N; ++j)
			ans[i][j] = start[i][j] = 0;

	for(int i = 0; i < M; ++i)
	{
		int x, y;char ch;
		scanf("%c %d %d\n", &ch, &x, &y);
		if (ch == 'x' || ch == 'o')
		{
			px[x] = 1;
			py[y] = 1;
			ans[x][y] |= 1;
			start[x][y] |= 1;
		}
		if (ch == '+' || ch == 'o')
		{
			pxy[x + y - 1] = 1;
			pyx[x - y + N] = 1;
			ans[x][y] |= 2;
			start[x][y] |= 2;
		}
	}
}

namespace solve
{

	int tim = 0;
	int ma[MXN], vis[MXN];
	/*
	 * hungary algorithm.
	 *
	 * start from node u, expand the flow.
	 */
	int match(int u)
	{
		tr(E[u])if (vis[su] != tim)
		{
			vis[su] = tim;
			if (!ma[su] || match(ma[su]))
			{
				ma[su] = u;
				return 1;
			}
		}
		return 0;
	}

	int score;
	static PII pa[MXN * MXN];int n;
	void solve()
	{
		n = 0;score = 0;

		tim = 0;
		for(int u = 0; u <= N*2; ++u)
			vis[u] = ma[u] = 0, E[u] = 0; ecnt = epool;

		for(int i = 1; i <= N; ++i)
			for(int j = 1; j <= N; ++j)
				if (!px[i] && !py[j])
				{
					addedge(i, j);//db(i),db(j),el;
				}

		for(int u = 0; u <= N*2; ++u)
		{
			++tim;
			if (match(u))
			{
				//++ score;
			}
		}
		for(int i = 1; i <= N; ++i)
			if (ma[i] != 0)
				ans[ma[i]][i] |= 1;



		tim = 0;
		for(int u = 0; u <= N*2; ++u)
			vis[u] = ma[u] = 0, E[u] = 0; ecnt = epool;

		for(int i = 1; i <= N; ++i)
			for(int j = 1; j <= N; ++j)
				if (!pxy[i + j - 1] && !pyx[i - j + N])
				{
					addedge(i + j - 1, i - j + N);
				}

		for(int u = 1; u <= N + N - 1; ++u)
		{
			++tim;
			if (match(u))
			{
				//++ score;
			}
		}
		for(int i = 1; i <= N + N - 1; ++i)
			if (ma[i] != 0)
			{
				int x = ma[i], y = i;
				ans[(x + y - N + 1) >> 1][(x - y + N + 1) >> 1] |= 2;
			}

		for(int i = 1; i <= N; ++i)
			for(int j = 1; j <= N; ++j)
				score += (ans[i][j] & 1) + (ans[i][j] >> 1);
		for(int i = 1; i <= N; ++i)
			for(int j = 1; j <= N; ++j)
				if (ans[i][j] != start[i][j])
				{
					pa[++n] = PII(i, j);
				}
		/*
		el;
		for(int i = 1; i <= N; ++i)
		{
			for(int j = 1; j <= N; ++j) printf("%d", ans[i][j]);
				el;
		}
		*/


		printf("%d %d\n", score, n);
		for(int i = 1; i <= n; ++i)
		{
			int x, y;
			x = pa[i].c0, y = pa[i].c1;
			printf("%c %d %d\n", sgnmap[ans[x][y]], x, y);
		}
	}
}

int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	scanf("%d", &cas);
	for(tcas = 0; tcas < cas; ++tcas)
	{
		init();
		printf("Case #%d: ", tcas + 1);
		solve::solve();
	}
	return 0;
}
