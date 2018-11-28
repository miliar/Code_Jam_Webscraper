#include <iostream>

using namespace std;

int flipString(int K, string* S) {
  int str_len = S->length();
  int num_flips = 0;
  for (int i = 0; i < str_len; ++i) {
    if ((*S)[i] == '+') continue;
    if ((i + K) > str_len) return -1;
    for (int j = i; j < i + K; ++j) {
      if ((*S)[j] == '-') {
        (*S)[j] = '+';
      } else {
        (*S)[j] = '-';
      }
    }
    num_flips++;
  }
  return num_flips;
}

int main(int argc, char** argv) {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    string S;
    cin >> S;
    int K;
    cin >> K;
    int n_flips = flipString(K, &S);
    if (n_flips == -1) {
      cout << "Case #" << i << ": IMPOSSIBLE" << endl;
    } else {
      cout << "Case #" << i << ": " << n_flips << endl;
    }
  }
  return 1;
}
