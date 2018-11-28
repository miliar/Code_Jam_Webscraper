
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int tc=1; tc<=T; tc++) {
    int D, N;
    cin >> D >> N;
    double max_time = 0;
    for (int i=0; i<N; i++) {
      int k, s;
      cin >> k >> s;
      double dist = D - k;
      double time = dist / s;
      max_time = max(time, max_time);
    }
    double speed = D / max_time;
  cout << "Case #" << tc << ": " << fixed << setprecision(8) << speed << endl;
  }
}
