#include <bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define rep1(i,n) for(int i=1;i<=(int)(n);i++)
#define all(c) c.begin(),c.end()
#define pb push_back
#define fs first
#define sc second
#define show(x) cout << #x << " = " << x << endl
#define chmin(x,y) x=min(x,y)
#define chmax(x,y) x=max(x,y)
using namespace std;
template<class S,class T> ostream& operator<<(ostream& o,const pair<S,T> &p){return o<<"("<<p.fs<<","<<p.sc<<")";}
template<class T> ostream& operator<<(ostream& o,const vector<T> &vc){o<<"sz = "<<vc.size()<<endl<<"[";for(const T& v:vc) o<<v<<",";o<<"]";return o;}

struct Bipartite_matching{
	int V;
	vector< vector<int> > G;
	vector<int> match;
	vector<bool> used;
	void init(int N){
		V=N;
		G.assign(V,vector<int>());
		match.assign(V,0);
		used.assign(V,false);
	}
	void add_edge(int v,int u){
		G[v].pb(u);
		G[u].pb(v);
	}
	bool dfs(int v){
		used[v]=true;
		rep(i,G[v].size()){
			int u=G[v][i],w=match[u];
			if(w<0 || (!used[w] && dfs(w))){
				match[v]=u;
				match[u]=v;
				return true;
			}
		}
		return false;
	}
	int bipartite(){
		int res=0;
		fill(all(match),-1);
		rep(v,V){
			if(match[v]<0){
				fill(all(used),false);
				if(dfs(v)) res++;
			}
		}
		return res;
	}
};


void solve(){
	int N,M;
	cin>>N>>M;
	Bipartite_matching b1,b2;
	b1.init(2*N);
	b2.init(4*N);
	vector<bool> x(N,0),y(N,0),xy(N*2-1,0),x_y(N*2-1,0);
	int n=0,m=0;
	vector< vector<int> > prev(N,vector<int>(N,0));
	rep(i,M){
		char c;
		int a,b;
		cin>>c>>a>>b;
		a--,b--;
		if(c!='+'){
			prev[a][b]|=1;
			x[a]=1;
			y[b]=1;
			b1.add_edge(a,b+N);
		}
		if(c!='x'){
			prev[a][b]|=2;
			int i = a+b, j = a-b+(N-1);
			xy[i]=1;
			x_y[j]=1;
			b2.add_edge(i,j+2*N-1);
		}
	}
	rep(i,N) if(!x[i]) rep(j,N) if(!y[j]) b1.add_edge(i,j+N);
	rep(i,N) rep(j,N){
		int a = i+j;
		int b = i-j+N-1;
		if(xy[a] || x_y[b]) continue;
		b2.add_edge(a,b+2*N-1);
	}
	vector<vector<int> > ans(N,vector<int>(N,0));

	n+=b1.bipartite();
	rep(i,N) if(b1.match[i]!=-1){
		int j=b1.match[i]-N;
		ans[i][j] |= 1;
	}
	n+=b2.bipartite();
	rep(i,2*N-1) if(b2.match[i]!=-1){
		int j = b2.match[i]-(2*N-1)-(N-1);
		int a = (i+j)/2, b = (i-j)/2;
		ans[a][b] |= 2;
	}
	rep(i,N) rep(j,N){
		if(prev[i][j]!=ans[i][j]) m++;
	}
	cout<<n<<" "<<m<<endl;
	rep(i,N) rep(j,N) if(prev[i][j]!=ans[i][j]){
		if(ans[i][j]==1) printf("x %d %d\n",i+1,j+1);
		if(ans[i][j]==2) printf("+ %d %d\n",i+1,j+1);
		if(ans[i][j]==3) printf("o %d %d\n",i+1,j+1);
	}
}
int main(){
	int T;
	cin>>T;
	rep1(t,T){
		printf("Case #%d: ",t);
		solve();
	}
}
