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

int solve(){
  int n,p;
  cin>>n>>p;
  vector<int> vec(n);
  rep(i,n) cin>>vec[i];
  vector<int> num(p,0);
  rep(i,n) num[vec[i]%p]++;

  int ans = num[0];
  if(p==2){
    ans += (num[1]+1)/2;
    return ans;

  } else if(p==3){
    int t = min(num[1], num[2]);
    ans += t;
    num[1] -= t;
    num[2] -= t;
    int a = num[1];
    int b = num[2];
    assert(a==0 || b==0);
    int x = a+b;
    ans += (x+2)/3;
    return ans;

  } else if(p==4){
    int t = min(num[1], num[3]);
    ans += t;
    num[1] -= t;
    num[3] -= t;

    int a = num[1];
    int b = num[3];
    assert(a==0 || b==0);
    int x = a + b;

    ans += num[2]/2;
    num[2] %= 2;

    if(num[2]==1 && x>=2){
      ans += 1;
      x -= 2;
      num[2] = 0;
    }

    ans += (x+3)/4;
    if(x==0 && num[2]==1) ans++;

    return ans;
  } else {
    assert(false);
  }
}

int main(){
  int t;
  cin>>t;
  rep(i,t){
    printf("Case #%d: %d\n", i+1, solve());
  }


  return 0;
}
