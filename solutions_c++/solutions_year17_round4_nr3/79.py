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

const int MAX_V=11000;
vector<int> G[MAX_V],rG[MAX_V],vs;
bool used[MAX_V];
int cmp[MAX_V];
void add_edgeG(int from,int to){
	G[from].push_back(to);
	rG[to].push_back(from);
}
void dfs(int v){
	used[v]=true;
	rep(i,G[v].size()){
		if(!used[G[v][i]]) dfs(G[v][i]);
	}
	vs.push_back(v);
}
void rdfs(int v,int k){
	used[v]=true;
	cmp[v]=k;
	rep(i,rG[v].size()){
		if(!used[rG[v][i]]) rdfs(rG[v][i],k);
	}
}
vector<int> cG[MAX_V];
int scc(int N){
	memset(used,0,sizeof(used));
	vs.clear();
	rep(v,N) if(!used[v]) dfs(v);
	memset(used,0,sizeof(used));
	int k=0;
	for(int i=vs.size()-1;i>=0;i--){
		if(!used[vs[i]]) rdfs(vs[i],k++);
	}
	return k;
}
void init(){
	rep(i,MAX_V) G[i].clear(),rG[i].clear(),used[i] = 0, cmp[i] = 0;
	vs.clear();
}

void add_edge(int x,int y){
	add_edgeG(x,y);
	add_edgeG(y^1,x^1);
}


int H,W;
string s[50];
bool vis[50][50][2];
int id(int x,int y,int t,int nt=0){return ((x*W+y)*2+t)*2+nt;}
int dx[4]={1,0,-1,0},dy[4]={0,1,0,-1};


bool is(int x,int y){
	return 0<=x&&x<H&&0<=y&&y<W&&s[x][y]!='#';
}

void solve(){
	init();
	cin>>H>>W;
	rep(i,H) cin>>s[i];

	rep(i,H) rep(j,W) rep(k,2) vis[i][j][k]=0;

	rep(i,H) rep(j,W) if(s[i][j]=='|') s[i][j]='-';

	int F = H*W*4,T = H*W*4+1;
	int V = H*W*4+2;

	rep(i,H) rep(j,W) if(s[i][j]=='-'){
		rep(t,2){//t=0 | t=1 -
			rep(k,2){
				vector<int> vs;
				int di = t+k*2;
				int x = i, y = j;
				while(true){
					int nx = x+dx[di], ny = y+dy[di];
					if(!is(nx,ny)){
						break;
					}
					if(s[nx][ny]=='.'){
						vis[nx][ny][di%2] = 1;
						vs.pb(id(nx,ny,di%2));
					}else if(s[nx][ny]=='-'){
//						show(i);
//						show(j);
						vs.pb(F);
						break;
					}else if(s[nx][ny]=='/'){
						if(di==0) di=3;
						else if(di==1) di=2;
						else if(di==2) di=1;
						else if(di==3) di=0;
					}else if(s[nx][ny]=='\\'){
						if(di==0) di=1;
						else if(di==1) di=0;
						else if(di==2) di=3;
						else if(di==3) di=2;
					}
					x = nx, y = ny;
				}
				int v0 = id(i,j,t);
//				show(v0);
//				show(vs);
				for(int v:vs){
					add_edge(v0,v);
					add_edge(v,v0);
				}
			}
		}
	}
	rep(i,H) rep(j,W) if(s[i][j]=='.' || s[i][j]=='-'){	// | or -
		add_edge(id(i,j,0,1),id(i,j,1));
		add_edge(id(i,j,1,1),id(i,j,0));
	}
	rep(i,H) rep(j,W) if(s[i][j]=='-'){	//not +
		add_edge(id(i,j,0),id(i,j,1,1));
		add_edge(id(i,j,1),id(i,j,0,1));
	}
	rep(i,H) rep(j,W) if(s[i][j]=='.'){
		rep(k,2) if(!vis[i][j][k]){	//cannot reach
			add_edge(id(i,j,k),F);
		}
	}
	rep(i,H*W*4) add_edge(F,i),add_edge(i,T);
	add_edge(F,T);
	scc(V);
	rep(i,H*W*2) if(cmp[i*2] == cmp[i*2+1]){
		puts("IMPOSSIBLE");
		return;
	}
	if(cmp[T]==cmp[F]){
		puts("IMPOSSIBLE");
		return;
	}
	puts("POSSIBLE");
	rep(i,H) rep(j,W) if(s[i][j]=='-'){
		int y = id(i,j,0);
		int n = id(i,j,0,1);
		if(cmp[y]>cmp[n]) s[i][j]='|';
	}
	rep(i,H) cout<<s[i]<<endl;
}
int main(){
	int T;
	cin>>T;
	rep1(t,T){
		printf("Case #%d: ",t);
		solve();
	}
}
