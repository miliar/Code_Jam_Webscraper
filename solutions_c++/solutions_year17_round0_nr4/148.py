#include <bits/stdc++.h>
using namespace std;

#define SOURCE 0
#define SINK 1
#define OFF1 2
#define OFF2 250

deque<int> graph[2][500];
int res[2][500][500];
int grid[100][100];
int vis[500];
int n,m;

void connect(int k, int a, int b)
{
	graph[k][a].push_back(b);
	graph[k][b].push_back(a);
	res[k][a][b] = 1;
	res[k][b][a] = 0;
}

int getdiag(int a, int b)
{
	return a+b;
}

int getadiag(int a, int b)
{
	return a-b+n-1;
}

int rec(int k, int u)
{
	if(u==SINK)
		return 1;
	vis[u] = 1;

	for(int i=0; i<graph[k][u].size(); i++)
	{
		int v = graph[k][u][i];
		if(vis[v] || res[k][u][v]==0)
			continue;
		if(rec(k,v))
		{
			res[k][u][v]--;
			res[k][v][u]++;
			return 1;
		}
	}

	return 0;
}

int main()
{
	int t;
	scanf("%d",&t);

	for(int cn=1; cn<=t; cn++)
	{
		cin >> n >> m;

		for(int i=0; i<2; i++)
			for(int j=0; j<500; j++)
				graph[i][j].clear();

		for(int j=0; j<n; j++)
			connect(0,SOURCE,j+OFF1);

		for(int j=0; j<n; j++)
			for(int k=0; k<n; k++)
				connect(0,j+OFF1,k+OFF2);

		for(int j=0; j<n; j++)
			connect(0,j+OFF2,SINK);

		for(int j=0; j<2*n-1; j++)
			connect(1,SOURCE,j+OFF1);

		for(int j=0; j<n; j++)
			for(int k=0; k<n; k++)
				connect(1,getdiag(j,k)+OFF1,getadiag(j,k)+OFF2);

		for(int j=0; j<2*n-1; j++)
			connect(1,j+OFF2,SINK);

		for(int i=0; i<n; i++)
			for(int j=0; j<n; j++)
				grid[i][j] = 0;

		int ans = 0;
		for(int i=0; i<m; i++)
		{
			string str;
			int a,b;
			cin >> str >> a >> b;
			a--,b--;
			if(str[0]=='o')
				ans+=2, grid[a][b] = 2;
			else
				ans++, grid[a][b] = 1;

			int d = getdiag(a,b);
			int ad = getadiag(a,b);
			if(str[0]=='x')
				res[0][SOURCE][a+OFF1] = res[0][b+OFF2][SINK] = res[0][a+OFF1][b+OFF2] = 0;
			else if(str[0]=='+')
				res[1][SOURCE][d+OFF1] = res[1][ad+OFF2][SINK] = res[1][d+OFF1][ad+OFF2] = 0;
			else
			{
				res[0][SOURCE][a+OFF1] = res[0][b+OFF2][SINK] = res[0][a+OFF1][b+OFF2] = 0;
				res[1][SOURCE][d+OFF1] = res[1][ad+OFF2][SINK] = res[1][d+OFF1][ad+OFF2] = 0;
			}
		}


		for(int i=0; i<2; i++)
		{
			//perform max flow for both graphs
			while(1)
			{
				fill(vis,vis+500,0);
				if(rec(i,SOURCE))
					ans++;
				else
					break;
			}
		}

		deque<tuple<char,int,int> > dq;
		for(int i=0; i<n; i++)
			for(int j=0; j<n; j++)
			{
				int d = getdiag(i,j);
				int ad = getadiag(i,j);

				int ca = !res[0][i+OFF1][j+OFF2];
				int cb = !res[1][d+OFF1][ad+OFF2];
				if(ca+cb!=grid[i][j])
				{
					char c;
					if(ca && cb)
						c = 'o';
					else if(ca)
						c = 'x';
					else if(cb)
						c = '+';
					else
						c = '.';
					dq.push_back(make_tuple(c,i+1,j+1));
					//cout << c << " " << i << " " << j << " " << d << " " << ad << endl;
				}
			}

		printf("Case #%d: %d %d\n",cn,ans,(int)dq.size());
		for(int i=0; i<dq.size(); i++)
			printf("%c %d %d\n",get<0>(dq[i]), get<1>(dq[i]), get<2>(dq[i]));

		// puts("");
		// for(int i=0; i<2; i++)
		// {
		// 	for(int j=0; j<n; j++)
		// 	{
		// 		printf("%d | SOURCE TO %d: %d\n",i,)
		// 	}
		// }
	}

	return 0;
}