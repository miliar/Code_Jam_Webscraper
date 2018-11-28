#include<stdio.h>
#include<algorithm>
#include<vector>
using namespace std;
int n, m, c;
struct T
{
	int p;
	int b;
}tickets[1010];

int N, M, A[1010], B[1010];
vector<int> adj[1010];
bool visited[1010];
bool dfs(int a)
{
	visited[a] = true;
	for(int b: adj[a])
	{
		if(B[b] == -1 || !visited[B[b]] && dfs(B[b]))
		{
			A[a] = b;
			B[b] = a;
			return true;
		}
	}
	return false;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int i, j, T, tt;
	scanf("%d", &T);
	for(tt=1; tt<=T; ++tt)
	{
		vector<int> c1, c2;
		scanf("%d%d%d", &n, &c, &m);
		for(i=1; i<=m; ++i)
		{
			scanf("%d%d", &tickets[i].p, &tickets[i].b);
			if(tickets[i].b == 1) c1.push_back(tickets[i].p);
			else c2.push_back(tickets[i].p);
		}
		if(c1.size()*c2.size()==0)
		{
			printf("Case #%d: %d 0\n", tt, m);
			continue;
		}
		sort(c1.begin(), c1.end());
		sort(c2.begin(), c2.end());
		int x, y;
		x = c1.size()>c2.size()?c1.size():c2.size();
		y = c1.size() + c2.size() - x;
		N = c1.size();
		M = c2.size();
		for(i=0; i<N; ++i)
		{
			adj[i].clear();
			for(j=0; j<M; ++j)
			{
				if(c1[i] != c2[j]) adj[i].push_back(j);
			}
		}
		int match=0;
		for(i=0; i<N; ++i) A[i]=-1;
		for(i=0; i<M; ++i) B[i]=-1;
		for(i=0; i<N; ++i)
		{
			if(A[i]!=-1) continue;
			for(j=0; j<N; ++j) visited[j]=false;
			if(dfs(i)) ++match;
		}
		if(N<M)
		{
			for(i=0; i<N; ++i)
			{
				if(c1[i]==1 && A[i]==-1)
				{
					++x;
					++match;
				}
			}
		}
		else
		{
			for(i=0; i<M; ++i)
			{
				if(c2[i]==1 && B[i]==-1)
				{
					++x;
					++match;
				}
			}
		}
		y = y-match;
		printf("Case #%d: %d %d\n", tt, x, y);
	}
}
