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
typedef pair<double,double> P;

void Main() {
  ll T,tt=1;
  R T;
  while(T--) {
    ll n,q;
    cin >> n >> q;
    P a[n];
    rep(i,n) cin >> a[i].F >> a[i].S;
    double c[n][n];
    rep(i,n)rep(j,n) {
      R c[i][j];
      if(c[i][j]==-1) c[i][j]=MAXL;
    }
    rep(k,n)rep(i,n)rep(j,n) {
      if(c[i][k]!=MAXL&&c[k][j]!=MAXL) c[i][j]=min(c[i][j],c[i][k]+c[k][j]);
    }
    double d[n][n];
    rep(i,n)rep(j,n)d[i][j]=MAXL;
    rep(s,n) {
      priority_queue<P,vector<P>,greater<P> > que;
      que.push(P(0,s));
      d[s][s]=0;
      while(!que.empty()) {
        P p=que.top();que.pop();
        int x=p.S;
        if(d[s][x]<p.F) continue;
        rep(y,n) {
          if(c[x][y]>a[x].F) continue;
          double t=c[x][y]/a[x].S;
          if(d[s][y]>d[s][x]+t) {
            d[s][y]=d[s][x]+t;
            que.push(P(d[s][y],y));
          }
        }
      }
    }
    cout << "Case #" << tt++ << ":";
    rep(i,q) {
      int s,t;
      cin >> s >> t;
      s--,t--;
      printf(" %.10f",d[s][t]);
    }
    ln;
  }
}

int main(){Main();return 0;}
