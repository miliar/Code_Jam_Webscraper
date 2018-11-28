#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

const ll maxx = 110, maxn = 1e6 + 5, max1 = 40, max2 = 40;

ll n, m, t, p, q, a1[maxx], a2[maxx];
vector<ll> adj[maxx];
bool vis[maxx];
ll match[maxx], mate[maxx];

bool dfs(ll root)
{
	vis[root] = true;
	for(ll x:adj[root])
		if (match[x] == -1 || (!vis[match[x]] && dfs(match[x])))
			return match[x] = root, mate[root] = x, true;
	return false;
}

int main()
{
//	ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	ifstream in;	in.open("tt.txt");	ofstream out;	out.open("ans.out");
	in >> t;
	for(ll uu = 1; uu <= t; uu++)
	{
		out << "Case #" << uu << ": " ;
		in >> n >> m; 
		if (n == 1)
		{
			ll ans = 0;
			in >> p;
			for(ll i = 0; i < m; i++)
			{
				ll x;
				in >> x;
				for(ll u = 1; u < maxn; u++)
				{
					ll g = u * p; if (x >= g - (g / 10) && x <= g + (g / 10) ) 
					{
						ans++;
						break;
					}
				}
			}
			out << ans << endl;
		}
		else
		{
			for(ll i = 0; i < 20; i++) adj[i].clear();
			in >> p >> q;
			for(ll i = 0; i < m; i++) in >> a1[i];
			for(ll i = 0; i < m; i++) in >> a2[i];
			
//			out << p << " " << q << endl;
//			for(ll i = 0; i < m; i++) out << a1[i] << " ";
//			out << endl;
///			for(ll i = 0; i < m; i++) out << a2[i] << " ";
//			out << endl;
			
			for(ll i = 0; i < m; i++)
			{
				for(ll j = 0; j < m; j++)
				{
					for(ll u = 1; u < maxn; u++)
					{
						ll g1 = u * p, g2 = u * q;
						if (a1[i] <= g1 + (g1 / 10ll) && a1[i] >= g1 - (g1 / 10ll) && 
							a2[j] <= g2 + (g2 / 10ll) && a2[j] >= g2 - (g2 / 10ll))
						{
							adj[i].push_back(m + j);
							break;
						}
					}
				}
			}
			//		
			ll ans = 0, n1 = m;
			fill(mate, mate + maxx, 0);
			fill(match, match + maxx, -1);
			while (true)
			{
				fill(vis, vis + max1, false);
				ll x = ans;
				for(ll i = 0; i < n1; i++)
					if (!vis[i] && !mate[i])
						ans += dfs(i);
				if (ans == x) break;
			}
			out << ans << endl;
		}
	}
	return 0;
}
