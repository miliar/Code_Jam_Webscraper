#include <iostream>
#include <stdexcept>
#include <string>

using namespace std;

string analyze(const string& N);

int main() {
  int T;
  string N;

  cin >> T;
  for (int i = 1; i <= T; ++i) {
    cin >> N;

    cout << "Case #" << i << ": ";
    cout << analyze(N);
    cout << "\n";
  }

  return 0;
}

string analyze(const string& input) {
  string N = input;
  for (int i = N.length() - 2; i >= 0; --i) {
    if (N[i + 1] - '0' >= N[i] - '0') {
      continue;
    } 

    if (i + 2 < N.length() && (N[i + 2] - '0') <  9) {
      for (int j = i + 2; j < N.length(); ++j) {
        N[j] = '9';
      }
    }
    N[i + 1] = '9';
    --N[i];
  }

  if (N[0] == '0') {
    return N.substr(1);
  }
  return N;
}
