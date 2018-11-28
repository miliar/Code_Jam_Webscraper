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

pair<int,int> solve(){
  int n,c,m;
  cin>>n>>c>>m;
  vector<int> p(m),b(m);
  rep(i,m) cin>>p[i]>>b[i];
  rep(i,m) p[i]--, b[i]--;

  vector<int> pos_cnt(n,0);
  vector<int> man_cnt(c,0);
  vector<vector<int>> mat(c,vector<int>(n,0));
  rep(i,m){
    pos_cnt[p[i]]++;
    man_cnt[b[i]]++;
    mat[b[i]][p[i]]++;
  }
  int y = *max_element(all(man_cnt));
  int acc = 0;
  rep(i,n){
    acc += pos_cnt[i];
    y = max(y, (acc+i)/(i+1));
  }

  int skip = 0;
  int x = 0;
  rep(i,n){
    int req = pos_cnt[i];
    if(req <= y){
      skip += y - req;
    } else {
      int promote = req - y;
      assert(skip >= promote);
      skip -= promote;
      x += promote;
    }
  }
  return mp(y,x);
}

int main(){
  int t;
  cin>>t;
  rep(i,t){
    auto p = solve();
    printf("Case #%d: %d %d\n", i+1, p.fi, p.se);
  }

  return 0;
}
