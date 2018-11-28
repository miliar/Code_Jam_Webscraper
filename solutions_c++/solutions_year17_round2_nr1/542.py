#include <bits/stdc++.h>
using namespace std;
#define REP(i,a,n) for(int i=(a); i<(int)(n); i++)
#define rep(i,n) REP(i,0,n)
#define FOR(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ALLOF(c) (c).begin(), (c).end()
typedef long long ll;
typedef unsigned long long ull;

int D, N;
int K[1005];
int S[1005];


bool C(double s){
  double t = (double)D / s;
  rep(i,N){
    if(K[i]+t*S[i]<D) return false;
  }
  return true;
}

void solve(){

  double lb = 1e-100, ub = 1e300;

  rep(i,10000){
    double m = (lb+ub)/2.0;
    if(C(m)) lb = m;
    else ub = m;
  }
  printf("%.12lf", lb);
}

int main(){
  int T;
  cin >> T;

  rep(t,T){
    cin >> D >> N;
    rep(i,N){
      cin >> K[i] >> S[i];
    }
    
    cout << "Case #" << t+1 << ": ";
    solve();
    cout << endl;
  }
  
  return 0;
}



//ios::sync_with_stdio(false);
