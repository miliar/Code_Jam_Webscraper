#include <bits/stdc++.h>
using namespace std;

#define MAX_X 1005
#define MAX_Y MAX_X
#define MAX_EDGE_NUM 1000005
#define MAX_NODE_NUM MAX_X
//if xi and yj are connected, add (i, j) as an edge.
struct Edge
{
	int v, next;
	Edge()
	{}
	Edge(int v, int next):v(v), next(next)
	{}
} edge[MAX_EDGE_NUM];

int head[MAX_NODE_NUM];
int edge_cnt;
bool vis[MAX_X];
int match[MAX_X];
int x_num, y_num;

void init_edge()
{
	memset(head, -1, sizeof(head));
	edge_cnt = 0;
}

void add_edge(int u, int v)
{
	edge[edge_cnt] = Edge(v, head[u]);
	head[u] = edge_cnt++;
}

bool find_match(int a)
{
	for (int i = head[a]; ~i; i = edge[i].next)
	{
		int v = edge[i].v;
		if (vis[v])
			continue;
		vis[v] = true;
		if (match[v] == -1 || find_match(match[v]))
		{
			match[v] = a;
			return true;
		}
	}
	return false;
}

int max_match()
{
	memset(match, -1, sizeof(match));
	for (int i = 0; i < x_num; i++)
	{
		memset(vis, 0, sizeof(vis));
		find_match(i);
	}
	int ans = 0;
	for (int i = 0; i < y_num; i++)
		if (match[i] != -1)
			ans++;
	return ans;
}

void init_match(int x, int y)
{
	x_num = x;
	y_num = y;
}

int n, m, c;
vector<int> c1, c2;

void input() {
	c1.clear();
	c2.clear();
	scanf("%d%d%d", &n, &c, &m);
	int c11 = 0;
	int c21 = 0;
	for (int i = 0; i < m; i++) {
		int a, b;
		scanf("%d%d", &a, &b);
		if (b == 1) {
			c1.push_back(a);
			if (a == 1)
				c11++;
		} else {
			c2.push_back(a);
			if (a == 1)
				c21++;
		}
	}
	int ret = c11 + c21;
	int c1r = max(0, int(c1.size() - c21 - c11));
	int c2r = max(0, int(c2.size() - c11 - c21));
	ret += max(c1r, c2r);
	printf("%d ", ret);
	init_edge();
	for (int i = 0; i < c1.size(); i++) {
		for (int j = 0; j < c2.size(); j++) {
			if (c1[i] != c2[j] && c1[i] != 1 && c2[j] != 1) {
				add_edge(i, j);
			}
		}
	}
	init_match(c1.size(), c2.size());
	int match = max_match();
	int second = min(int((c1.size() - c11 - match) - c21), int((c2.size() - c21 - match) - c11));
	second = max(0, second);
	printf("%d\n", second);
}

int main()
{
	int t;
	scanf("%d", &t);
	int case_num = 0;
	while (t--)
	{
		case_num++;
		printf("Case #%d: ", case_num);
		input();
	}
	return 0;
}
