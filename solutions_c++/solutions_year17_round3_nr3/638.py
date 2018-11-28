#include <bits/stdc++.h>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define ALL(x) (x).begin(), (x).end()

typedef long long ll;
typedef long double ld;

const int INF = 1e9;
const ld EPS = 1e-8;

ld solve_small1(int N, ld U, vector<ld>& P) {
  P.push_back(1.0);
  sort(ALL(P));
  REP(i,N) {
    if((P[i + 1] - P[i]) * (i + 1) <= U) {
      U -= (P[i + 1] - P[i]) * (i + 1);
      REP(j,i + 1) P[j] = P[i + 1];
    }else{
      REP(j,i + 1) P[j] += U / (i + 1);
      U = 0;
      break;
    }
  }
  ld res = 1.0;
  REP(i,N) res *= P[i];
  return res;
}

int main(){
  int T;
  cin >> T;
  REP(t,T) {
    int N, K;
    ld U;
    cin >> N >> K >> U;
    vector<ld> P(N);
    REP(i,N) cin >> P[i];

    cout << "Case #" << t + 1 << ": " << fixed << setprecision(10) << solve_small1(N, U, P) << endl;
  }
  return 0;
}

