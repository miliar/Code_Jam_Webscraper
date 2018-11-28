#include <bits/stdc++.h>

using namespace std;

const int maxx = 1002;

int n, m, tc, a[maxx], c, b[maxx], ta, tb;
vector<int> adj[maxx + maxx];
bool vis[maxx];
int mate[maxx], match[maxx];

bool dfs(int root)
{
	vis[root] = true;
	for(int x:adj[root])
		if (match[x] == -1 || (!vis[match[x]] && dfs(match[x])))
			return match[x] = root, mate[root] = x, true;
	return false;
}

int main()
{
	ifstream in;	in.open("tt.txt");	ofstream out;	out.open("ans.out"); 
	in >> tc;
	for(int u = 1; u <= tc; u++)
	{
		out << "Case #" << u << ": ";
		in >> n >> c >> m; ta = 0; tb = 0;
		for(int i = 0; i < m; i++)
		{
			int x, y;
			in >> x >> y;
			if (y == 1) a[ta++] = x;
			else		b[tb++] = x;
		}
		for(int i = 0; i < maxx * 2; i++)
			adj[i].clear();
		fill(vis, vis + maxx, false); 
		fill(match, match + maxx, 0);
		fill(mate, mate + maxx, 0);
		for(int i = 0; i < ta; i++)
		{
			for(int j = 0; j < tb; j++)
			{
				if (a[i] != b[j]) adj[i].push_back(ta + j), adj[ta + j].push_back(i);
			}
		}
		int ans = 0;
		fill(match, match + maxx, -1);
		while (true)
		{
			fill(vis, vis + maxx, false);
			int x = ans;
			for(int i = 0; i < ta; i++)
				if (!vis[i] && !mate[i])
					ans += dfs(i);
			if (ans == x) break;
		}
//	cout << ans << endl;
		int g = -1;
		for(int i = 0; i < ta + tb; i++) 
		{
			if (match[i] == -1 && mate[i] == 0) 
			{
				if (i < ta) g = a[i];
				else		g = b[i - ta];
				break;
			}
		}
		if (ans == min(ta, tb)) out << max(ta, tb) << " " << 0 << endl;
		else
		{
			if (g != 1)
				out << max(ta, tb) << " " << min(ta, tb) - ans << endl;
			else
			{
				out << ta + tb - ans << " " << 0 << endl;
			}
		}
	}
	return 0;
}
