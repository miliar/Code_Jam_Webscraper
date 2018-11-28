#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
using namespace std;

typedef long long int lli;
typedef long double dbl;

const lli maxn = 105, inf = lli(1e15)+5;

lli E[maxn], S[maxn], D[maxn][maxn];
dbl V[maxn];
vector<pair<lli, dbl>> graph[maxn];

void dijkstra(lli node)
{
	set<pair<dbl, lli>> Q;
	Q.insert({0.00, node});
	V[node] = 0.00;
	while(!Q.empty())
	{
		pair<dbl, lli> top = *Q.begin();
		Q.erase(Q.begin());

		for(auto it: graph[top.second])
		{
			if(V[it.first] > top.first+it.second)
			{
				if(V[it.first] != inf) Q.erase({V[it.first], it.first});
				V[it.first] = top.first+it.second;
				Q.insert({V[it.first], it.first});
			}
		}
	}
}

void solve()
{
	lli n, q, u, v;
	scanf("%lld%lld", &n, &q);
	for(lli i = 0;i < n;i++) scanf("%lld%lld", &E[i], &S[i]);

	for(lli i = 0;i < n;i++)
	{
		for(lli j = 0;j < n;j++)
		{
			scanf("%lld", &D[i][j]);
			if(i == j) D[i][j] = 0;
			else if(D[i][j] == -1) D[i][j]= inf;
		}
	}

	for(lli k = 0;k < n;k++)
	{
		for(lli i = 0;i < n;i++)
		{
			for(lli j = 0;j < n;j++)
			{
				D[i][j] = min(D[i][j], D[i][k]+D[k][j]);
			}
		}
	}

	for(lli i = 0;i < n;i++)
	{
		graph[i].clear();
		for(lli j = 0;j < n;j++)
		{
			if(D[i][j] <= E[i]) graph[i].push_back({j, dbl(D[i][j])/S[i]});
		}
	}

	while(q--)
	{
		scanf("%lld%lld", &u, &v);
		u--, v--;
		for(lli i = 0;i < n;i++) V[i] = inf;
		dijkstra(u);
		printf("%.10Lf ", V[v]);
	}
	printf("\n");
}


int main(void)
{
	lli t;
	scanf("%lld", &t);
	for(lli tst = 1;tst <= t;tst++)
	{
		printf("Case #%lld: ", tst);
		solve();
	}
}