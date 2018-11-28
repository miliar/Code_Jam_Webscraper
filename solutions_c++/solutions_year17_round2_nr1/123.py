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

#define INF 2147483600

double solve(){
  long d;
  int n;
  cin>>d>>n;
  vector<long> k(n),s(n);
  rep(i,n) cin>>k[i]>>s[i];
  vector<double> t(n);
  rep(i,n){
    t[i] = (double)(d-k[i])/s[i];
  }

  double g = *max_element(all(t));
  return (double)d/g;
}

int main(){
  int t;
  cin>>t;
  rep(i,t){
    printf("Case #%d: %.7f\n", i+1, solve());
  }

  return 0;
}
