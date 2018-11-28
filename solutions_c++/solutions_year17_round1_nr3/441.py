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

ll solve(ll h1,ll d1,ll h2,ll d2,ll b,ll c,ll l,ll r) {
  ll t=0,h=h1;
  rep(i,l) {
    if(h1-(d2-c)<=0) {
      h1=h;
      h1-=d2;
      t++;
    }
    d2-=c;
    h1-=d2;
    if(h1<=0) return MAX;
    t++;
  }
  rep(i,r) {
    if(h1-d2<=0) {
      h1=h;
      h1-=d2;
      t++;
    }
    d1+=b;
    h1-=d2;
    if(h1<=0) return MAX;
    t++;
  }
  while(h2>0) {
    if(h2-d1<=0) return t+1;
    if(h1-d2<=0) {
      h1=h;
      h1-=d2;
      t++;
    }
    h2-=d1;
    t++;
    if(h2<=0) return t;
    h1-=d2;
    if(h1<=0) return MAX;
  }
  return t;
}

void Main() {
  int T,tt=1;
  R T;
  while(T--) {
    ll h1,d1,h2,d2,b,c;
    cin >> h1 >> d1 >> h2 >> d2 >> b >> c;
    ll ans=MAX;
    rep(l,101) {
      rep(r,101) {
        ans=min(ans,solve(h1,d1,h2,d2,b,c,l,r));
      }
    }
    cout << "Case #" << tt++ << ": ";
    if(ans==MAX) cout << "IMPOSSIBLE" << endl;
    else cout << ans << endl;
  }
}

int main(){ios::sync_with_stdio(0);cin.tie(0);Main();return 0;}
