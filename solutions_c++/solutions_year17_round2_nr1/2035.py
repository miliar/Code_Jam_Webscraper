#include<iostream>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; ++cas) {
    int D, N;
    cin >> D >> N;
    int K, S;
    cin >> K >> S;
    double max_time = double(D - K)/S;
    for(--N; N > 0; --N) {
      cin >> K >> S;
      max_time = max(max_time, double(D - K)/S);
    }
    cout.setf(ios::fixed);
    cout.precision(6);
    cout << "Case #" << cas << ": " << D/max_time << endl;
  }
}
