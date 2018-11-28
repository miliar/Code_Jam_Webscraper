#include <iostream>
#include <string>

using namespace std;

int T = 0;

string solve(string& S) {
  int o_index = 0;
  int index = 1;
  while (index < S.size()) {
    if (S[index] == S[o_index]) {
      index++;
      continue;
    } else if (S[index] > S[o_index]) {
      o_index = index;
      index++;
      continue;
    }

    S[o_index] = S[o_index] - 1;
    for (int i = o_index + 1; i < S.size(); i++) {
      S[i] = '9';
    }
    break;
  }

  if (S.size() > 1 && S[0] == '0') {
    S = S.substr(1);
  }

  return S;
}

int main() {

  string S;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cin >> S;
    cout << "Case #" << i << ": " << solve(S) << endl;
  }

  return 0;
}
