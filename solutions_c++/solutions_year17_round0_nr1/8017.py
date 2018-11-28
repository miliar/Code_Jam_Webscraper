#include <iostream>
#include <string>

using namespace std;

void flip(bool* sides, int start, int length) {
  for (int i = 0; i < length; ++i) {
    sides[start + i] = !sides[start + i];
  }
}

void process_case() {
  string S;
  int K;

  cin >> S >> K;
  auto length = S.length();
  auto sides = new bool[length];
  for (int i = 0; i < length; ++i) {
    sides[i] = S[i] == '+';
  }

  int flipCount = 0;
  for (int i = 0; i <= length - K; ++i) {
    if (!sides[i]) {
      ++flipCount;
      flip(sides, i, K);
    }
  }

  bool allHappy = true;
  for (int i = 0; i < length; ++i) {
    if (!sides[i]) {
      allHappy = false;
      break;
    }
  }

  if (allHappy) {
    cout << flipCount;
  } else {
    cout << "IMPOSSIBLE";
  }

  delete[] sides;
}

int main() {
  int T;
  cin >> T;

  for (int n = 0; n < T; ++n) {
    cout << "Case #" << (n + 1) << ": ";
    process_case();
    cout << endl;
  }
}
