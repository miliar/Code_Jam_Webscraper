#include <bits/stdc++.h>

using namespace std;

int main() {
  int T;
  stringstream output;
  cin >> T;
  for (int ii = 0; ii < T; ++ii) {
    string S;
    int K, flips = 0;
    cin >> S >> K;
    for (int idx = 0; idx < S.length() + 1 - K; ++idx) {
      if (S[idx] == '-') {
	flips++;
	for (int jj = idx; jj < idx + K; ++jj) {
	  if (S[jj] == '-') {
	    S[jj] = '+';
	  } else {
	    S[jj] = '-';
	  }
	}
      }
    }
    bool success = true;
    for (int idx = S.length() - K; idx < S.length(); idx++) {
      if (S[idx] == '-') {
	success = false;
	break;
      }
    }
    output << "Case #" << ii + 1 << ": ";
    if (success) {
      output << flips << endl;
    } else {
      output << "IMPOSSIBLE" << endl;
    }
  }
  cout << output.str();
  return 0;
}
