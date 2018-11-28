#include <iostream>

using namespace std;

static const int IMPOSSIBLE = -1;

static void Flip(string& pancakes, int first, int K) {
  for (int i = first; i < (first + K); ++i) {
    char& ch = pancakes[i];
    if (ch == '-') {
      ch = '+';
    } else {
      ch = '-';
    }
  }
}

static bool AllHappy(const string& pancakes) {
  for (auto ch : pancakes) {
    if (ch != '+') {
      return false;
    }
  }
  return true;
}

static int GetMinFlips(string& pancakes, int K) {
  int flips = 0;
  for (int i = 0; i <= (pancakes.length() - K); ++i) {
    char& ch = pancakes[i];
    if (ch == '-') {
      Flip(pancakes, i, K);
      ++flips;
    }
  }
  return AllHappy(pancakes) ? flips : IMPOSSIBLE;
}

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; ++t) {
    string pancakes;
    int K;
    cin >> pancakes >> K;
    int result = GetMinFlips(pancakes, K);
    cout << "Case #" << (t + 1) << ": ";
    if (result == IMPOSSIBLE) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      cout << result << endl;
    }
  }

  return 0;
}
