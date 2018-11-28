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

const lint INF=1e18;

lint g[105][105];
int n,q;
lint dist[105],speed[105];
int main(){
  int T;cin>>T;
  for(int setn=1;setn<=T;++setn){
    printf("Case #%d:",setn);
    cin>>n>>q;
    REP(i,n){
      cin>>dist[i]>>speed[i];
    }
    REP(i,n) REP(j,n){
      cin>>g[i][j];
      if(g[i][j]==-1) g[i][j]=INF;
    }
    REP(i,n) g[i][i]=0;
    REP(i,n) REP(j,n) REP(k,n) chmin(g[j][k],g[j][i]+g[i][k]);

    REP(hoge,q){
      int u,v;scanf("%d%d",&u,&v);
      --u;--v;
      
      double cost[105];
      bool done[105]={};
      REP(i,n) cost[i]=INF;
      cost[u]=0;
      while(!done[v]){
        int mx=-1;
        REP(i,n) if(!done[i] && (mx==-1 || cost[i]<cost[mx])) mx=i;
        done[mx]=1;
        REP(i,n) if(!done[i] && g[mx][i]<=dist[mx]) chmin(cost[i],cost[mx]+g[mx][i]/(double)speed[mx]);
      }
      printf(" %.10f",cost[v]);
    }
    puts("");
  }
  return 0;
}



