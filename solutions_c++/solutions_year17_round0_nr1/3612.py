#include <iostream>
#include <string>

using namespace std;

string caseN() {
  string S;
  int K;
  cin >> S >> K;
  int r = 0;
  
  for (int i = 0; i <= S.size()-K; ++i) {
    if (S[i] == '+')
      continue;
    
    for (int j = 0; j < K; ++j) {
      if (S[i+j] == '-')
        S[i+j] = '+';
      else
        S[i+j] = '-';
    }
    r++;

  }
  

  for (char c : S)
    if (c == '-')
      return "IMPOSSIBLE";

  return to_string(r);
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #"<<t<<": " << caseN() << endl;
  }
  return 0;
}
