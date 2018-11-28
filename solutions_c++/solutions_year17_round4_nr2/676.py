#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <functional>
#include <iostream>
#define INF 100000
using namespace std;
typedef long long ll;
typedef pair<int,int> P;

int t;
int n,c,m;
int p[1001],b[1001];
int seat[1001][2];
int cnt[1001][2];

struct edge{
	int to,cap,cost,rev;
	edge(){}
	edge(int tt,int cc,int co,int rr){
		to=tt;
		cap=cc;
		cost=co;
		rev=rr;
	}
};

int V;
vector<edge> G[5000];
int h[5001];
int dist[5000];
int prevv[5000],preve[5000];

void add_edge(int from,int to,int cap,int cost){
	G[from].push_back(edge(to,cap,cost,G[to].size()));
	G[to].push_back(edge(from,0,-cost,G[from].size()-1));
}

int min_cost_flow(int s,int t,int f){
	int res=0;
	fill(h,h+V,0);
	while(f>0){
		priority_queue<P,vector<P>,greater<P> > que;
		fill(dist,dist+V,INF);
		dist[s]=0;
		que.push(P(0,s));
		while(que.size()){
			P p=que.top();
			que.pop();
			int v=p.second;
			if(dist[v]<p.first)continue;
			for(int i=0;i<G[v].size();i++){
				edge &e=G[v][i];
				if(e.cap>0 && dist[e.to]>dist[v]+e.cost+h[v]-h[e.to]){
					dist[e.to]=dist[v]+e.cost+h[v]-h[e.to];
					prevv[e.to]=v;
					preve[e.to]=i;
					que.push(P(dist[e.to],e.to));
				}
			}
		}
		if(dist[t]==INF){
			return -1;
		}
		for(int v=0;v<V;v++){
			h[v]+=dist[v];
		}
		int d=f;
		for(int v=t;v!=s;v=prevv[v]){
			d=min(d,G[prevv[v]][preve[v]].cap);
		}
		f-=d;
		res+=d*h[t];
		for(int v=t;v!=s;v=prevv[v]){
			edge &e=G[prevv[v]][preve[v]];
			e.cap-=d;
			G[v][e.rev].cap+=d;
		}
	}
	return res;
}

int C(int num){
	int s=n+m+c,t=s+1;
	V=n+m+c+2;
	for(int i=0;i<V;i++){
		G[i].clear();
	}
	for(int i=0;i<n;i++){
		add_edge(s,i,num,0);
		for(int j=0;j<m;j++){
			if(i==p[j]){
				add_edge(i,n+j,1,0);
			}
			if(i<p[j]){
				add_edge(i,n+j,1,1);
			}
		}
	}
	for(int i=0;i<m;i++){
		add_edge(n+i,n+m+b[i],1,0);
	}
	for(int i=0;i<c;i++){
		add_edge(n+m+i,t,num,0);
	}
	return min_cost_flow(s,t,m);
}

P solve(){
	int l=0,r=m;
	int res=0;
	while(r-l>1){
		int mid=(l+r)/2;
		int v=C(mid);
		if(v!=-1){
			r=mid;
			res=v;
		}else l=mid;
	}
	return P(r,C(r));
}

int main(void){
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		scanf("%d%d%d",&n,&c,&m);
		for(int j=0;j<m;j++){
			scanf("%d%d",&p[j],&b[j]);
			b[j]--;
			p[j]--;
		}
		P res=solve();
		printf("Case #%d: %d %d\n",i+1,res.first,res.second);
	}
	return 0;
}
