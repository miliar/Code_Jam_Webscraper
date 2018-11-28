#include <iostream>

#include <map>
#include <queue>
#include <set>
#include <stack>
#include <unordered_map>
#include <vector>

#include <algorithm>
#include <limits>

#include <cmath>

using namespace std;



int main() {

  int T;
  cin >> T;

  for (int t = 1; t <= T; t++) {
    cout << "Case #" << t << ": ";

    string S;
    int K;
    cin >> S >> K;

    int count = 0;
    for (int i = 0; i < S.length() - K + 1; ++i) {
      if (S[i] == '-') {
	count++;
	for (int j = i; j < i + K; ++j) {
	  if (S[j] == '-') {
	    S[j] = '+';
	  } else {
	    S[j] = '-';
	  }
	}
      }
    }

    bool impossible = false;
    for (int i = 0; i < S.length(); ++i) {
      if (S[i] == '-') {
	impossible = true;
	break;
      }
    }
    if (impossible) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      cout << count << endl;
    }
  }
  
  return 0;
}
