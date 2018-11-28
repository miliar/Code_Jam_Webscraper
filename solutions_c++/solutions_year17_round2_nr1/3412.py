#include <cstdio>
#include <iostream>
#include <iomanip>

using namespace std;

typedef long double ld;

int main() {

  ios::sync_with_stdio(0);

  long long T, D, N, S, K;

  freopen("in.txt", "r", stdin);

  cout << fixed;
  cout << setprecision(6);
  cin >> T;
  for (int t = 1;t<=T;t++) {
    cin >> D >> N;

    ld max_speed = -1;

    for (int i = 0;i<N;i++) {
      cin >> K >> S;
      ld t = (D - K)/(ld)S;

      if(D/t < max_speed || max_speed == -1) {
        max_speed = D/t;
      }
    }
    cout << "Case #" << t << ": " << max_speed << "\n";
  }

  return 0;
}