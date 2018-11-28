/*
 * test.cpp
 *
 *
 *      Author: Fireworks
 */

#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<queue>
#include<string>
#include<map>
#include<cmath>
#include<bitset>
#include<set>
#include<iomanip>
#include<fstream>
#include<bitset>
#include<cstring>
#include<cstdlib>
#include<complex>
#include<list>
#include<sstream>

using namespace std;

typedef pair<int,int> ii;
typedef pair<int,long long> il;
typedef pair<long long,long long> ll;
typedef pair<ll,int> lli;
typedef pair<long long,int> li;
typedef pair<double,double> dd;
typedef pair<ii,int> iii;
typedef pair<double,int> di;
long long mod = 1000000007LL;
long long base = 37;
long long large = 1000000000000000000LL;


struct Edge{
	int from,to,cap,flow,cost;
};

struct MCMF {
	int n,m,s,t;
	vector<Edge> edges;
	vector<vector<int> > G;
	vector<int> inq;
	vector<int> dis;
	vector<int> p;
	vector<int> a;

	void init(int maxn){
		n=maxn;
		G.assign(n+10,vector<int>(0));
		edges.clear();
		inq.assign(n+10,0);
		dis.assign(n+10,1000000000);
		p.assign(n+10,0);
		a.assign(n+10,0);
	}
	void addEdge(int from,int to,int cap,int cost){
		edges.push_back((Edge){from,to,cap,0,cost});
		edges.push_back((Edge){to,from,0,0,-cost});
		m=(int)edges.size();
		G[from].push_back(m-2);
		G[to].push_back(m-1);
	}
	bool SPFA(int s,int t,int& flow,int& cost){
		dis.assign(n+10,1000000000);
		inq.assign(n+10,0);
		dis[s]=0;
		inq[s]=1;
		p[s]=0;
		a[s]=1000000000;
		//change the following spfa to DJ if needed
		queue<int> q;
		q.push(s);
		while(!q.empty()){
			int u=q.front();
			q.pop();
			inq[u]=0;
			for(int i=0;i<(int)G[u].size();i++){
				Edge& e=edges[G[u][i]];
				if(e.cap>e.flow&&dis[e.to]>dis[u]+e.cost){
					dis[e.to]=dis[u]+e.cost;
					p[e.to]=G[u][i];
					a[e.to]=min(a[u],e.cap-e.flow);
					if(!inq[e.to]){
						q.push(e.to);
						inq[e.to]=1;
					}
				}
			}
		}
		if(dis[t]==1000000000) return false;
		flow+=a[t];
		cost+=dis[t]*a[t];
		int u=t;
		while(u!=s){
			edges[p[u]].flow+=a[t];
			edges[p[u]^1].flow-=a[t];
			u=edges[p[u]].from;
		}
		return true;
	}
	ii mincost(int s,int t){
		int flow=0,cost=0;
		this->s=s;
		this->t=t;
		while(SPFA(s,t,flow,cost));
		return ii(flow,cost);
	}
	void clearflow(){
		inq.assign(n+10,0);
		dis.assign(n+10,1000000000);
		p.assign(n+10,0);
		a.assign(n+10,0);
		for(int i=0;i<(int)edges.size();i++){
			edges[i].flow=0;
		}
	}
};

int main(){


	int totalcase;
	int testcase=0;
	cin>>totalcase;
	ofstream out;
	out.open("result.txt");

	while(totalcase--){
		testcase++;
		out<<"Case #"<<testcase<<": ";
		cout<<testcase<<": "<<endl;

		//GOGOGO

		int n,c,m;
		cin>>n>>c>>m;
		vector<vector<int> > adj(c,vector<int>(0,0));
		for(int i=0;i<m;i++){
			int x,y;
			cin>>x>>y;
			x--;y--;
			adj[y].push_back(x);
		}
		for(int i=0;i<c;i++) {
			sort(adj[i].begin(),adj[i].end());
		}
		MCMF mf;
		mf.init(m+10);
		int st = m+1;
		int en = m+2;
		int base = (int)adj[0].size();
		for(int i=0;i<(int)adj[0].size();i++){
			for(int j=0;j<(int)adj[1].size();j++){
				int u = adj[0][i];
				int v = adj[1][j];
				if(u!=v){
					mf.addEdge(i,base+j,1,0);
				}else{
					if(u==0&&v==0){

					}else{
						mf.addEdge(i,base+j,1,1);
					}
				}
			}
		}
		for(int i=0;i<(int)adj[0].size();i++){
			mf.addEdge(st,i,1,0);
		}
		for(int i=0;i<(int)adj[1].size();i++){
			mf.addEdge(base+i,en,1,0);
		}
		ii re = mf.mincost(st,en);
		out<<m-re.first<<" "<<re.second<<endl;

		//END
	}
	out.close();

	return 0;
}
