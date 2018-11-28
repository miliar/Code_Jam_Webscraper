#include <bits/stdc++.h>

using namespace std;
#define MAX 2111

vector<int> adj[MAX];
int num;
int dfsnum[MAX];
int dfslow[MAX];
int napilha[MAX], pilha[MAX], ps;
int res = 0;
char ans[MAX];
// garfo direcionado ou nao..
void tarjan(int p, int l)
{
	dfsnum[p] = dfslow[p] = num++;
	pilha[ps++] = p;
	napilha[p] = 1;
	
	for (int i = 0; i < adj[p].size(); ++i)
	{
		int v = adj[p][i];
		if (v == l) continue; // atencao, so usar isso aqui se for NAO direcionado as arestas!
		if (dfsnum[v] == 0) // tree edge
			tarjan(v, p);
		else
		{
			if (!napilha[v]) ; // cross edge
			else if (dfsnum[v] < dfsnum[p]) ; // back edge
			else ; // forward edge
		}
		if (napilha[v]) 
			dfslow[p] = min(dfslow[p], dfslow[v]);
	}
	
	if (dfsnum[p] == dfslow[p])
	{
		++res;
		while (1)
		{
			int v = pilha[ps-1];
			--ps;
			napilha[v] = 0;
			// v esta neste componente!
			if (v == p) break;
		}
	}
}

int n,r,o,y,g,b,v,t;
int rr,oo,yy,gg,bb,vv;

void dfs(int curr)
{
	vector< pair<pair<int, char>, int> > v2;
	for (int i = 0; i < adj[curr].size(); ++i)
	{
		int u = adj[curr][i];
		if (dfsnum[u])
			continue;
		if (u < r)
		{
			v2.push_back(make_pair(make_pair(rr, 'R'), u));
		}
		else if (u < r + y)
		{
			v2.push_back(make_pair(make_pair(yy, 'Y'), u));
		}
		else if (u < r + y + b)
		{
			v2.push_back(make_pair(make_pair(bb, 'B'), u));
		}
		else if (u < r + y + b + g)
		{
			v2.push_back(make_pair(make_pair(gg, 'G'), u));
		}
		else if (u < r + y + b + g + v)
		{
			v2.push_back(make_pair(make_pair(vv, 'V'), u));
		}
		else if (u < r + y + b + g + v + o)
		{
			v2.push_back(make_pair(make_pair(oo, 'O'), u));
		}
	}
	if (!v2.size()){
		return;
	}
	sort(v2.rbegin(), v2.rend());
	ans[num++] = v2[0].first.second;
	if (v2[0].first.second == 'R')
		rr--;
	if (v2[0].first.second == 'Y')
		yy--;
	if (v2[0].first.second == 'B')
		bb--;
	if (v2[0].first.second == 'G')
		gg--;
	if (v2[0].first.second == 'V')
		vv--;
	if (v2[0].first.second == 'O')
		oo--;
	dfsnum[v2[0].second] = 1;
	dfs(v2[0].second);
}
int main(void)
{
	ios :: sync_with_stdio(false);
	cin >> t;
	for (int cases = 1; cases <= t; ++cases)
	{
		cin >> n >> r >> o >> y >> g >> b >> v;
		rr = r;
		yy = y;
		bb = b;
		gg = g;
		vv = v;
		oo = o;
		for (int i = 0; i < MAX; ++i)
			adj[i].clear();
		memset(dfsnum, 0, sizeof dfsnum);
		memset(napilha, 0, sizeof napilha);
		memset(dfslow, 0, sizeof dfslow);
		memset(pilha, 0, sizeof pilha);
		memset(ans, 0, sizeof ans);
		ps = 0;
		res = 0;
		num = 1;
		for (int i = 0; i < r; ++i)
		{
			for (int j = 0; j < y; ++j)
			{
				adj[i].push_back(r + j);
				adj[r + j].push_back(i);
			}
			for (int j = 0; j < b; ++j)
			{
				adj[i].push_back(r + y + j);
				adj[r + y + j].push_back(i);
			}
			for (int j = 0; j < g; ++j)
			{
				adj[i].push_back(r + y + b + j);
				adj[r + y + b + j].push_back(i);
			}
		}
		for (int i = 0; i < y; ++i)
		{
			for (int j = 0; j < b; ++j)
			{
				adj[r + i].push_back(r + y + j);
				adj[r + y + j].push_back(r + i);
			}
			for (int j = 0; j < v; ++j)
			{
				adj[r + i].push_back(r + y + b + g + j);
				adj[r + y + b + g + j].push_back(r + i);
			}
		}
		for (int i = 0; i < b; ++i)
		{
			for (int j = 0; j < o; ++j)
			{
				adj[r + y + i].push_back(r + y + b + g + v + j);
				adj[r + y + b + g + v + j].push_back(r + y + i);
			}
		}
		
		for (int i = 0; i < r + y + b + g + v + o; ++i)
		{
			if (dfsnum[i] == 0)
			{
				tarjan(i, i);
			}
		}
		if (res != 1)
		{
			cout << "Case #" << cases << ": " << "IMPOSSIBLE" << "\n";
		}
		else
		{
			cout << "Case #" << cases << ": ";
			if (r > 0)
				rr--, ans[0] = 'R';
			else if (y > 0)
				yy--, ans[0] = 'Y';
			else if (b > 0)
				bb--, ans[0] = 'B';
			else if (g > 0)
				gg--, ans[0] = 'G';
			else if (v > 0)
				vv--, ans[0] = 'V';
			else if (o > 0)
				oo--, ans[0] = 'O';
			memset(dfsnum, 0, sizeof dfsnum);
			dfsnum[0] = 1;
			num = 1;
			dfs(0);
			if (num < n or (n > 1 and ans[0] == ans[n - 1]))
				cout << "IMPOSSIBLE" << "\n";
			else
			{
				for (int i = 0; i < n; ++i)
					cout << ans[i];
				cout << "\n";
			}
		}
	}
}
