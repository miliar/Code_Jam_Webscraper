#define DEB
#include<bits/stdc++.h>
#define REP(i,m) for(int i=0;i<(m);++i)
#define REPN(i,m,in) for(int i=(in);i<(m);++i)
#define ALL(t) (t).begin(),(t).end()
#define CLR(a) memset((a),0,sizeof(a))
#define pb push_back
#define mp make_pair
#define fr first
#define sc second

using namespace std;


#ifdef DEB
#define dump(x)  cerr << #x << " = " << (x) << endl
#define prl cerr<<"called:"<< __LINE__<<endl
#define dumpR(x) cerr<<"\x1b[31m"<<#x<<" = " <<(x)<<"\x1b[39m"<<endl
#define dumpY(x) cerr<<"\x1b[33m"<<#x<<" = " <<(x)<<"\x1b[39m"<<endl
#define dumpG(x) cerr<<"\x1b[32m"<<#x<<" = " <<(x)<<"\x1b[39m"<<endl
template<class T> void debug(T a,T b){ for(;a!=b;++a) cerr<<*a<<' ';cerr<<endl;}
#else
#define dump(x) ;
#define dumpR(x) ;
#define dumpY(x) ;
#define dumpG(x) ;
#define prl ;
template<class T> void debug(T a,T b){ ;}
#endif

template<class T> void chmin(T& a,const T& b) { if(a>b) a=b; }
template<class T> void chmax(T& a,const T& b) { if(a<b) a=b; }

typedef long long int lint;
typedef pair<int,int> pi;

namespace std{
  template<class S,class T>
  ostream &operator <<(ostream& out,const pair<S,T>& a){
    out<<'('<<a.fr<<','<<a.sc<<')';
    return out;
  }
}
const int INF=5e8;

struct MCF{
  static const int MAX_V=10000;
  struct edge{
    int to,cap,cost,rev;
    edge(int st,int sc,int sco,int sr){
      to=st;cap=sc;cost=sco;rev=sr;
    }
  };
  vector<edge> g[MAX_V];
  int pot[MAX_V],dist[MAX_V];
  int prevv[MAX_V],preve[MAX_V];

  int neg_cost_sum,neg_cap_sum;
  int SS,TT;//SET BEFORE ADDING EDGE
  void init(){
    REP(i,MAX_V) g[i].clear();
  }

  void add_edge(int from,int to,int cap,int cost){
    if(cost>=0){
      g[from].pb(edge(to,cap,cost,g[to].size()));
      g[to].pb(edge(from,0,-cost,g[from].size()-1));
    }else{
      neg_cost_sum+=cost*cap;
      neg_cap_sum+=cap;
      add_edge(SS,to,cap,0);
      add_edge(from,TT,cap,0);
      add_edge(to,from,cap,-cost);
    }
  }
  int solve(int s,int t,int f,int V){//without negedge
  //f==-1: flow as much as possible
  //f==-2: flow as long as cost is negative
    int type=f;;
    if(f<0) f=INF;
    int res=0;
    fill(pot,pot+V,0);
    while(f>0){
      priority_queue<pi,vector<pi>,greater<pi> >pq;pq.push(mp(0,s));
      fill(dist,dist+V,INF);
      dist[s]=0;
      while(!pq.empty()){
        pi cur=pq.top();pq.pop();
        if(dist[cur.sc]<cur.fr) continue;
        REP(i,g[cur.sc].size()){
          edge& e=g[cur.sc][i];
          if(e.cap>0 && dist[e.to]>cur.fr+e.cost+pot[cur.sc]-pot[e.to]){
            dist[e.to]=cur.fr+e.cost+pot[cur.sc]-pot[e.to];
            prevv[e.to]=cur.sc;
            preve[e.to]=i;
            pq.push(mp(dist[e.to],e.to));
          }
        }
      }
      if(dist[t]==INF){
        if(type<0) return res;
        return -1;
      }
      if(type==-2 && dist[t]>0) return res;
      for(int v=0;v<V;++v) pot[v]+=dist[v];
      int d=f;
      for(int v=t;v!=s;v=prevv[v]){
        d=min(d,g[prevv[v]][preve[v]].cap);
      }
      f-=d;
      res+=d*pot[t];
      for(int v=t;v!=s;v=prevv[v]){
        edge& e=g[prevv[v]][preve[v]];
        e.cap-=d;
        g[v][e.rev].cap+=d;
      }
    }
    return res;
  }
  int solve2(int S,int T,int f,int V){//with negedge
    int type=f;
    if(f<0) f=INF;
    add_edge(T,S,f,0);
    int res=solve(SS,TT,neg_cap_sum,V);
    assert(~res);
    res+=neg_cost_sum;

    int flowed=0;
    for(auto e:g[T]) if(e.to==S && e.cost==0) flowed+=f-e.cap;
    int add=solve(S,T,type<0?type:f-flowed,V);
    if(add==-1 && type>=0) return -1;
    res+=add;
    return res;
  }
};
MCF g;

int n,m,C;
pi ar[1005];//person, place
int main(){
  int T;cin>>T;
  for(int setn=1;setn<=T;++setn){
    printf("Case #%d: ",setn);
    cin>>n>>C>>m;
    CLR(ar);
    REP(i,m){
      int a,b;scanf("%d%d",&a,&b);--a;--b;
      ar[i]={b,a};
    }
    int lb=0,ub=m+2,cost=-1;
    while(ub-lb>1){
      int md=(lb+ub)>>1;
      g.init();
      int S=md+n+m+C,T=S+1;
      REP(i,md){
        g.add_edge(S,i,INF,0);
        REP(j,C) g.add_edge(i,j+md,1,0);
      }
      REP(j,C) REP(k,m){
        if(ar[k].fr==j) g.add_edge(j+md,k+md+C,1,0);
      }
      REP(k,m){
        REP(l,n){
          if(ar[k].sc>=l) g.add_edge(k+md+C,l+md+C+m,1,(ar[k].sc==l?0:1));
        }
      }
      REP(l,n) g.add_edge(l+md+C+m,T,md,0);
      int fl=g.solve(S,T,m,T+1);
      if(fl==-1) lb=md;
      else{
        ub=md;
        cost=fl;
      }
    }
    printf("%d %d\n",ub,cost);
  }
  return 0;
}



