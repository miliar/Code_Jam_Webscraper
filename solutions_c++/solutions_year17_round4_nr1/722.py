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

void Main() {
  int T,tt=1;
  R T;
  while(T--) {
    ll n,m;
    cin >> n >> m;
    ll c[m];
    mem(c);
    rep(i,n) {
      ll x;
      R x;
      c[x%m]++;
    }
    ll ans=c[0];
    c[0]=0;
    REP(i,1,m/2+m%2) {
      ll x=min(c[i],c[m-i]);
      c[i]-=x;
      c[m-i]-=x;
      ans+=x;
    }
    if(m%2==0) {
      ans+=c[m/2]/2;
      c[m/2]%=2;
    }
    if(m==2) ans+=c[1];
    else if(m==3) ans+=ceil((double)c[1]/3)+ceil((double)c[2]/3);
    else {
    }
    cout << "Case #" << tt++ << ": " << ans << endl;
  }
}

int main(){ios::sync_with_stdio(0);cin.tie(0);Main();return 0;}
