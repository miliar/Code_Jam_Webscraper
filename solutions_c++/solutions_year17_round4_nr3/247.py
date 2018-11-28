#include<cstdio>
#include <vector>
#include <cstring>
#include <map>
const int MAXN = 2600;
const int SIZE = 2 * MAXN + 1;
using namespace std;

int n;

bool assn[2600];
char grid[64][64];
int gn, gm;
int ind[64][64];
//ver: +1
//hor: -1
int dx[4] = { 0, -1, 0, 1 }, dy[4] = { -1, 0, 1, 0 }; //ver, hor, ver, hor
int r1[4] = { 3, 2, 1, 0 }; // '/'
int r2[4] = { 1, 0, 3, 2 }; // '\'
//up, left, down, right
vector<pair<int, int>> clauses;
bool twosat();
int get_ray(int x, int y, int k)
{
	if (x<1 || y<1 || x>gn || y>gm) return 0;
	if (grid[x][y] == '#') return 0;
	if (ind[x][y]) return ind[x][y];
	if (grid[x][y] == '/') k = r1[k];
	else if (grid[x][y] == '\\') k = r2[k];
	return get_ray(x + dx[k], y + dy[k], k);
}
bool setup_graph()
{
	int i, j, k;
	for (i = 1; i <= gn; i++)
	{
		for (j = 1; j <= gm; j++)
		{
			int xs[4] = { 0, 0, 0, 0 };
			if (grid[i][j] == '.')
			{
				for (k = 0; k < 4; k++)
					xs[k] = get_ray(i + dx[k], j + dy[k], k);
				if (xs[0] && xs[1] && xs[2] && xs[3]) return false;
				int ver = (xs[0] && xs[2]) ? 0 : xs[0] + xs[2];
				int hor = (xs[1] && xs[3]) ? 0 : xs[1] + xs[3];
				if (ver && hor)
					clauses.push_back(make_pair(ver, -hor));
				else if (ver)
					clauses.push_back(make_pair(ver, ver));
				else if (hor)
					clauses.push_back(make_pair(-hor, -hor));
				else return false;
			}
			else if (grid[i][j] == '-' || grid[i][j] == '|')
			{
				for (k = 0; k < 4; k++)
					xs[k] = get_ray(i + dx[k], j + dy[k], k);
				bool ver = (xs[0] || xs[2]);
				bool hor = (xs[1] || xs[3]);
				int cur = ind[i][j];
				if (ver && hor) return false;
				else if (ver)
					clauses.push_back(make_pair(-cur, -cur));
				else if (hor)
					clauses.push_back(make_pair(cur, cur));
			}
		}
	}
	return true;
}
int main()
{
	int i, j;
	int tc;
	scanf("%d", &tc);
	for (int t = 1; t <= tc; t++)
	{
		scanf("%d%d", &gn, &gm);
		for (i = 1; i <= gn; i++) scanf("%s", &grid[i][1]);
		n = 0;
		for (i = 1; i <= gn; i++)
		{
			for (j = 1; j <= gm; j++)
			{
				if (grid[i][j] == '-' || grid[i][j] == '|')
					ind[i][j] = ++n;
				else ind[i][j] = 0;
			}
		}
		printf("Case #%d: ", t);
		clauses.clear();
		if (!setup_graph())
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		if (!twosat())
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		printf("POSSIBLE\n");
		for (i = 1; i <= gn; i++)
		{
			for (j = 1; j <= gm; j++)
			{
				if (ind[i][j])
				{
					if (!assn[ind[i][j]]) grid[i][j] = '|';
					else grid[i][j] = '-';
				}
			}
		}
		for (i = 1; i <= gn; i++) printf("%s\n", &grid[i][1]);
	}
	return 0;
}



// Assuming vertices are labeled 1...V
vector <int> G[SIZE], Grev[SIZE];
bool explored[SIZE];
int leader[SIZE], finish[SIZE], order[SIZE], t, parent;
map <int, bool> truthAssignment;

// running DFS on the reverse graph
void dfs_reverse(int i) {
	explored[i] = true;
	for (auto it = Grev[i].begin(); it != Grev[i].end(); it++)
		if (!explored[*it])
			dfs_reverse(*it);
	t++;
	finish[i] = t;
}

// running DFS on the actual graph
void dfs(int i) {
	explored[i] = true;
	leader[i] = parent;
	for (auto it = G[i].begin(); it != G[i].end(); it++)
		if (!explored[*it])
			dfs(*it);
}

// check if u & v are in the same connected component
bool stronglyConnected(int u, int v) {
	return leader[u] == leader[v];
}

bool twosat()
{
	int i, u, v, N = n;
	// N is the number of variables and M is the number of clauses
	for (i = 0; i < SIZE; i++)
	{
		G[i].clear(); Grev[i].clear();
	}
	memset(explored, false, sizeof(explored));
	memset(leader, 0, sizeof(leader));
	memset(finish, 0, sizeof(finish));
	memset(order, 0, sizeof(order));
	t = 0; parent = 0;
	truthAssignment.clear();
	for (i = 0; i < clauses.size(); i++)
	{
		/*  Each clause is of the form u or v
			1 <= x <= N for an uncomplemented variable x
			-N <= x <= -1 for a complemented variable x
			-x is the complement of a variable x
		*/
		u = clauses[i].first;
		v = clauses[i].second;
		if (u > 0) {
			if (v > 0) {
				G[N + u].push_back(v); G[N + v].push_back(u);
				Grev[v].push_back(N + u); Grev[u].push_back(N + v);
			}
			else {
				G[N + u].push_back(N - v); G[-v].push_back(u);
				Grev[N - v].push_back(N + u); Grev[u].push_back(-v);
			}
		}
		else {
			if (v > 0) {
				G[-u].push_back(v); G[N + v].push_back(N - u);
				Grev[v].push_back(-u); Grev[N - u].push_back(N + v);
			}
			else {
				G[-u].push_back(N - v); G[-v].push_back(N - u);
				Grev[N - v].push_back(-u); Grev[N - u].push_back(-v);
			}
		}
	}

	// run dfs on the reverse graph to get reverse postorder
	memset(explored, false, (2 * N + 1) * sizeof(bool));
	for (i = 2 * N; i > 0; i--) {
		if (!explored[i])
			dfs_reverse(i);
		order[finish[i]] = i;
	}

	// run dfs on the actual graph in reverse postorder
	memset(explored, false, (2 * N + 1) * sizeof(bool));
	for (i = 2 * N; i > 0; i--)
		if (!explored[order[i]]) {
			parent = order[i];
			dfs(order[i]);
		}
	// check if a variable and its complement belong in the same SCC in reverse postorder
	// and assign truth values to SCC
	for (i = 2 * N; i > 0; i--) {
		u = order[i];
		if (u > N) {
			if (stronglyConnected(u, u - N)) break;
			if (truthAssignment.find(leader[u]) == truthAssignment.end()) {
				truthAssignment[leader[u]] = true;
				truthAssignment[leader[u - N]] = false;
			}
		}
		else {
			if (stronglyConnected(u, N + u)) break;
			if (truthAssignment.find(leader[u]) == truthAssignment.end()) {
				truthAssignment[leader[u]] = true;
				truthAssignment[leader[N + u]] = false;
			}
		}
	}

	if (i > 0) return false;
	for (i = 1; i <= N; i++)
		assn[i] = truthAssignment[leader[i]];
	return true;
}
