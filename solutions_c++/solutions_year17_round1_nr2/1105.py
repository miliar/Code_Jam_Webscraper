#include <bits/stdc++.h>

#define For(i, a, b) for (int i = (a); i < (b); ++i)
#define INF 100000000

using namespace std;

typedef pair<int, int> ii;

struct edge
{
int v,rev,cap,flow;
edge(int _v,int _rev,int _cap,int _flow)
{
v=_v;
rev=_rev;
cap=_cap;
flow=_flow;
}
edge(){}
};

int need[55];
int package[55][55];
set<int> servings[55][55];

vector<ii> path;
vector<vector<edge>> AdjList;
int f=0;

void addEdge(int u,int v,int cap)
{
	//printf("add edge %d %d, %d\n", u, v, cap);
int k=AdjList[v].size(),l=AdjList[u].size();
AdjList[u].push_back(edge(v,k,cap,0));
AdjList[v].push_back(edge(u,l,0,0));
}

void augment(int s,int v,int min_edge)
{
if(v==s)
{
f=min_edge;
return;
}
int u=path[v].first,i=path[v].second;
if(u!=-1)
{
int res=AdjList[u][i].cap - AdjList[u][i].flow;
augment(s,u,min(res,min_edge));
AdjList[u][i].flow+=f;
AdjList[v][AdjList[u][i].rev].flow-=f;
}
}

int maxFlow(int s,int t,int N)
{
int maxflow=0;
path.resize(N);
while(true)
{
f=0;
vector<int>dist(N,INF);
vector<bool>visit(N,false);
path[t]=make_pair(-1,-1);
queue<int>cola;
cola.push(s);
visit[s]=true;
while(!cola.empty())
{
int u=cola.front();cola.pop();
if(u==t)
break;
For(i,0,(int)AdjList[u].size())
{
edge e=AdjList[u][i];
if(!visit[e.v] and e.cap - e.flow>0)
cola.push(e.v),visit[e.v]=true,path[e.v]=make_pair(u,i);
}
}
augment(s,t,INF);
if(!f)
break;
maxflow+=f;
}
return maxflow;
}

int main()
{
	int tt, caso = 1;
	scanf("%d", &tt);

	while (tt--) {
		int n, p;
		scanf("%d %d", &n, &p);

		for (int i = 0; i < n; i++)
			scanf("%d", &need[i]);

		for (int i = 0; i < n; ++i)
			for (int j = 0; j < p; ++j)
				scanf("%d", &package[i][j]);

		for (int i = 0; i < n; ++i)
			for (int j = 0; j < p; ++j)
			{
				servings[i][j].clear();
				int exact = package[i][j] / need[i];
				//printf("exact: %d\n", exact);
				for (int k = exact; k > 0 and package[i][j]*100/(k*need[i]) <= 110; k--)
					servings[i][j].insert(k); //printf("(%d, %d) k:%d\n", i, j, package[i][j]*100/(k*need[i]));
				for (int k = exact+1; package[i][j]*100/(k*need[i]) >= 90; k++)
					servings[i][j].insert(k); //printf("(%d, %d) k:%d\n", i, j, package[i][j]*100/(k*need[i]));
			}

		/*for (int i = 0; i < n; ++i)
			for (int j = 0; j < p; ++j)
			{
				printf("%d %d:", i, j);
				for (int s : servings[i][j])
					printf("%d ", s);
				printf("\n");
			}

		continue;*/

		AdjList.assign(n*p*2+2, vector<edge>());

		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < p; ++j) 
			{
				int u = i*p+j;
				int in = u*2, out = u*2 + 1;

				addEdge(in, out, 1);
				if (i != n-1)
					for (int k = 0; k < p; ++k)
					{
						int v = (i+1)*p+k;
						int inNext = v*2;
						for (int s : servings[i][j])
							if (servings[i+1][k].count(s))
							{
								addEdge(out, inNext, INF);
								break;
							}
					} 
			}	
		}


		for (int j = 0; j < p; ++j)
		{
			if (servings[0][j].size())
				addEdge(n*p*2, (0*p+j)*2, INF);
			if (servings[n-1][j].size())
				addEdge(2*((n-1)*p+j)+1, n*p*2+1, INF);
		}

		printf("Case #%d: %d\n", caso++, maxFlow(n*p*2, n*p*2+1, n*p*2+2));
	}
	
	return 0;
}