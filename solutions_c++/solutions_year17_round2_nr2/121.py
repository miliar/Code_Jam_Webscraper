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

#define FAIL  "IMPOSSIBLE"

string sol(int b, int r, int y){
  int mx = max(b,max(r,y));
  int sum = b+r+y;
  if(mx*2 > sum) return FAIL;

  vector<pair<int,char>> vec;
  vec.pb(mp(b,'B'));
  vec.pb(mp(r,'R'));
  vec.pb(mp(y,'Y'));
  sort(all(vec));

  string ret;
  rep(i,vec[1].fi){
    ret.pb(vec[2].se);
    ret.pb(vec[1].se);
  }
  rep(i,vec[2].fi-vec[1].fi) ret.pb(vec[2].se);

  reverse(all(ret));

  string ans;
  rep(i,vec[0].fi){
    ans.pb(vec[0].se);
    ans.pb(ret[i]);
  }
  repl(i,vec[0].fi, ret.size()) ans.pb(ret[i]);

  assert(ans.size() == b+r+y);
  rep(i,ans.size()) assert(ans[i] != ans[(i+1)%(ans.size())]);

  return ans;
}

string solve(){
  int n,r,o,y,g,b,v;
  cin>>n>>r>>o>>y>>g>>b>>v;

  bool bo = b==0 && o==0;
  bool rg = r==0 && g==0;
  bool yv = y==0 && v==0;
  if(bo && rg){
    if(y!=v) return FAIL;
    string ret;
    rep(i,n/2) ret += "YV";
    return ret;
  }
  if(bo && yv){
    if(r!=g) return FAIL;
    string ret;
    rep(i,n/2) ret += "RG";
    return ret;
  }
  if(yv && rg){
    if(b!=o) return FAIL;
    string ret;
    rep(i,n/2) ret += "BO";
    return ret;
  }

  if( (o>0 && b<=o) || (g>0 && r<=g) || (v>0 && y<=v) ) return FAIL;

  string bb="B",yy="Y",rr="R";
  rep(i,o) bb += "OB";
  rep(i,g) rr += "GR";
  rep(i,v) yy += "VY";
  if(o==0) bb = "";
  else b -= o;
  if(g==0) rr = "";
  else r -= g;
  if(v==0) yy = "";
  else y -= v;

  string bry = sol(b,r,y);
  if(bry[0]=='I') return FAIL;

  string ret;
  for(auto c : bry){
    if(c=='B' && bb.size()>0){
      ret += bb;
      bb = "";
    }
    else if(c=='R' && rr.size()>0){
      ret += rr;
      rr = "";
    }
    else if(c=='Y' && yy.size()>0){
      ret += yy;
      yy = "";
    }
    else ret.pb(c);
  }

  assert(ret.size()==n);

  return ret;
}

int main(){
  int t;
  cin>>t;
  rep(i,t){
    cout << "Case #" << i+1 << ": " << solve() << endl;
  }

  return 0;
}
