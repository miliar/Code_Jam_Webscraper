#include <cstdio>
#include <memory.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <numeric>
#define min(x, y) (y ^ ((x ^ y) & -(x < y)))
#define max(x, y) (x ^ ((x ^ y) & -(x < y)))
using namespace std;
typedef long long LL;
typedef double D;

struct edge
{
	int from, to, cap, flow;
};

const int N = 500;
vector<int> G[N];
vector <edge> E;
int q[N], level[N], ptr[N], s, t;

void add_edge(int from, int to, int cap)
{
	G[from].push_back((int)E.size());
	E.push_back({from, to, cap, 0});
	G[to].push_back((int)E.size());
	E.push_back({to, from, 0, 0});
}

bool bfs()
{
	int l = 0, r = 0;
	memset(level, -1, sizeof(level));
	level[s] = 0;
	q[r++] = s;
	while (l < r && level[t] == -1)
	{
		int v = q[l++];
		for (int id : G[v])
		{
			int to = E[id].to;
			if (level[to] == -1 && E[id].flow < E[id].cap)
			{
				level[to] = level[v] + 1;
				q[r++] = to;
			}
		}
	}
	return level[t] != -1;
}

int dfs(int v, int flow)
{
	if (!flow)
		return 0;
	if (v == t)
		return flow;
	for (; ptr[v] < G[v].size(); ++ptr[v])
	{
		int id = G[v][ptr[v]], to = E[id].to;
		if (level[to] == level[v] + 1)
		{
			int pushed = dfs(to, min(flow, E[id].cap - E[id].flow));
			if (pushed)
			{
				E[id].flow += pushed;
				E[id ^ 1].flow -= pushed;
				return pushed;
			}
		}
	}
	return 0;
}

const int INF = 1e9;
int dinic()
{
	int flow = 0;
	while(bfs())
	{
		memset(ptr, 0, sizeof(ptr));
		while (int pushed = dfs(s, INF))
			flow += pushed;
	}
	return flow;
}

int origin[101][101];
bool pl[101][101], cr[101][101];
bool R[101], C[101], Rpl[300], Rcr[101], Cpl[300], Ccr[101];
int n;

pair<int, int> diag(int i, int j)//R, C
{
	return {n + i - j, i + j - 1};
}

pair<int, int> normal(int k, int l)//R, C
{
	return {(l - n + k + 1) / 2, (n + l - k + 1) / 2};
}

