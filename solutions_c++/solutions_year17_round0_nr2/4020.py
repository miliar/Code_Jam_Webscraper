#include <string>
#include <iostream>
using namespace std;

bool isTidy(long long N) {
  int last = 9;
  while (N) {
    if (N % 10 <= last) {
      last = N % 10;
      N /= 10;
    } else {
      return false;
    }
  }
  return true;
}

long long brute(string S) {
  long long N = 0;
  for (int i = 0; i < S.length(); ++i) {
    N = N * 10 + (S[i] - '0');
  }
  long long ans = 0;
  for (long long i = 1; i <= N; ++i) {
    if (isTidy(i)) {
      ans = i;
    }
  }
  return ans;
}

int main() {
  int N;
  string S;
  cin >> N;
  for (int c = 1; c <= N; ++c) {
    cin >> S;
    for (int i = 0; i < S.length() - 1; ++i) {
      if (S[i] > S[i + 1]) {
        int k = i;
        int last = i;
        while (k >= 0) {
          if (S[k] == S[i]) {
            last = k;
            k--;
          } else {
            break;
          }
        }
        S[last] = S[last] - 1;
        for (int j = last + 1; j < S.length(); ++j) {
          S[j] = '9';
        }
        break;
      }
    }

    long long ans = 0;
    for (int i = 0; i < S.length(); ++i) {
      ans = ans * 10 + (S[i] - '0');
    }

    cout << "Case #" << c << ": " << ans << "\n";
  }
  return 0;
}
