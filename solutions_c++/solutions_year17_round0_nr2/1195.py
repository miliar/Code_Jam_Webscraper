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

long solve(){
  long n;
  cin>>n;
  long base=1;
  while(n/base>=10) base*=10L;
//dbg(base);
  auto exe = [&](){
    long bb = base;
    long last = -1;
    long m = n;

    while(bb>0){
      if(m/bb < last){
        n -= m%bb + bb;
        n += bb-1;
        return false;
      }
      last = m/bb;
      m = m%bb;
      bb /= 10;
    }
    return true;
  };

  while(!exe());//dbg(n);

  return n;
}

int main(){
  int t;
  cin>>t;
  rep(i,t){
    long r = solve();
    cout << "Case #" << i+1 << ": ";
    cout << r << endl;
  }

  return 0;
}
