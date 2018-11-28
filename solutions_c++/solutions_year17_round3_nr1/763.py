#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<double,double> P;

#define fi first
#define se second
#define repl(i,a,b) for(ll i=(ll)(a);i<(ll)(b);i++)
#define rep(i,n) repl(i,0,n)
#define each(itr,v) for(auto itr:v)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define dbg(x) cout<<#x"="<<x<<endl
#define mmax(x,y) (x>y?x:y)
#define mmin(x,y) (x<y?x:y)
#define maxch(x,y) x=mmax(x,y)
#define minch(x,y) x=mmin(x,y)
#define uni(x) x.erase(unique(all(x)),x.end())
#define exist(x,y) (find(all(x),y)!=x.end())
#define bcnt __builtin_popcount

#define INF 1e16

int n,k;
double r[1111],h[1111];
const double pi=acos(-1);

bool sorter(const P& a,const P& b){
  if(a.fi*a.se==b.fi*b.se){
    return a.fi > b.fi;
  }else return a.fi*a.se > b.fi*b.se;
}

int main(){
	cin.sync_with_stdio(false);
  int cases;
  cin>>cases;
  repl(hoge,1,cases+1){
    cin>>n>>k;
    vector<P> ps;
    rep(i,n){
      cin>>r[i]>>h[i];
      ps.push_back(P(r[i],h[i]));
    }
    sort(all(ps),sorter);
    double res=0;
    rep(i,n){
      double nr=ps[i].fi;
      double nh=ps[i].se;
      double s=nr*nr*pi+nr*nh*2*pi;
      int cnt=1;
      rep(j,n){
        if(cnt==k)break;
        if(i==j)continue;
        if(ps[j].fi<=nr){
          double nnr=ps[j].fi;
          nh=ps[j].se;
          s+=nnr*nh*2*pi;
          cnt++;
        }
      }
      if(cnt==k)maxch(res,s);
    }
    printf("Case #%lld: %.10f\n", hoge,res);
  }
	return 0;
}
