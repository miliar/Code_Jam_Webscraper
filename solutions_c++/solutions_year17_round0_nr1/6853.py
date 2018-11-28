#include <iostream>

using namespace std;

void solve() {
  string sides;
  int K;
  cin >> sides >> K;

  int ans = 0;
  for (int i = 0; i + K - 1 < sides.size(); i++) {
    if (sides[i] == '-') {
      ans++;
      for (int j = 0; j < K; j++) {
	if (sides[i + j] == '+') {
	  sides[i + j] = '-';
	} else {
	  sides[i + j] = '+';
	}
      }
    }
  }

  for (int i = 0; i < sides.size(); i++) {
    if (sides[i] != '+') {
      cout << "IMPOSSIBLE" << endl;
      return;
    }
  }
  cout << ans << endl;
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    cout << "Case #" << i + 1 << ": ";
    solve();
  }
  return 0;
}
