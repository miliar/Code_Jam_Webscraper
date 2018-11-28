#include <bits/stdc++.h>
using namespace std;
#define repl(i,a,b) for(int i=(int)(a);i<(int)(b);i++)
#define rep(i,n) repl(i,0,n)
#define mp(a,b) make_pair((a),(b))
#define pb(a) push_back((a))
#define all(x) (x).begin(),(x).end()
#define uniq(x) sort(all(x)),(x).erase(unique(all(x)),end(x))
#define fi first
#define se second
#define dbg(x) cout<<#x" = "<<((x))<<endl
template<class T,class U> ostream& operator<<(ostream& o, const pair<T,U> &p){o<<"("<<p.fi<<","<<p.se<<")";return o;}
template<class T> ostream& operator<<(ostream& o, const vector<T> &v){o<<"[";for(T t:v){o<<t<<",";}o<<"]";return o;}

#define INF 21474836001234567

vector<double> solve(){
  int n,q;
  cin>>n>>q;
  vector<long> e(n),s(n);
  rep(i,n) cin>>e[i]>>s[i];
  vector<vector<long>> d(n,vector<long>(n));

  rep(i,n) rep(j,n) cin>>d[i][j];
  rep(i,n) rep(j,n) if(d[i][j]==-1) d[i][j]=INF;
  rep(i,n) d[i][i]=0;

  rep(k,n)rep(i,n)rep(j,n) d[i][j] = min(d[i][j], d[i][k] + d[k][j]);

  vector<vector<double>> t(n,vector<double>(n,INF));
  rep(i,n) t[i][i] = 0;

  rep(i,n){
    // iの町の馬だけで行けるだけ行く
    rep(j,n) if(i!=j){
      if(d[i][j] <= e[i]) t[i][j] = min(t[i][j], (double)d[i][j]/s[i]);
    }
  }

  rep(k,n)rep(i,n)rep(j,n) t[i][j] = min(t[i][j], t[i][k] + t[k][j]);

  vector<double> ans;
  rep(_,q){
    int u,v;
    cin>>u>>v;
    u--;v--;
    ans.pb(t[u][v]);
  }
  return ans;
}

int main(){
  int t;
  cin>>t;
  rep(i,t){
    vector<double> res = solve();
    printf("Case #%d:", i+1);
    for(auto r : res) printf(" %.7f", r);
    printf("\n");
  }

  return 0;
}
