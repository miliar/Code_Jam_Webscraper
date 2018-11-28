#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <cassert>
#include <numeric>
#include <string>
#include <cstring>
#include <cmath>
using namespace std;

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif

typedef long long int int64;


namespace Hung
{
	const int INF = (int)1e9;
	const int N = 103;
	int n, m;
	int a[N][N];
	int mt[N];
	int way[N];
	int minDist[N];
	int v[N], u[N];
	bool used[N];

	void hungarian()
	{
//		memset(a, 0, sizeof a);
		memset(mt, 0, sizeof mt);
		memset(way, 0, sizeof way);
		memset(minDist, 0, sizeof minDist);
		memset(v, 0, sizeof v);
		memset(u, 0, sizeof u);
		memset(used, 0, sizeof used);
		
		for (int it = 1; it <= n; it++)
		{
			mt[0] = it;
			for (int i = 1; i <= m; i++)
			{
				minDist[i] = INF;
				way[i] = -1;
				used[i] = false;
			}
			int col = 0;
			while(mt[col])
			{
				used[col] = 1;
				int row = mt[col];
				int ncol = -1;
				int delta = INF;
				for (int c = 1; c <= m; c++)
				{
					if (used[c]) continue;
					int d = a[row][c] + v[row] + u[c];
					if (d < minDist[c])
					{
						way[c] = col;
						minDist[c] = d;
					}
					if (minDist[c] < delta)
					{
						delta = minDist[c];
						ncol = c;
					}
				}
				for (int i = 0; i <= m; i++)
				{
					if (used[i])
					{
						u[i] += delta;
						v[mt[i]] -= delta;
					}
					else
						minDist[i] -= delta;
				}
				col = ncol;
			}
			while(col)
			{
				mt[col] = mt[way[col]];
				col = way[col];
			}
		}
		return;
	}
};


int DX[4] = {-1, 0, 0, 1};
int DY[4] = {0, -1, 1, 0};

const int N = 105;
char f[N][N];
pair <int, int> pS[N], pT[N];
int r, c;
int m;
int S, T;

vector <int> turels[N][N];
int reach[N][N];

bool inF(int x, int y)
{
	return x >= 0 && x < r && y >= 0 && y < c;
}

void clear()
{
	S = 0;
	T = 0;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			turels[i][j].clear();
	memset(reach, -1, sizeof reach);
}

void markTurelDir(int id, int dir)
{
	int x = pT[id].first;
	int y = pT[id].second;

	while (inF(x, y) && f[x][y] != '#')
	{
//		eprintf("%d, %d <- %d\n", x, y, id);
		turels[x][y].push_back(id);
		x += DX[dir];
		y += DY[dir];
	}
}

void markTurel(int id)
{
	for (int d = 0; d < 4; d++)
		markTurelDir(id, d);
}

void markTurels()
{
	for (int i = 0; i < T; i++)
		markTurel(i);
}


pair <int, int> qu[N * N];
int dist[N][N];


bool used[N];
int mt[N];
int rmt[N];

bool tryKuhn(int v)
{
	used[v] = true;
	for (int to = 0; to < T; to++)
	{
		if (reach[v][to] == -1) continue;
		if (mt[to] == -1 || (!used[mt[to] ] && tryKuhn(mt[to] ) ) )
		{
			mt[to] = v;
			return true;
		}
	}
	return false;
}

void goS(int id)
{
	memset(dist, -1, sizeof dist);
	int qul = 0, qur = 0;
	qu[qur++] = pS[id];
	dist[pS[id].first][pS[id].second] = 0;

	while (qul < qur)
	{
		int x = qu[qul].first;
		int y = qu[qul].second;
		qul++;
		int cd = dist[x][y];
		
//		eprintf("%d reach %d, %d by %d\n", id, x, y, cd);

		for (int dir = 0; dir < 4; dir++)
		{
			int nx = x + DX[dir];
			int ny = y + DY[dir];
			if (!inF(nx, ny) || f[nx][ny] == '#') continue;
			if (dist[nx][ny] != -1) continue;
			dist[nx][ny] = cd + 1;
			qu[qur++] = make_pair(nx, ny);
		}
	}
	for (int x = 0; x < r; x++)
		for (int y = 0; y < c; y++)
		{
			int cd = dist[x][y];
			if (cd == -1 || cd > m) continue;
			for (int tid : turels[x][y] )
			{
				if (reach[id][tid] == -1 || reach[id][tid] > cd)
					reach[id][tid] = cd;
			}
		}
}

void goS()
{
	for (int i = 0; i < S; i++)
		goS(i);
}

void solve()
{
	clear();


	scanf("%d%d%d", &c, &r, &m);
	for (int i = 0; i < r; i++)
		scanf("%s", f[i] );
	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++)
		{
			if (f[i][j] == 'S')
				pS[S++] = make_pair(i, j);
			if (f[i][j] == 'T')
				pT[T++] = make_pair(i, j);
		}
	markTurels();
	goS();
//	eprintf("end go\n");
	

	T = max(T, S);
	memset(mt, -1, sizeof mt);
	
	int ansk = 0;
	for (int i = 0; i < S; i++)
	{
		memset(used, false, sizeof used);
		if (tryKuhn(i) ) ansk++;
	}

	memset(used, false, sizeof used);

//	eprintf("m = %d\n", m);
	for (int i = 0; i < S; i++)
	{
		for (int j = 0; j < T; j++)
		{
//			eprintf("%d ", reach[i][j] );
			if (reach[i][j] != -1 && reach[i][j] <= m)
				Hung::a[i + 1][j + 1] = reach[i][j];
			else
				Hung::a[i + 1][j + 1] = N * N;
		}
//		eprintf("\n");
	}

	Hung::n = S;
	Hung::m = T;
	Hung::hungarian();
	
	int ans = 0;
	for (int i = 0; i < T; i++)
	{
		if (Hung::mt[i + 1] != 0 && Hung::a[Hung::mt[i + 1] ][i + 1] != N * N)
		{
			mt[i] = Hung::mt[i + 1] - 1;
//			eprintf("%d - %d\n", mt[i], i);
			ans++;
		}
		else
			mt[i] = -1;
	}

//	eprintf("ans = %d, ansk = %d\n", ans, ansk);
	if (ans != ansk) throw;


	memset(rmt, -1, sizeof rmt);
	for (int i = 0; i < T; i++)
		if (mt[i] != -1)
			rmt[mt[i] ] = i;

	printf("%d\n", ans);
//	eprintf("ans = %d\n", ans);

	memset(used, false, sizeof used);
	for (int it = 0; it < ans; it++)
	{
		for (int i = 0; i < S; i++)
		{
			if (rmt[i] == -1 || used[rmt[i] ] ) continue;

			bool bad = false;
			for (int j = 0; j < T; j++)
			{
				if (!used[j] && reach[i][j] != -1 && reach[i][j] < reach[i][rmt[i] ] )
					bad = true;
			}
			if (bad) continue;
			printf("%d %d\n", i + 1, rmt[i] + 1);
			used[rmt[i] ] = true;
			break;
		}
	}

}

void multitest()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		printf("Case #%d: ", i);
		eprintf("Case #%d .. %d\n", i, n);
		solve();
	}
}

int main(int argc, char **)
{
	if (argc == 1)
		multitest();
	else
		solve();

	return 0;
}


