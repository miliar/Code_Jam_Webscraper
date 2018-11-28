#include <bits/stdc++.h>
using namespace std;
#define F first
#define S second
#define pi M_PI
#define R cin>>
#define Z class
#define ll long long
#define ln cout<<'\n'
#define in(a) insert(a)
#define pb(a) push_back(a)
#define pd(a) printf("%.10f\n",a)
#define mem(a) memset(a,0,sizeof(a))
#define all(c) (c).begin(),(c).end()
#define iter(c) __typeof((c).begin())
#define rrep(i,n) for(int i=(int)(n)-1;i>=0;i--)
#define REP(i,m,n) for(int i=(int)(m);i<(int)(n);i++)
#define rep(i,n) REP(i,0,n)
#define tr(it,c) for(iter(c) it=(c).begin();it!=(c).end();it++)
template<Z A>void pr(A a){cout<<a;ln;}
template<Z A,Z B>void pr(A a,B b){cout<<a<<' ';pr(b);}
template<Z A,Z B,Z C>void pr(A a,B b,C c){cout<<a<<' ';pr(b,c);}
template<Z A,Z B,Z C,Z D>void pr(A a,B b,C c,D d){cout<<a<<' ';pr(b,c,d);}
template<Z A>void PR(A a,ll n){rep(i,n){if(i)cout<<' ';cout<<a[i];}ln;}
ll check(ll n,ll m,ll x,ll y){return x>=0&&x<n&&y>=0&&y<m;}
const ll MAX=1000000007,MAXL=1LL<<61,dx[4]={-1,0,1,0},dy[4]={0,1,0,-1};
typedef pair<int,int> P;
/*
const int MAX_V=111;

struct edge{
  int to,cap,rev;
};
vector<edge> G[MAX_V];
bool used[MAX_V];

void add_edge(int from,int to, int cap) {
  G[from].push_back((edge){to,cap,G[to].size()});
  G[to].push_back((edge){from,0,G[from].size()-1});
}

int dfs(int v,int t,int f) {
  if(v==t) return f;
  used[v]=true;
  rep(i,G[v].size()) {
    edge &e=G[v][i];
    if(!used[e.to] && e.cap>0) {
      int d=dfs(e.to,t,min(f,e.cap));
      if(d>0) {
        e.cap-=d;
        G[e.to][e.rev].cap+=d;
        return d;
      }
    }
  }
  return 0;
}

int max_flow(int s,int t) {
  int flow=0;
  for(;;) {
    memset(used,0,sizeof(used));
    int f=dfs(s,t,MAX);
    if(!f)return flow;
    flow+=f;
  }
}
*/

void Main() {
  int T,tt=1;
  R T;
  while(T--) {
    int n,m;
    cin >> n >> m;
    ll a[n];
    rep(i,n) R a[i];
    ll c[n][m];
    rep(i,n) {
      rep(j,m) R c[i][j];
      sort(c[i],c[i]+m);
    }
    ll l[n],ans=0;
    mem(l);
    REP(k,1,1000000) {
      bool f=1;
      while(f) {
        rep(i,n) {
          while(l[i]<m&&c[i][l[i]]<(double)a[i]*0.9*k) l[i]++;
          if(l[i]>=m||(double)a[i]*1.1*k<c[i][l[i]]) f=0;
        }
        if(f) {
          ans++;
          rep(i,n) l[i]++;
        }
      }
    }
    cout << "Case #" << tt++ << ": " << ans << endl;
  }
}

int main(){ios::sync_with_stdio(0);cin.tie(0);Main();return 0;}
