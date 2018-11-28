#include <bits/stdc++.h>
using namespace std;
#define REP(i,a,n) for(int i=(a); i<(int)(n); i++)
#define rep(i,n) REP(i,0,n)
#define FOR(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ALLOF(c) (c).begin(), (c).end()
typedef long long ll;
typedef unsigned long long ull;

int N;
int R, O, Y, G, B, V;

void solve_small(){
  if(R>=Y && R>=B){
    if(Y+B<R){ cout << "IMPOSSIBLE"; return; }
    vector<string> v(R, "");
    for(int i=0; i<Y; i++){ v[i] += "Y"; }
    for(int i=0; i<B; i++){ v[v.size()-1-i] += "B"; }
    rep(i,R){
      cout << "R" << v[i];
    }
  }
  else if(Y>=R && Y>=B){
    if(R+B<Y){ cout << "IMPOSSIBLE"; return; }
    vector<string> v(Y, "");
    for(int i=0; i<R; i++){ v[i] += "R"; }
    for(int i=0; i<B; i++){ v[v.size()-1-i] += "B"; }
    rep(i,Y){
      cout << "Y" << v[i];
    }
  }
  else if(B>=R && B>=Y){
    if(R+Y<B){ cout << "IMPOSSIBLE"; return; }
    vector<string> v(B, "");
    for(int i=0; i<R; i++){ v[i] += "R"; }
    for(int i=0; i<Y; i++){ v[v.size()-1-i] += "Y"; }
    rep(i,B){
      cout << "B" << v[i];
    }
  }
}

int main(){
  int T;
  cin >> T;

  rep(t,T){
    cin >> N >> R >> O >> Y >> G >> B >> V;

    cout << "Case #" << t+1 << ": ";
    solve_small();
    cout << endl;
  }
  
  return 0;
}



//ios::sync_with_stdio(false);
