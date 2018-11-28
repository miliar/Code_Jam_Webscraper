#include <iostream>
#include <limits>

using namespace std;

int
main() {
  int T;

  cin >> T;

  cout.precision(6);
  for(int i = 1; i <= T; i++) {
    int D, N;

    cin >> D >> N;

    double t_max = 0;
    for(int j = 0; j < N; j++) {
      int h, s;
      cin >> h >> s;

      double t = ((double)(D - h))/s;
      if(t > t_max) {
        t_max = t;
      }
    }

    cout << "Case #" << i << ": " << fixed << ((double)D)/t_max << endl;
  }

  return 0;
}

