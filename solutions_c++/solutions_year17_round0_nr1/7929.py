#include <iostream>
#include <stdexcept>
#include <string>

using namespace std;

int analyze(const string& S, const int K);
void flip(string& S, const int start, const int end);

int main() {
  int T, K;
  string S;

  cin >> T;
  for (int i = 1; i <= T; ++i) {
    cin >> S >> K;

    cout << "Case #" << i << ": ";
    try {
      cout << analyze(S, K);
    } catch (const exception& e) {
      cout << "IMPOSSIBLE";
    }

    cout << "\n";
  }

  return 0;
}

int analyze(const string& input, const int K) {
  int count = 0;
  string S = input;
  for (int i = 0; i <= S.length() / 2; ++i) {
    int frontC = i, backC = S.length() - 1 - i;
    if (S[frontC] == '-') {
      if (frontC + K - 1 > backC) {
        throw runtime_error("error");
      }

      flip(S, frontC, frontC + K - 1);
      ++count;
    }

    if (S[backC] == '-') {
      if (backC - K + 1 <= frontC) {
        throw runtime_error("error");
      }

      flip(S, backC - K + 1, backC);
      ++count;
    }
  }

  return count;
}

void flip(string& S, const int start, const int end) {
  for (int i = start; i <= end; ++i) {
    if (S[i] == '-') {
      S[i] = '+';
    } else if (S[i] == '+') {
      S[i] = '-';
    }
  }
}
