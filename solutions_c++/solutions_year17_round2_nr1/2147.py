#include <bits/stdc++.h>

using namespace std;

using LD = long double;
LD K[1005];
LD S[1005];
LD D;
int N;

bool f(LD med) {
  for (int i = 0; i < N; i++) {
//    cout << med << " " << S[i] << endl;
    if (med > S[i]) {
      LD t = K[i]/(med - S[i]);
      LD dist = med*t;
      if (dist < D) return false;
    }
  }
  return true;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    cin >> D >> N;
    for (int i = 0; i < N; i++) cin >> K[i] >> S[i];

    long double low = 0, high = LONG_MAX;
    for (int i = 0; i < 5000; i++) {
      LD med = low + (high-low)/2;
      if (f(med)) {
        low = med;
      } else {
        high = med;
      }
    }

    cout << "Case #" << t << ": " << fixed << setprecision(9) << low << endl;
  }
  return 0;
}