int main()
{
	freopen("out.txt", "w", stdout);
	freopen("in.txt", "r", stdin);
	int T, m;
	char c;
	cin >> T;
	for (int k = 0; k < T; ++k)
	{
		cin >> n >> m;
		//clear
		memset(origin, 0, sizeof(origin));
		memset(pl, 0, sizeof(pl));
		memset(cr, 0, sizeof(cr));
		memset(R, 0, sizeof(R));
		memset(C, 0, sizeof(C));
		memset(Rpl, 0, sizeof(Rpl));
		memset(Cpl, 0, sizeof(Cpl));
		memset(Rcr, 0, sizeof(Rcr));
		memset(Ccr, 0, sizeof(Ccr));
		//
		
		//set
		for (int l = 0; l < m; ++l)
		{
			int i, j;
			cin >> c >> i >> j;
			if (c == '+') {origin[i][j] = 1; Rpl[diag(i, j).first] = Cpl[diag(i, j).second] = 1; pl[i][j] = 1;}
			if (c == 'x') {origin[i][j] = 2; Rcr[i] = Ccr[j] = 1; cr[i][j] = 1;};
			if (c == 'o') {origin[i][j] = 3; Rpl[diag(i, j).first] = Cpl[diag(i, j).second] = 1; pl[i][j] = 1; Rcr[i] = Ccr[j] = 1; cr[i][j] = 1;}
			if (origin[i][j])
				R[i] = C[j] = 1;
		}
		//
		
		//'x'
		s = 0; t = n * 2 + 1;
		for (int i = 0; i < 500; ++i)
			G[i].clear();
		E.clear();
		
		for (int i = 1; i <= n; ++i)
		{
			if (!Ccr[i])
				add_edge(s, i, 1);
			if (!Rcr[i])
				add_edge(i + n, t, 1);
			for (int j = 1; j <= n; ++j)
			{
				if (!Rcr[j] && !Ccr[i])
					add_edge(i, j + n, 1);
			}
		}
		
		dinic();
		for (int i = 0; i < E.size(); i += 2)
			if (E[i].from != s && E[i].to != t && E[i].flow)
				cr[E[i].to - n][E[i].from] = 1;
		//
		
		//'+'
		s = 0; t = n * 4 - 1;
		for (int i = 0; i < 500; ++i)
			G[i].clear();
		E.clear();
		
		for (int i = 1; i <= n * 2 - 1; ++i)
		{
			if (!Cpl[i])
				add_edge(s, i, 1);
			if (!Rpl[i])
				add_edge(i + 2 * n - 1, t, 1);
		}
		
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j)
				if (!Rpl[diag(i, j).first] && !Cpl[diag(i, j).second])
					add_edge(diag(i, j).second, diag(i, j).first + 2 * n - 1, 1);
		
		dinic();
		for (int i = 0; i < E.size(); i += 2)
			if (E[i].from != s && E[i].to != t && E[i].flow)
				pl[normal(E[i].to - (2 * n - 1), E[i].from).first][normal(E[i].to - (2 * n - 1), E[i].from).second] = 1;
		//
		
		//result
		int cnt = 0, points = 0;
		for (int i = 1; i <= n; ++i)
		{
			for (int j = 1; j <= n; ++j)
			{
				if (origin[i][j] == 3)
				{
					points += 2;
					continue;
				}
				if ((origin[i][j] == 1 && cr[i][j]) || (origin[i][j] == 2 && pl[i][j]))
				{
					cnt++;
					points += 2;
					continue;
				}
				if (origin[i][j] == 1 || origin[i][j] == 2)
				{
					points++;
					continue;
				}
				if (pl[i][j] && cr[i][j])
				{
					points += 2;
					cnt++;
					continue;
				}
				if (pl[i][j] || cr[i][j])
				{
					points += 1;
					cnt++;
					continue;
				}
			}
		}
		cout << "Case #" << k + 1 << ": " << points << ' ' << cnt << '\n';
		for (int i = 1; i <= n; ++i)
		{
			for (int j = 1; j <= n; ++j)
			{
				if (origin[i][j] == 3)
					continue;
				if ((origin[i][j] == 1 && cr[i][j]) || (origin[i][j] == 2 && pl[i][j]))
				{
					cout << "o " << i << ' ' << j << '\n';
					continue;
				}
				if (origin[i][j] == 1 || origin[i][j] == 2)
					continue;
				if (pl[i][j] && cr[i][j])
				{
					cout << "o " << i << ' ' << j << '\n';
					continue;
				}
				if (pl[i][j])
				{
					cout << "+ " << i << ' ' << j << '\n';
					continue;
				}
				if (cr[i][j])
				{
					cout << "x " << i << ' ' << j << '\n';
					continue;
				}
			}
		}
		//
	}

	fclose(stdout);
	fclose(stdin);
}

