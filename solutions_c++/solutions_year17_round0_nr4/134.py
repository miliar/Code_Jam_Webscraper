#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<queue>
#include<vector>
using namespace std;
typedef pair<int, int> pii;
#define INF 2140000000
#define MAX_V 3005
struct edge {        // to : 목적지, c : 용량 , r: 역변 정보 : ad[i][j] 의 역엣지 = ad[ad[i][j].to][ad[i][j].r]
	int to, c, r;
};

int adn;
vector<edge> ad[MAX_V]; // 그래프 인접리스트
bool chk[MAX_V];        // DFS에서 방문 체크
int level[MAX_V];
int iter[MAX_V];

void inil()
{
	for (int i = 0; i < adn; i++)
	{
		ad[i].clear();
	}
}

void add_edge(int v1, int v2, int c) {  // v1->v2 로 용량 c의 엣지 추가
	edge e1 = { v2,c, ad[v2].size() };
	ad[v1].push_back(e1);
	edge e2 = { v1,0, ad[v1].size() - 1 };
	ad[v2].push_back(e2);
}

void bfs(int s) {                     // s로부터의 최단거리 계산
	memset(level, -1, sizeof(level));
	queue<int> q;
	level[s] = 0;
	q.push(s);
	while (!q.empty()) {
		int v = q.front();
		q.pop();
		for (int i = 0; i<ad[v].size(); i++) {
			edge &e = ad[v][i];
			if (e.c>0 && level[e.to]<0) {
				level[e.to] = level[v] + 1;
				q.push(e.to);
			}
		}
	}
}

int dfs(int v, int t, int f) {         // 증가경로를 DFS로 탐색
	if (v == t) return f;
	for (int &i = iter[v]; i<ad[v].size(); i++) {
		edge &e = ad[v][i];
		if (e.c>0 && level[v]<level[e.to]) {
			int d = dfs(e.to, t, min(f, e.c));
			if (d>0) {
				e.c -= d;
				ad[e.to][e.r].c += d;
				return d;
			}
		}
	}
	return 0;
}

int max_flow(int s, int t) {       // s->t 의 최대흐름 계산
	int flow = 0;
	while (true) {
		bfs(s);
		if (level[t]<0) return flow;
		memset(iter, 0, sizeof(iter));
		int f;
		while ((f = dfs(s, t, INF))>0) {
			flow += f;
		}
	}
}


int n, m;
vector<pii> vx;
vector<pii> vp;
vector<pii> vo;
int res;
int vxc[109][109];
int vpc[109][109];
void read_vpx() {
	int i, j;
	char xx[2];
	for (i = 0; i < n; i++)
		for (j = 0; j < n; j++)
			vpc[i][j] = vxc[i][j] = 0;
	while (m--) {
		scanf("%s %d %d", xx, &i, &j);
		i--; j--;
		if (xx[0] == '+' || xx[0] == 'o') {
			vpc[i][j] = 1;
		}
		if (xx[0] == 'x' || xx[0] == 'o') {
			vxc[i][j] = 1;
		}
	}
}
void build_vx()
{
	int i, j, k;
	adn = 2 * n + 2;
	inil();
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
			if (vxc[i][j])
				break;
		if(j==n)
			add_edge(adn - 2, i, 1);
		for (j = 0; j < n; j++)
			if (vxc[j][i])
				break;
		if(j==n)
			add_edge(i+n, adn-1, 1);
	}
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
		{
			if (vxc[i][j] == 0) {
				add_edge(i, j + n, 1);
			}
		}
	}
	max_flow(adn - 2, adn - 1);
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < ad[i].size(); j++)
		{
			if (ad[i][j].c == 0)
			{
				vxc[i][ad[i][j].to - n] = 2;
			}
		}
	}
}

