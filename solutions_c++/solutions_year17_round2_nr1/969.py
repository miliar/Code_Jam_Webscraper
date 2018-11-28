#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

#define rep(i, from, to) for(int i = from; i < to; i++)

int main(){
  int T; cin >> T;
  long double D;
  long N;
  vector<long double> K, S;
  rep(t, 1, T+1){
    cin >> D >> N;
    K.assign(N, 0.0); S.assign(N, 0.0);
    rep(i, 0, N) cin >> K[i] >> S[i];
    long double bestTime;
    bestTime = (D-K[0])/S[0];
    rep(i, 1, N) bestTime = max(bestTime, (D-K[i])/S[i]);
    cout << "Case #" << t << ": " << fixed << setprecision(9) << D/bestTime << endl;
  }
}
