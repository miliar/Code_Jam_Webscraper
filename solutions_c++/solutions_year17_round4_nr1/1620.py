#include <iostream>
#include <algorithm>

using namespace std;

int G[101];

int main() {
  int T; cin >> T;

  for(int t = 1; t <= T; t++) {
    int N, P; cin >> N >> P;
    int F[4] = {0, 0, 0, 0};
    for(int i = 1; i <= N; i++) {
      cin >> G[i];
      F[G[i] % P]++;
    }

    int ans = 0;

    if(P == 2) {
      ans += F[0];
      ans += (F[1] + 1)/2;
    }
    else if(P == 3) {
      ans += F[0];
      int v = min(F[1], F[2]);
      ans += v;
      F[1] -= v;
      F[2] -= v;
      ans += (F[1] + 2)/3;
      ans += (F[2] + 2)/3;
    }

    cout << "Case #" << t << ": " << ans << endl;
  }
}
