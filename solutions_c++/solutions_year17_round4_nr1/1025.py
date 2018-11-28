#include <bits/stdc++.h>
using namespace std;
#define REP(i,a,n) for(int i=(a); i<(int)(n); i++)
#define rep(i,n) REP(i,0,n)
#define FOR(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ALLOF(c) (c).begin(), (c).end()
typedef long long ll;
typedef unsigned long long ull;

int N, P;
vector<int> g;

void solve(){
  int ret = 0;
  map<int,int> cnt;
  rep(i,g.size()){
    if(g[i] % P == 0) ret++;
    else cnt[g[i]%P]++;
  }

  if(P==2){
    int n = cnt[1];
    if(n%2==0) ret += n/2;
    else ret += n/2 + 1;
  }
  if(P==3){
    int a = cnt[1];
    int b = cnt[2];
    int mn = min(a,b);
    ret += mn;
    a -= mn;
    b -= mn;
    ret += a/3; a %= 3;
    ret += b/3; b %= 3;
    if(a>0) ret++;
    if(b>0) ret++;
  }
  if(P==4){
    int a = cnt[1];
    int b = cnt[2];
    int c = cnt[3];
    int mn = min(a,c);
    ret += mn;
    a -= mn;
    c -= mn;
    while(a>=2 && b>=1){
      a-=2;
      b--;
      ret++;
    }
    while(c>=2 && b>=1){
      c-=2;
      b--;
      ret++;
    }
    ret += b/2; b %= 2;
    ret += a/4; a %= 4;
    ret += c/4; c %= 4;
    if(a>0 || b>0 || c>0) ret++;
  }
  cout << ret << endl;
}

int main(){
  int T;
  cin >> T;

  rep(t,T){
    cin >> N >> P;
    g.clear();
    rep(i,N){
      int a;
      cin >> a;
      g.push_back(a);
    }
    
    cout << "Case #" << t+1 << ": ";
    solve();
  }
  
  return 0;
}



//ios::sync_with_stdio(false);
