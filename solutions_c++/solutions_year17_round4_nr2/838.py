#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
void ioinit()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
}

const int N=1007;
int linker[N],c1[N],c2[N];
bool used[N];
vector<int> adj[N];
bool dfs(int u)
{
	for(auto v:adj[u])
	{
		if(!used[v])
		{
			used[v]=1;
			if(linker[v]==-1||dfs(linker[v]))
			{
				linker[v]=u;
				return 1;
			}
		}
	}
	return 0;
}
int hungary()
{
	int res=0;
	memset(linker,-1,sizeof(linker));
	for(int u=0;u<N;u++)
	{
		if(adj[u].size()==0) continue;
		memset(used,0,sizeof(used));
		if(dfs(u)) res++;
	}
	return res;
}

bool vis1[1007],vis2[1007];
int main()
{
	ioinit();
	int T,kase=1;
	cin>>T;
	while(T--)
	{
		vector<int> v1,v2;
		memset(c1,0,sizeof(c1));
		memset(c2,0,sizeof(c2));
		int n,m,c;
		cin>>n>>c>>m;
		//clog << n << " " << c << " " << m << endl;
		for(int i=0;i<N;i++) adj[i].clear();
		for(int i=0;i<m;i++)
		{
			int p,b;
			cin>>p>>b;
			if(b==1) v1.push_back(p),c1[p]++;
			else v2.push_back(p),c2[p]++;
		}
		for(int u=0;u<v1.size();u++)
			for(int v=0;v<v2.size();v++)
				if(v1[u]!=v2[v]) adj[u].push_back(v);
		int ans1=hungary();
		//clog << v1.size() << " " << v2.size() << endl;
		for(int v=0;v<v2.size();v++)
		{
			int u=linker[v];
			//if(n==2&&c==2) clog << u << " " << v << endl;
			if(u!=-1)
			{
				c1[v1[u]]--;
				c2[v2[v]]--;
			}
		}
		//clog  << "Gg" ;
		int ans2=0;
		if(ans1==v1.size()||ans1==v2.size())
		{
			ans1+=max(v1.size()-ans1,v2.size()-ans1);
		}
		else if(c1[1]&&c2[1]) ans1+=c1[1]+c2[1];
		else
		{
			for(int i=1;i<=n;i++)
			{
				if(c1[i]||c2[i])
				{
					ans1+=min(c1[i],c2[i]);
					ans2+=min(c1[i],c2[i]);
					ans1+=max(c1[i]-min(c1[i],c2[i]),c2[i]-min(c1[i],c2[i]));
					break;
				}
			}
		}
		printf("Case #%d: %d %d\n",kase++,ans1,ans2);
	}
	return 0;
}
