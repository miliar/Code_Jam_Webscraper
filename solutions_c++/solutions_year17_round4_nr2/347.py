#include <bits/stdc++.h>
using namespace std;

using ll=long long;
#define int ll

#define FOR(i,a,b) for(int i=int(a);i<int(b);i++)
#define REP(i,b) FOR(i,0,b)
#define MP make_pair
#define PB push_back
#define ALL(x) x.begin(),x.end()
#define REACH cerr<<"reached line "<<__LINE__<<endl
#define DBG(x) cerr<<"line "<<__LINE__<<" "<<#x<<":"<<x<<endl

using pi=pair<int,int>;
using vi=vector<int>;
using ld=long double;

template<class T,class U>
ostream& operator<<(ostream& os,const pair<T,U>& p){
	os<<"("<<p.first<<","<<p.second<<")";
	return os;
}

template<class T>
ostream& operator <<(ostream& os,const vector<T>& v){
	os<<"[";
	REP(i,(int)v.size()){
		if(i)os<<",";
		os<<v[i];
	}
	os<<"]";
	return os;
}

int read(){
	int i;
	scanf("%lld",&i);
	return i;
}

void printSpace(){
	printf(" ");
}

void printEoln(){
	printf("\n");
}

void print(int x,int suc=1){
	printf("%lld",x);
	if(suc==1)
		printEoln();
	if(suc==2)
		printSpace();
}

string readString(){
	static char buf[3341919];
	scanf("%s",buf);
	return string(buf);
}

char* readCharArray(){
	static char buf[3341919];
	static int bufUsed=0;
	char* ret=buf+bufUsed;
	scanf("%s",ret);
	bufUsed+=strlen(ret)+1;
	return ret;
}

template<class T,class U>
void chmax(T& a,U b){
	if(a<b)
		a=b;
}

template<class T,class U>
void chmin(T& a,U b){
	if(a>b)
		a=b;
}

template<class T>
T Sq(const T& t){
	return t*t;
}

namespace MaxFlow{
	using CapType=int;
	const CapType inf=1145141919;
	struct Edge{
		int to,rev;
		CapType cap;
	};
	vector<vector<Edge>> g;
	vi itr,level;
	void Init(int n){
		g.assign(n,vector<Edge>());
		itr.assign(n,0);
		level.assign(n,0);
	}
	void AddEdge(int from,int to,CapType cap){
		g[from].PB({to,(int)g[to].size(),cap});
		g[to].PB({from,(int)g[from].size()-1,0});
	}
	void bfs(int s){
		fill(level.begin(),level.end(),-1);
		level[s]=0;
		queue<int> q;
		q.push(s);
		while(!q.empty()){
			int v=q.front();q.pop();
			for(auto e:g[v])if(e.cap>0&&level[e.to]==-1){
				level[e.to]=level[v]+1;
				q.push(e.to);
			}
		}
	}
	CapType dfs(int v,int t,CapType f){
		if(v==t)
			return f;
		for(int&i=itr[v];i<(int)g[v].size();i++){
			Edge& e=g[v][i];
			if(e.cap>0&&level[e.to]==level[v]+1){
				CapType d=dfs(e.to,t,min(f,e.cap));
				if(d>0){
					e.cap-=d;
					g[e.to][e.rev].cap+=d;
					return d;
				}
			}
		}
		return 0;
	}
	CapType Calc(int s,int t){
		CapType flow=0;
		while(1){
			bfs(s);
			if(level[t]==-1)
				return flow;
			fill(itr.begin(),itr.end(),0);
			CapType f;
			while((f=dfs(s,t,inf))>0)
				flow+=f;
		}
	}
}
namespace MinCostFlow{
	const int inf=1145141919;
	struct Edge{
		int to,rev,cost,cap;
	};
	vector<vector<Edge>> g;
	int n;
	vi h,dist,prevv,preve;
	void Init(int _n){
		n=_n;
		g.assign(n,vector<Edge>());
		h.assign(n,0);
		dist.assign(n,0);
		prevv.assign(n,0);
		preve.assign(n,0);
	}
	void AddEdge(int from,int to,int cost,int cap){
		g[from].PB({to,(int)g[to].size(),cost,cap});
		g[to].PB({from,(int)g[from].size()-1,-cost,0});
	}
	pi go(int s,int t,int f){
		priority_queue<pi,vector<pi>,greater<pi>> q;
		fill(dist.begin(),dist.end(),inf);
		dist[s]=0;
		q.push(MP(0,s));
		while(!q.empty()){
			int v=q.top().second,d=q.top().first;q.pop();
			if(dist[v]<d)
				continue;
			REP(i,(int)g[v].size()){
				Edge e=g[v][i];
				if(e.cap>0){
					int w=dist[v]+e.cost+h[v]-h[e.to];
					if(w<dist[e.to]){
						dist[e.to]=w;
						q.push(MP(w,e.to));
						prevv[e.to]=v;
						preve[e.to]=i;
					}
				}
			}
		}
		if(dist[t]==inf)
			return MP(0,0);
		REP(i,n)
			h[i]+=dist[i];
		int d=f;
		for(int v=t;v!=s;v=prevv[v])
			chmin(d,g[prevv[v]][preve[v]].cap);
		for(int v=t;v!=s;v=prevv[v]){
			Edge& e=g[prevv[v]][preve[v]];
			e.cap-=d;
			g[e.to][e.rev].cap+=d;
		}
		return MP(d,d*h[t]);
	}
	int Calc(int s,int t,int f){
		int res=0;
		while(f>0){
			pi w=go(s,t,f);
			if(w.first==0)
				return inf;
			f-=w.first;
			res+=w.second;
		}
		return res;
	}
}

const int inf=LLONG_MAX/3;

void Solve(){
	int n=read(),c=read(),m=read();
	MaxFlow::Init(1+c+n+1);
	REP(i,c)MaxFlow::AddEdge(0,1+i,0);
	REP(i,n)MaxFlow::AddEdge(1+c+i,1+c+n,0);
	REP(i,n-1)MaxFlow::AddEdge(1+c+i+1,1+c+i,MaxFlow::inf);
	vector<pi> es;
	REP(i,m){
		int p=read()-1,b=read()-1;
		es.PB(pi(b,p));
		MaxFlow::AddEdge(1+b,1+c+p,1);
	}
	int flow=0,y=0;
	while(flow<m){
		y++;
		for(auto&e:MaxFlow::g[0])e.cap++;
		REP(i,n)MaxFlow::g[1+c+i][0].cap++;
		flow+=MaxFlow::Calc(0,1+c+n);
	}
	
	MinCostFlow::Init(1+c+n+n+1);
	REP(i,c)MinCostFlow::AddEdge(0,1+i,0,y);
	REP(i,n)MinCostFlow::AddEdge(1+c+i,1+c+n+i,0,MinCostFlow::inf);
	REP(i,n-1)MinCostFlow::AddEdge(1+c+i+1,1+c+i,0,MinCostFlow::inf);
	REP(i,n)MinCostFlow::AddEdge(1+c+n+i,1+c+n+n,0,y);
	for(auto e:es){
		MinCostFlow::AddEdge(1+e.first,1+c+e.second,1,1);
		MinCostFlow::AddEdge(1+e.first,1+c+n+e.second,0,1);
	}
	int z=MinCostFlow::Calc(0,1+c+n+n,m);
	cout<<y<<" "<<z<<endl;
}

signed main(){
	int t=read();
	REP(i,t){
		printf("Case #%lld: ",i+1);
		Solve();
	}
}
