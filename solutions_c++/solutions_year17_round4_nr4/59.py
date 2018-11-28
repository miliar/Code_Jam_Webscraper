#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cassert>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <functional>
#include <iostream>
#include <map>
#include <set>
#include <cassert>
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
typedef pair<int,P> P1;
typedef pair<P,P> P2;
#define pu push
#define pb push_back
#define mp make_pair
#define eps 1e-7
#define INF 1000000000
#define fi first
#define sc second
#define rep(i,x) for(int i=0;i<x;i++)
#define SORT(x) sort(x.begin(),x.end())
#define ERASE(x) x.erase(unique(x.begin(),x.end()),x.end())
#define POSL(x,v) (lower_bound(x.begin(),x.end(),v)-x.begin())
#define POSU(x,v) (upper_bound(x.begin(),x.end(),v)-x.begin())
int t,n,m,L;
string f[105];
int v[35][35];
/*
struct edge
{
	int to,cap,rev;
};
vector<edge>G[105];
bool used[105];

void add_edge(int from,int to,int cap)
{
	G[from].push_back((edge){to,cap,G[to].size()});
	G[to].push_back((edge){from,0,G[from].size()-1});
}
int dfs(int v,int t,int f)
{ 
	if(v==t) return f;
	used[v]=true;
	for(int i=0;i<G[v].size();i++)
	{
		edge &e=G[v][i];
		if(!used[e.to] && e.cap>0)
		{ 
			int d=dfs(e.to,t,min(f,e.cap));
			if(d>0) 
			{ 
				e.cap-=d;
				G[e.to][e.rev].cap+=d;
				return d;
			}
		}
	}
	return 0;
}
int max_flow(int s,int t)
{ 
	int flow=0;
	while(1)
	{ 
		memset(used,0,sizeof(used));
		int f=dfs(s,t,INF);
		if(!f) return flow;
		flow+=f;
	}
}
*/
int dp[1025][1025];
P nxt[1025][1025];
bool vis[1025][1025];
vector<P>sol,tar;
int rec(int m1,int m2){
	if(vis[m1][m2]) return dp[m1][m2];
	vis[m1][m2] = 1;
	for(int i=0;i<sol.size();i++){
		if(((m1>>i)&1)) continue;
		bool ok[11]={};
		bool used[35][35]={};
		int dist[35][35];
		for(int x=0;x<n;x++) for(int y=0;y<m;y++) dist[x][y] = INF;
		queue<P>que;
		que.push(sol[i]);
		dist[sol[i].fi][sol[i].sc] = 0;
		while(!que.empty()){
			P p = que.front(); que.pop();
			if(used[p.fi][p.sc] || dist[p.fi][p.sc] > L) continue;
			used[p.fi][p.sc] = 1;
			int dx[4]={0,1,0,-1};
			int dy[4]={1,0,-1,0};
			bool C =  0;
			for(int k=0;k<4;k++){
				int nx = p.fi+dx[k],ny = p.sc+dy[k];
				while(0<=nx&&nx<n&&0<=ny&&ny<m&&f[nx][ny] != '#'){
					if(f[nx][ny] == 'T' && !((m2>>v[nx][ny])&1)){
						ok[v[nx][ny]] = 1;
						C = 1;
					}
					nx += dx[k]; ny += dy[k];
				}
			}
			if(C) continue;
			for(int k=0;k<4;k++){
				int nx = p.fi+dx[k],ny = p.sc+dy[k];
				if(0<=nx&&nx<n&&0<=ny&&ny<m&&f[nx][ny] != '#' && !used[nx][ny]){
					dist[nx][ny] = min(dist[nx][ny],dist[p.fi][p.sc]+1);
					que.push(mp(nx,ny));
				}
			}
		}
		for(int j=0;j<tar.size();j++){
			if(ok[j]){
				 int x = rec(m1+(1<<i),m2+(1<<j));
				 if(dp[m1][m2] < 1+x){
				 	dp[m1][m2] = 1+x;
				 	nxt[m1][m2] = mp(m1+(1<<i),m2+(1<<j));
				 }
			}
		}
	}
	return dp[m1][m2];
}
int main(){
	cin >> t;
	for(int q=1;q<=t;q++){
	sol.clear(); tar.clear();
	memset(vis,0,sizeof(vis));memset(dp,0,sizeof(dp));
		memset(v,-1,sizeof(v));
		cin >> m >> n >> L;
		for(int i=0;i<n;i++) cin >> f[i];
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				if(f[i][j] == 'S') sol.pb(mp(i,j));
				if(f[i][j] == 'T'){
					tar.pb(mp(i,j));
					v[i][j] = tar.size()-1;
				}
			}
		}
		printf("Case #%d: %d\n",q,rec(0,0));
		int x = 0,y = 0;
		while(dp[x][y]){
			int nx = nxt[x][y].fi,ny = nxt[x][y].sc;
			nx -= x; ny-= y;
			for(int i=0;i<sol.size();i++){
				if( (1<<i) == nx) printf("%d ",i+1);
			}
			for(int i=0;i<tar.size();i++){
				if( (1<<i) == ny) printf("%d\n",i+1);
			}
			x+=nx;y+=ny;
		}
	}
}