#include <iostream>
#include <iomanip>
#include <unordered_set>
#include <cstring>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    int D, N;
    cin >> D >> N;
    cout << "Case #" << i+1 << ": ";
    double max_time = 0.0;
    for (int j = 0; j < N; ++j) {
      int K, S;
      cin >> K >> S;
      double t = (double)(D - K) / (double)S;
      if (t > max_time) max_time = t;
    }
    double speed = D / max_time;
    cout << std::fixed << std::setprecision(6) << speed << endl;
  }
  return 0;
}

