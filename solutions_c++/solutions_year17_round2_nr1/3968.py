#include<bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[]) {
  long double D, N, K, S, ti, ans;
  int tc;
  cin >> tc;
  for(int t = 1; t <= tc; ++t) {
    vector<long double> V;
    cin >> D >> N;
    for(int i = 0; i < N; ++i) {
      cin >> K >> S;
      V.push_back((D - K) / S);
    }
    //for(int i = 0; i < N; ++i) cout << V[i] << " "; cout << endl;
    ti = V[0];
    for(int i = 1; i < N; ++i) {
      if(V[i] > ti) {
        ti = V[i];
        break;
      }
    }
    ans = D / ti;
    cout << fixed << setprecision(8) << "Case #" << t << ": " << ans << endl;
  }
  return 0;
}