//const int n = 40;
//int G[n][4];
//bool used[n];
//int mass[n];
//int color[n];
//
//int dfs(int v, int clr)
//{
//	int res = 1;
//	color[v] = clr;
//	used[v] = 1;
//	for (int i = 0; i < 4; ++i)
//	{
//		if (G[v][i] == -1)
//			continue;
//		int to = G[v][i];
//		if (!used[to])
//			res += dfs(to, clr);
//	}
//	return res;
//}
//
//int N, M;
//int num(int i, int j)
//{
//	return i * M + j;
//}
//
//bool arr[2001][2001];
//int last[2001];
//int main()
//{
//	memset(G, -1, sizeof(G));
//	memset(last, -1, sizeof(last));
//	char c;
//	cin >> N >> M;
//	for (int i = 0; i < N; ++i)
//		for (int j = 1; j <= M; ++j)
//		{
//			cin >> c;
//			arr[i][j] = c == '+';
//		}
//	
//	int lst = -1;
//	for (int j = 1; j <= M; ++j)
//	{
//		if (lst != -1)
//			G[num(0, j)][1] = num(0, lst);
//		if (arr[0][j])
//		{
//			G[num(0, lst)][0] = num(0, j);
//			last[j] = 0;
//			lst = j;
//		}
//	}
//	
//	for (int i = 1; i < N; ++i)
//	{
//		lst = -1;
//		for (int j = 1; j <= M; ++j)
//		{
//			if (last[j] != -1)
//				G[num(i, j)][3] = num(last[j], j);
//			if (lst != -1)
//				G[num(i, j)][1] = num(i, lst);
//			
//			if (arr[i][j])
//			{
//				G[num(last[j], j)][2] = num(i, j);
//				G[num(i, lst)][0] = num(i, j);
//				last[j] = i;
//				lst = j;
//			}
//		}
//	}
//	
//	lst = -1;
//	for (int j = M; j >= 1; --j)
//	{
//		if (lst != -1)
//			G[num(N - 1, j)][1] = num(N - 1, lst);
//		if (arr[N - 1][j])
//		{
//			G[num(N - 1, lst)][0] = num(N - 1, j);
//			last[j] = 0;
//			lst = j;
//		}
//	}
//	
//	for (int i = N - 2; i >= 0; --i)
//	{
//		lst = -1;
//		for (int j = M; j >= 1; --j)
//		{
//			if (last[j] != -1)
//				G[num(i, j)][3] = num(last[j], j);
//			if (lst != -1)
//				G[num(i, j)][1] = num(i, lst);
//			
//			if (arr[i][j])
//			{
//				G[num(last[j], j)][2] = num(i, j);
//				G[num(i, lst)][0] = num(i, j);
//				last[j] = i;
//				lst = j;
//			}
//		}
//	}
//	
//	int mx = 0, R = 0, C = 0, clr = 1;
//	
//	for (int i = 0; i < N; ++i)
//		for (int j = 1; j <= M; ++j)
//		{
//			if (arr[i][j])
//				continue;
//			int val = 0;
//			vector<int> temp;
//			
//			for (int k = 0; k < 4; ++k)
//			{
//				if (G[num(i, j)][k] == -1)
//					continue;
//				
//				bool b = 1;
//				for (int l = 0; l < temp.size(); ++l)
//					if (color[G[num(i, j)][k]] == temp[l])
//					{
//						b = 0;
//						break;
//					}
//				if (b)
//				{
//					if (mass[color[G[num(i, j)][k]]])
//						val += mass[color[G[num(i, j)][k]]];
//					else
//					{
//						mass[clr] = dfs(G[num(i, j)][k], clr);
//						val += mass[clr];
//						clr++;
//					}
//					temp.push_back(color[G[num(i, j)][k]]);
//				}
//			}
//			
//			if (val > mx)
//			{
//				mx = val;
//				R = i + 1;
//				C = j;
//			}
//		}
//	cout << mx << '\n';
//	if (mx)
//		cout << R << ' ' << C;
//}


////#include <stdio.h>
//#include <memory.h>
//#include <algorithm>
//#include <iostream>
//#include <string>
//#include <vector>
//#define min(x, y) (y ^ ((x ^ y) & -(x < y)))
//#define max(x, y) (x ^ ((x ^ y) & -(x < y)))
//using namespace std;
//typedef long long LL;
//typedef double D;
//
//LL dp[60] = {0, 3};
//LL sum[60] = {0, 3};
//
//char f(char last, LL n)
//{
//	switch (last)
//	{
//		case 'a':
//		{
//			return 'b' + n;
//		}
//		case 'c':
//		{
//			return 'a' + n;
//		}
//	}
//	if (!n)
//		return 'a';
//	else
//		return 'c';
//}
//int main()
//{
//	LL n, k;
//	cin >> n >> k;
//	for (int i = 2; i <= 57; ++i)
//	{
//		dp[i] = dp[i - 1] << 1;
//		sum[i] = sum[i - 1] + dp[i];
//	}
//	if (n > 57)
//		n = 57;
//	if (k > sum[n])
//	{
//		cout << "NO";
//		return 0;
//	}
//	char last = (char)((k - 1) / (sum[n] / 3LL) + 'a');
//	cout << last;
//	k = (k - 1) % (sum[n] / 3LL) + 1;
//	n--;
//	while(n)
//	{
//		if (k == 1LL)
//			return 0;
//		else
//			k--;
//		last = f(last, (k - 1) / (sum[n] / 3LL));
//		k = (k - 1) % (sum[n] / 3LL) + 1;
//		cout << last;
//		n--;
//	}
//}
//
//
//
//
//
//
//
//
//
