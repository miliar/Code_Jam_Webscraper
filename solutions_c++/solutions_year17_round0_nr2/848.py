#include <iostream>
#include <string>

#include <inttypes.h>

using namespace std;

void solve(string S) {
  uint64_t pos = 1;
  while (pos < S.size()) { if (S[pos - 1] > S[pos]) break; ++pos; }
  for (uint64_t i = 1 + pos; i < S.size(); ++i) S[i] = '9';
  if (pos != S.size()) {
    while (pos--) {
      if (S[pos] > S[pos + 1]) {
        S[pos + 1] = '9';
        --S[pos];
      }
      else break;
    }
  }
  pos = 0; while (pos < S.size()) { if (S[pos] != '0') break; ++pos; }
  while (pos < S.size()) { cout << S[pos]; ++pos; }
}

int main() {
  uint64_t T; cin >> T;
  for (uint64_t i = 1; i <= T; ++i) {
    string S; cin >> S;
    cout << "Case #" << i << ": "; solve(S); cout << endl;
  }
  return 0;
}

