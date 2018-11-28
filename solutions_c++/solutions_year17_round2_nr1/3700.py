#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>
#include <limits>
using namespace std;
int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
      int D, N;
      cin >> D >> N;
      double T = numeric_limits<double>::max();
      for (int i = 0; i < N; i++) {
        double Ki, Si;
        cin >> Ki >> Si;
        //cout << Ki << Si << endl;
        T = min(D/((D - Ki)/Si), T);
      }
      cout << "Case #" << t << ": " << fixed << T << endl;
  }

}
