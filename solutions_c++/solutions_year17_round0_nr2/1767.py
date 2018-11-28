#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

string solve(string S) {
  if (S.size() == 1) {
    return S;
  }

  int n = S.size();

  int i;
  for (i=1; i<n; i++) {
    if (S[i] < S[i-1]) {
      break;
    }
  }

  if (i == n) {
    return S;
  }

  int j;
  for (j=i-2; j>=0; j--) {
    if (S[j] != S[j+1]) {
      break;
    }
  }

  if (j == -1)  {
    if (S[0] == '1') {
      return string(n-1, '9');
    }
  }

  S[j+1]--;
  for (int k=j+2; k<n; k++) {
    S[k] = '9';
  }

  return S;
}

int main() {
  int T;
  cin >> T;
  for (int i=1; i<=T; i++) {
    string S;
    cin >> S;

    string result = solve(S);

    cout << "Case #" << i << ": " << result << endl;
  }

  return 0;
}
