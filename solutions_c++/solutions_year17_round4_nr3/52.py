


                #include <string>
#include <vector>
#include <map>
#include <list>
#include <iterator>
#include <cassert>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>
#include <time.h>
using namespace std;

#define FOR(i, a, b) for(int i=(a);i<(b);i++)
#define RFOR(i, b, a) for(int i=(b)-1;i>=(a);--i)
#define FILL(A,value) memset(A,value,sizeof(A))

#define ALL(V) V.begin(), V.end()
#define SZ(V) (int)V.size()
#define PB push_back
#define MP make_pair
#define Pi 3.14159265358979
#define x0 ikjnrmthklmnt
#define y0 lkrjhkltr
#define y1 ewrgrg

typedef long long Int;
typedef unsigned long long UInt;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef pair<Int, Int> PLL;
typedef pair<long double, long double> PDD;

const int INF = 1000000000;
const int BASE = 1000000007;
const int MAX = 1007;
const int MAX2 = 10007;
const int MAXE = 100000;
const int ADD = 1000000;
const int MOD = 1000000007;
const int CNT = 0;

string s[57];
int n , m;
int cnt;

vector<int> A[57][57];

set<PII> S;
bool ok;

int dx[4] = {0,-1,0,1};
int dy[4] = {1,0,-1,0};



bool inside(int x, int y)
{
	return x >= 0 && y >= 0 && x < n && y < m;
}

void go(int x, int y, int dir)
{
	if (!ok) return;
	if (s[x][y] == '/')
	{
		int dd = dir;
		if (dd == 0) dir = 1;
		if (dd == 1) dir = 0;
		if (dd == 2) dir = 3;
		if (dd == 3) dir = 2;
	}
	if (s[x][y] == '\\')
	{
		int dd = dir;
		if (dd == 0) dir = 3;
		if (dd == 1) dir = 2;
		if (dd == 2) dir = 1;
		if (dd == 3) dir = 0;
	}

	if (s[x][y] == '.')
		S.insert(MP(x , y));

	x += dx[dir];
	y += dy[dir];
	if (!inside(x , y)) return;
	if (s[x][y] == '#') return;

	if (s[x][y] == '-' || s[x][y] == '|')
	{
		ok = 0;
		return;
	}

	go(x , y , dir);
}

VI G[5007];
VI GR[5007];
bool U[5007];
VI order;
int C[5007];

void dfs1(int v)
{
	U[v] = 1;
	FOR(i,0,SZ(G[v]))
	{
		int to = G[v][i];
		if (U[to]) continue;
		dfs1(to);
	}
	order.push_back(v);
}

void dfs2(int v, int c)
{
	C[v] = c;
	FOR(i,0,SZ(GR[v]))
	{
		int to = GR[v][i];
		if (C[to] != -1) continue;
		dfs2(to, c);
	}
}

int main()
{
	freopen("in.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);

	int t;
	cin >> t;
	FOR(tt,0,t)
	{
		printf("Case #%d: " , tt + 1);

		cin >> n >> m;
		FOR(i,0,n)
		{
			cin >> s[i];
		}

		cnt = 0;

		FOR(i,0,5007)
		{
			G[i].clear();
			GR[i].clear();
		}

		FOR(i,0,n)
			FOR(j,0,m)
				A[i][j].clear();

		bool nosol = 0;
		FOR(i,0,n)
		{
			FOR(j,0,m)
			{
				if (nosol) break;
				if (s[i][j] == '-' || s[i][j] == '|')
				{
					S.clear();
					ok = 1;
					go(i, j, 0);
					go(i, j, 2);
					bool ok1 = ok;
					if (ok)
					{
						for(set<PII>::iterator it = S.begin(); it != S.end(); ++it)
						{
							A[it->first][it->second].push_back(cnt * 2);
						}
					}

					S.clear();
					ok = 1;
					go(i, j, 1);
					go(i, j, 3);
					bool ok2 = ok;
					if (ok)
					{
						for(set<PII>::iterator it = S.begin(); it != S.end(); ++it)
						{
							A[it->first][it->second].push_back(cnt * 2 + 1);
						}
					}

					if (!ok1 && !ok2)
					{
						nosol = 1;
						break;
					}
					if (!ok1)
					{
						G[cnt * 2].push_back(cnt * 2 + 1);
						GR[cnt * 2 + 1].push_back(cnt * 2);
					}
					if (!ok2)
					{
						GR[cnt * 2].push_back(cnt * 2 + 1);
						G[cnt * 2 + 1].push_back(cnt * 2);
					}

					++ cnt;
				}
			}
		}



		FOR(i,0,n)
		{
			FOR(j,0,m)
			{
				if (nosol) break;
				if (s[i][j] == '.')
				{
					if (SZ(A[i][j]) == 0)
					{
						nosol = 1;
						break;
					}
					if (SZ(A[i][j]) == 1)
					{
						G[A[i][j][0] ^ 1].push_back(A[i][j][0]);
						GR[A[i][j][0]].push_back(A[i][j][0] ^ 1);
					}
					if (SZ(A[i][j]) == 2)
					{
						G[A[i][j][0] ^ 1].push_back(A[i][j][1]);
						GR[A[i][j][1]].push_back(A[i][j][0] ^ 1);

						G[A[i][j][1] ^ 1].push_back(A[i][j][0]);
						GR[A[i][j][0]].push_back(A[i][j][1] ^ 1);
					}
				}
			}
		}
		if (nosol)
		{
			cout << "IMPOSSIBLE" << endl;
			continue;
		}

		FILL(U, 0);
		order.clear();

		FOR(i,0,2 * cnt)
		{
			if (!U[i])
				dfs1(i);
		}

		FILL(C, -1);
		int c = 0;
		RFOR(i,SZ(order), 0)
		{
			int v = order[i];
			if (C[v] != -1) continue;
			dfs2(v , c);
			++ c;
		}

		vector<bool> res;

		FOR(i,0,cnt)
		{
			if (C[2 * i] == C[2 * i + 1])
			{
				nosol = 1;
			}
			else
			{
				if (C[2 * i] > C[2 * i + 1])
				{
					res.push_back(0);
				}
				else
				{
					res.push_back(1);
				}
			}
		}
		if (nosol)
		{
			cout << "IMPOSSIBLE" << endl;
			continue;
		}

		RFOR(i,n,0)
		{
			RFOR(j,m,0)
			{
				if (s[i][j] == '-' || s[i][j] == '|')
				{
					if (res.back())
					{
						s[i][j] = '|';
					}
					else
					{
						s[i][j] = '-';
					}
					res.pop_back();
				}
			}
		}
		cout << "POSSIBLE" << endl;
		FOR(i,0,n)
		{
			cout << s[i] << endl;
		}

	}


    return 0;
}






