#include <string>
#include <vector>
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<stack>
#include<queue>
#include<cmath>
#include<algorithm>
#include<functional>
#include<list>
#include<deque>
#include<bitset>
#include<set>
#include<map>
#include<unordered_map>
#include<unordered_set>
#include<cstring>
#include<sstream>
#include<complex>
#include<iomanip>
#include<numeric>
#include<cassert>
#define X first
#define Y second
#define pb push_back
#define rep(X,Y) for (int (X) = 0;(X) < (Y);++(X))
#define reps(X,S,Y) for (int (X) = S;(X) < (Y);++(X))
#define rrep(X,Y) for (int (X) = (Y)-1;(X) >=0;--(X))
#define rreps(X,S,Y) for (int (X) = (Y)-1;(X) >= (S);--(X))
#define repe(X,Y) for ((X) = 0;(X) < (Y);++(X))
#define peat(X,Y) for (;(X) < (Y);++(X))
#define all(X) (X).begin(),(X).end()
#define rall(X) (X).rbegin(),(X).rend()
#define eb emplace_back
#define UNIQUE(X) (X).erase(unique(all(X)),(X).end())
#define Endl endl

using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
template<class T> using vv=vector<vector<T>>;
template<class T> ostream& operator<<(ostream &os, const vector<T> &t) {
os<<"{"; rep(i,t.size()) {os<<t[i]<<",";} os<<"}"<<endl; return os;}
template<class S, class T> ostream& operator<<(ostream &os, const pair<S,T> &t) { return os<<"("<<t.first<<","<<t.second<<")";}
template<class T> inline bool MX(T &l,const T &r){return l<r?l=r,1:0;}
template<class T> inline bool MN(T &l,const T &r){return l>r?l=r,1:0;}
#define out(args...){vector<string> a_r_g_s=s_p_l_i_t(#args, ','); e_r_r(a_r_g_s.begin(), args); }
vector<string> s_p_l_i_t(const string &s, char c){vector<string> v;int d=0,f=0;string t;for(char c:s){if(!d&&c==',')v.pb(t),t="";else t+=c;if(c=='\"'||c=='\'')f^=1;if(!f&&c=='(')++d;if(!f&&c==')')--d;}v.pb(t);return move(v);}
void e_r_r(vector<string>::iterator it) {}
template<typename T, typename... Args> void e_r_r(vector<string>::iterator it, T a, Args... args){ if(*it==" 1"||*it=="1") cerr<<endl; else cerr << it -> substr((*it)[0] == ' ', it -> length()) << " = " << a << ", "; e_r_r(++it, args...);}
const ll MOD=1e9+7;

vector<string> mp;
int dx[]={1,0,-1,0};
int dy[]={0,1,0,-1,0};
vector<pair<pii,int>> from[55][55];
bool dfs(int x,int y,int d,int ox=-1,int oy=-1,int od=-1){
  if(mp[y][x]=='#') return 0;
  if(mp[y][x]=='|' || mp[y][x]=='-') return 1;
  if(ox>=0) from[y][x].eb(pii(ox,oy),od);
  if(mp[y][x]=='/') d=3-d;
  if(mp[y][x]=='\\') d^=1;
  return dfs(x+dx[d],y+dy[d],d,ox,oy,od);
}
// SCC
typedef vv<int> Graph;
struct Scc{
  stack<int> S;
  vector<int> inS,low,num;
  int time;
public:
  Graph dag;
  vector<int> inv;
  vv<int> scc;
  void visit(const Graph &g, int v){
    low[v] = num[v] = ++time;
    S.push(v); inS[v]=1;
    for(const int  &w:g[v]) {
      if(!num[w]){
	visit(g,w);
	low[v]=min(low[v],low[w]);
      }else if(inS[w])
	low[v]=min(low[v],num[w]);
    }
    if(low[v]==num[v]){
      scc.push_back(vector<int>());
      while(1){
	int w = S.top(); S.pop(); inS[w]=0;
	scc.back().push_back(w);
	if (v==w) break;
      }
    }
  }
  Scc(const Graph &g) {
    const int n = g.size();
    num.resize(n); low.resize(n); inS.resize(n);
    rep(u,n) if(!num[u])
      visit(g,u);
    reverse(all(scc));
    
    inv.resize(n); dag.resize(n);
    rep(i,scc.size()) rep(j,scc[i].size())
      inv[scc[i][j]]=i;
    rep(i,scc.size()) rep(j,scc[i].size())
      for(auto e:g[scc[i][j]])
	if(inv[e] != i)
	  dag[i].pb(inv[e]);
  }
};

