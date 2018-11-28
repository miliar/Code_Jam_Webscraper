#include <iostream>
#include <bitset>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {

    string S;
    int K;
    cin >> S >> K;
    bitset<1000> xs;
    for (int i = 0; i < S.size(); i++) {
      xs[i] = S[i] == '+' ? 1 : 0;
    }

    int i = 0;
    int z = 0;
    for (int i = 0; i < S.size() - K + 1; i++) {
      if (!xs[i]) {
        z += 1;
        for (int k = 0; k < K; k++) {
          xs.flip(i+k);
        }
      }
    }

    bool b = true;
    for (int i = S.size() - K; i < S.size(); i++) {
      if (!xs[i]) {
        b = false;
      }
    }

    cout << "Case #" << (t + 1) << ": " << (b ? to_string(z) : "IMPOSSIBLE") << endl;
  }

  return 0;
}
