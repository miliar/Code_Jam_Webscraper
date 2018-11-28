#include <bits/stdc++.h>

using namespace std;

int main() {
  int T;

  cin >> T;
  for(int caso = 1; caso <= T; caso++) {
    double Vfin = 10e30, D, x, v;
    int N;
    cin >> D >> N;

    for(int i = 0; i < N; i++) {
      cin >> x >> v;
      Vfin = min(Vfin, (D*v)/(D-x));
    }

    printf("Case #%d: %.7f\n", caso, Vfin);
  }

  return 0;
}
