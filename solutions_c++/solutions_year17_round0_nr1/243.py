#define NDEBUG
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;


string solve() {
  string state;
  int K;
  cin >> state >> K;
  int ans = 0;
  for (int i = 0; i + K <= (int)state.size(); ++i) {
    if (state[i] == '-') {
      for (int j = i; j < i + K; ++j) {
        state[j] = state[j] == '-' ? '+' : '-';
      }
      ++ans;
    }
  }
  if (state.find('-') != string::npos) {
    return "IMPOSSIBLE";
  }
  return to_string(ans);
}

int main() {
  ios_base::sync_with_stdio(false);
  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) { // caret here
    cout << "Case #" << tt << ": " << solve() << '\n';
  }
}
