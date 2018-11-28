#include <iostream>
#include <string>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; ++t) {
    cout << "Case #" << (t+1) << ": ";
// cout << endl;
    std::string S;
    int K;
    cin >> S >> K;
// cout << S << endl;
    int count = 0;
    for (int j = 0; j <= S.size() - K; ++j) {
      if (S[j] == '-') {
        for (int i = j; i < j + K; ++i) {
          S[i] ^= 6;
        }
        count++;
// cout << S << endl;
      }
    }
    bool broken = false;
    for (int j = 0; j < S.size(); ++j) {
      if (S[j] == '-') {
        cout << "IMPOSSIBLE" << endl;
        broken = true;
        break;
      }
    }
    if (broken == false) {
      cout << count << endl;
    }
  }
  return 0;
}
