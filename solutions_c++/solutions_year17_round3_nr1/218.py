#include <iostream>
#include <iomanip>
#include <vector>
#include <utility>
#include <algorithm>
#include <cmath>

using namespace std;

#define PI atan(1)*4

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define FORE(i,a,b) for(int i=(a);i<=(b);i++)
#define ALL(A) A.begin(), A.end()
#define SET(A,p) memset(A,p,sizeof(A))

typedef pair<double,double> RH;
#define fi first
#define se second

double dp[1024];

double calc1(double r, double h) {
  return PI * r * h * 2;
}

double calc(double r, double h) {
  return PI * r * r + calc1(r,h);
}

void do_case(int tc) {
  int N, K;
  cin >> N >> K;
  vector<RH> A(N);
  FOR(i,0,N) cin >> A[i].fi >> A[i].se;
  sort(ALL(A));
  SET(dp,0);
  double res = 0;
  FOR(i,0,N) {
    res = max(res, dp[K-1]+calc(A[i].fi,A[i].se));
    for(int k=K-1;k>=0;k--) {
      dp[k+1] = max(dp[k+1], dp[k]+calc1(A[i].fi,A[i].se));
    }
  }

  cout << "Case #" << tc << ": " << fixed << setprecision(9) << res << endl;
}

int main () {
  int T;
  cin >> T;
  FORE(tc,1,T) do_case(tc);
  return 0;
}