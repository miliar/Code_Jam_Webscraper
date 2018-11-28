#include <string>
#include <fstream>
#include <iostream>
#include <istream>
#include <sstream>
#include <functional>
#include <numeric>
#include <vector>
#include <algorithm>
#include <math.h>
#include <iomanip>

using namespace std;

int main() {
  int T;
  cin >> T;

  for (int t = 0; t != T; ++t) {
    unsigned long D, N;
    unsigned long K, S;
    cin >> D >> N;
    double maxtime = 0;
    for (int i = 0; i < N; ++i) {
      cin >> K >> S;
      double lala = (D - K) * 1.0 / S;
      if (lala > maxtime) {
        maxtime = lala;
      }
    }

    cout << "Case #" << t + 1 << ": " << setprecision(9) << fixed << (D * 1.0 / maxtime);

    cout << endl;
  }

  return 0;
}