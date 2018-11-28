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

pair<long,long> solve(){
  long n,k;
  cin>>n>>k;

  map<long,long> m;
  m[n] = 1;

  while(k>0){
    auto itr = m.end();
    itr--;
    long l = itr->first;
    long c = itr->second;
    m.erase(itr);
    k -= c;
    if(k<=0) return mp(l/2, (l-1)/2);
    m[l/2] += c;
    m[(l-1)/2] += c;
  }
  assert(false);
}

int main(){
  int t;
  cin>>t;
  rep(i,t){
    pair<long,long> p = solve();
    cout << "Case #" << i+1 << ": ";
    cout << p.first << " " << p.second << endl;
  }

  return 0;
}