int main(){
  ios_base::sync_with_stdio(false);
  cout<<fixed<<setprecision(0);
  int T;
  cin>>T;
  rep(kase,T){
    int n,m;
    cin>>n>>m;
    mp.clear();
    mp.resize(n+2,string(m+2,'#'));
    rep(i,55)rep(j,55) from[i][j].clear();
    rep(i,n){
      string s;
      cin>>s;
      mp[i+1]="#"+s+"#";
    }
    //for(auto s:mp)cout<<s<<endl;
    int ng[55][55]={};
    int id[55][55]={};
    n+=2; m+=2;
    vector<pii> ls;
    rep(i,n)rep(j,m)if(mp[i][j]=='|' || mp[i][j]=='-'){
      id[i][j]=ls.size();
      ls.eb(j,i);
      rep(d,4) if(dfs(j+dx[d],i+dy[d],d)) ng[i][j]|=(1<<(d%2));
      rep(d,4)if(!(ng[i][j]>>(d%2)&1)) dfs(j+dx[d],i+dy[d],d,j,i,d%2);
    }
    int t=ls.size();
    vv<int> g(2*t);
    //rep(i,n)rep(j,m)out(i,j,from[i][j],1);
    int f=0;
    rep(i,n)rep(j,m){
      if(mp[i][j]=='.'){
	assert(from[i][j].size()<=2);
	if(from[i][j].size()==1){
	  pii p=from[i][j][0].X;
	  int a=from[i][j][0].Y;
	  int k=id[p.Y][p.X];
	  g[a*t+k].pb((1-a)*t+k);
	}else if(from[i][j].size()==2){
	  rep(k,2){
	    pii p=from[i][j][k].X;
	    int a=from[i][j][k].Y;
	    int x=id[p.Y][p.X];
	    pii q=from[i][j][1-k].X;
	    int b=from[i][j][1-k].Y;
	    int y=id[q.Y][q.X];
	    //out(i,j,p,a,x,q,b,y,1);
	    g[a*t+x].pb((1-b)*t+y);
	  }
	}else f=1;
      }else if(mp[i][j]=='|' || mp[i][j]=='-'){
	int x=id[i][j];
	//out(i,j,x,ng[i][j],1);
	if(ng[i][j]&1) g[x+t].pb(x);
	if(ng[i][j]&2) g[x].pb(x+t);
      }
    }
    //    rep(i,n)rep(j,m)if(from[i][j].size())out(i,j,from[i][j],1);
    //out(g,1);
    Scc h(g);
    rep(i,h.dag.size())for(int x:h.dag[i]) assert(i<x);
    vector<int> tf(t,-1);
    rep(i,t){
      if(h.inv[i]==h.inv[t+i]) f=1;
      tf[i]=(h.inv[t+i]<h.inv[i]);
    }
    //if(f){for(auto s:mp)cout<<s<<endl;} continue;
    cout<<"Case #"<<kase+1<<": ";
    if(f){
      cout<<"IMPOSSIBLE"<<endl;
    }else{
      cout<<"POSSIBLE"<<endl;
      reps(i,1,n-1){
	reps(j,1,m-1){
	  if(mp[i][j]=='|' || mp[i][j]=='-'){
	    cout<<(tf[id[i][j]]?'|':'-');
	  }else{
	    cout<<mp[i][j];
	  }
	}
	cout<<endl;
      }
    }
  }
  return 0;
}
