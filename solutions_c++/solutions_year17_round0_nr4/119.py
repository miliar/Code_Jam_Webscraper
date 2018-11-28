/*
 * test.cpp
 *
 *  Created on: Sep 26, 2016
 *      Author: SCE15-0683
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
long long mod = 1000000007LL;
long long base = 37;
long long large = 1000000000000000000LL;

struct Edge {
	int from,to,cap,flow;
};
struct Dinic {
	int n,m,s,t;
	vector<Edge> edges;
	vector<vector<int> > G;
	vector<bool> vis;
	vector<int> dis;
	vector<int> cur;
	void init(int maxn){
		edges.clear();
		G.assign(maxn+10,vector<int>(0));
		vis.assign(maxn+10,false);
		dis.assign(maxn+10,0);
		cur.assign(maxn+10,0);
		n=maxn;
	}
	void addEdge(int from,int to,int cap){
		edges.push_back((Edge){from,to,cap,0});
		edges.push_back((Edge){to,from,0,0});
		m=edges.size();
		G[from].push_back(m-2);
		G[to].push_back(m-1);
	}
	bool BFS() {
		vis.assign(n+10,false);
		queue<int> q;
		q.push(s);
		dis[s]=0;
		vis[s]=true;
		while(!q.empty()){
			int u=q.front();
			q.pop();
			for(int i=0;i<(int)G[u].size();i++){
				Edge& e=edges[G[u][i]];
				if(!vis[e.to]&&e.cap>e.flow){
					vis[e.to]=1;
					dis[e.to]=dis[u]+1;
					q.push(e.to);
				}
			}
		}
		return vis[t];
	}
	int DFS(int x,int a){
		if(x==t||a==0) return a;
		int flow=0,f;
		for(int& i=cur[x];i<(int)G[x].size();i++){
			Edge& e=edges[G[x][i]];
			if(dis[x]+1==dis[e.to]&&(f=DFS(e.to,min(a,e.cap-e.flow)))>0){
				e.flow+=f;
				edges[G[x][i]^1].flow-=f;
				flow+=f;
				a-=f;
				if(a==0) break;
			}
		}
		return flow;
	}
	int maxflow(int s,int t){
		this->s=s;
		this->t=t;
		int flow=0;
		while(BFS()){
			cur.assign(n+10,0);
			flow+=DFS(s,1000000000);
		}
		return flow;
	}
	void clearflow(){
		vis.assign(n+10,false);
		dis.assign(n+10,0);
		cur.assign(n+10,0);
		for(int i=0;i<(int)edges.size();i++){
			edges[i].flow=0;
		}
	}
};


int main(){
	int t;
	cin>>t;
	int test=0;
	ofstream out;
	out.open("result.txt");
	while(t--){
		test++;
		out<<"Case #"<<test<<": ";
		vector<vector<bool> > old1,old2;
		int n,m;
		cin>>n>>m;
		old1.assign(n,vector<bool>(n,false));
		old2=old1;
		for(int i=0;i<m;i++){
			char c;
			int x,y;
			cin>>c>>x>>y;
			x--;y--;
			if(c=='+'||c=='o') old1[x][y]=true;
			if(c=='x'||c=='o') old2[x][y]=true;
		}

		vector<vector<bool> > m1,m2;
		m1=old1;
		m2=old2;
		vector<bool> canr(n,true);
		vector<bool> canc(n,true);
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				if(m2[i][j]) {
					canr[i]=false;
					canc[j]=false;
				}
			}
		}
		for(int i=0;i<n;i++){
			if(canr[i]){
				for(int j=0;j<n;j++){
					if(canc[j]){
						m2[i][j]=true;
						canc[j]=false;
						break;
					}
				}
			}
		}
		canr.assign(2*n,true);
		canc=canr;
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				if(m1[i][j]){
					canr[j-i+n-1]=false;
					canc[i+j]=false;
				}
			}
		}
		int off = 2*n-1;
		int st = 4*n+10;
		int en = st+1;
		Dinic d;
		d.init(4*n+20);
		for(int i=0;i<off;i++){
			if(canr[i]){
				d.addEdge(st,i,1);
			}
			if(canc[i]){
				d.addEdge(i+off,en,1);
			}
		}
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				d.addEdge(j-i+n-1,j+i+off,1);
			}
		}

		d.maxflow(st,en);

		for(int i=0;i<(int)d.edges.size();i++){
			Edge tt = d.edges[i];
			if(tt.from!=st&&tt.to!=en&&tt.flow==1){
				int a = tt.from-(n-1);
				int b = tt.to-off;
				int x = (b-a)/2;
				int y = (b+a)/2;
				m1[x][y]=true;
			}
		}

		int cnt = 0;
		int cnt2 = 0;
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				if(m1[i][j]) cnt++;
				if(m2[i][j]) cnt++;
				bool flag1=false;
				bool flag2=false;
				if(m1[i][j]!=old1[i][j]) flag1 = true;
				if(m2[i][j]!=old2[i][j]) flag2 = true;
				if(flag1||flag2) cnt2++;
			}
		}
		cout<<cnt<<endl;
		out<<cnt<<" "<<cnt2<<endl;
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				bool flag1=false;
				bool flag2=false;
				if(m1[i][j]!=old1[i][j]) flag1 = true;
				if(m2[i][j]!=old2[i][j]) flag2 = true;
				if(flag1||flag2){
					if(m1[i][j]&&m2[i][j]){
						out<<'o'<<" "<<i+1<<" "<<j+1<<endl;
					}else{
						if(flag1){
							out<<'+'<<" "<<i+1<<" "<<j+1<<endl;
						}else{
							out<<'x'<<" "<<i+1<<" "<<j+1<<endl;
						}
					}

				}
			}
		}






	}

	out.close();
	return 0;
}