pii vp_cross(int pi, int pj)
{
	pii res;
	//rx - ry = pi - n + 1
	//rx + ry = pj
	res.first = (pi + pj - n + 1) / 2;
	res.second = (pj - pi + n - 1) / 2;
	return res;
}
void build_vp()
{
	int i, j, k;
	adn = 2 * (2*n-1) + 2;
	inil();
	for (i = 0; i < 2*n-1; i++)
	{
		for (j = 0; j < n; j++)
		{
			// x - y == i - n + 1
			if(i - n + 1 + j >=0 && i - n + 1 + j < n)
				if (vpc[i-n+1+j][j])
					break;
		}
		if (j == n)
		{
			add_edge(adn - 2, i, 1);
		}
		for (j = 0; j < n; j++)
		{
			// x + y == i
			if (i - j >= 0 && i - j < n)
				if (vpc[i-j][j])
					break;
		}
		if (j == n)
		{
			add_edge(i + (2*n-1), adn - 1, 1);
		}
	}
	for (i = 0; i < 2*n-1; i++)
	{
		for (j = 0; j < 2*n-1; j++)
		{
			if ((i + j) % 2 != (n - 1) % 2) continue;
			pii cc = vp_cross(i, j);
//			printf("%d x %d --> %d %d\n", i, j, cc.first, cc.second);
			if(cc.first >= 0 && cc.first < n)
				if (cc.second >= 0 && cc.second < n)
				{
					if (vpc[cc.first][cc.second] == 0)
					{
						add_edge(i, j + 2 * n - 1, 1);
					}
				}
		}
	}
	max_flow(adn - 2, adn - 1);
	for (i = 0; i < 2*n-1; i++)
	{
		for (j = 0; j < ad[i].size(); j++)
		{
			if (ad[i][j].c == 0)
			{
				k = ad[i][j].to - 2 * n + 1;
				if (k >= 0 && k < 2 * n - 1)
					if((i+k)%2 == (n-1)%2)
				{
					pii cc = vp_cross(i, k);
//					printf(" -- %d x %d --> %d %d\n", i, k, cc.first, cc.second);
					vpc[cc.first][cc.second] = 2;
				}
			}
		}
	}
}
int main()
{
//	freopen("D-small-attempt0.in", "rt", stdin);
//	freopen("D-small-attempt0.out", "wt", stdout);
	freopen("D-large.in", "rt", stdin);
	freopen("D-large.out", "wt", stdout);
	
	int t, tv = 0;
	int i, j, k, l;
	scanf("%d", &t);
	while (t--)
	{
		scanf("%d %d", &n, &m);
		read_vpx();

		build_vx();
		build_vp();

		vp.clear();
		vx.clear();
		vo.clear();
		res = 0;
		for (i = 0; i < n; i++)
		{
			for (j = 0; j < n; j++)
			{
				if (vpc[i][j] == 1)
				{
					if (vxc[i][j] == 1) {
						res += 2;
					}
					else if (vxc[i][j] == 2) {
						res += 2;
						vo.push_back(pii(i, j));
					}
					else
					{
						res++;
					}
				}
				else if (vpc[i][j] == 2) {

					if (vxc[i][j] == 1) {
						res += 2;
						vo.push_back(pii(i, j));
					}
					else if (vxc[i][j] == 2) {
						res += 2;
						vo.push_back(pii(i, j));
					}
					else
					{
						res++;
						vp.push_back(pii(i, j));
					}
				}
				else
				{
					if (vxc[i][j] == 1) {
						res++;
					}
					else if (vxc[i][j] == 2) {
						res++;
						vx.push_back(pii(i, j));
					}
					else
					{
					}
				}
			}
		}
		printf("Case #%d: %d %d\n", ++tv, res, vo.size() + vp.size() + vx.size());
		for (i = 0; i < vo.size(); i++)
			printf("o %d %d\n", vo[i].first+1, vo[i].second+1);
		for (i = 0; i < vp.size(); i++)
			printf("+ %d %d\n", vp[i].first+1, vp[i].second+1);
		for (i = 0; i < vx.size(); i++)
			printf("x %d %d\n", vx[i].first+1, vx[i].second+1);
	}
}