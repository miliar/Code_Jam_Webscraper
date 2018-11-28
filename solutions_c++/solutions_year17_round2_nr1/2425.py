#include <iostream>
#include <algorithm>
#include <iomanip>

using namespace std;

void solve() {
  cout << setprecision(16) << fixed;

  int D, N;
  cin >> D >> N;

  double max_t = 0;
  for(int i = 0; i < N; ++i) {
    double K, S;
    cin >> K >> S;
    if(K != D) {
      max_t = max(max_t, (D - K) / S);
    }
  }

  cout << D / max_t << endl;
}

int main() {
  int T;
  cin >> T;
  for(int c = 0; c < T; ++c) {
    cout << "Case #" << (c+1) << ": ";
    solve();
  }
  return 0;
}
