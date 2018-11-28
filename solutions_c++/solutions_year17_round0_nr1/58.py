#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <cstdio>

using namespace std;

int main() {
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    string S;
    int K;
    cin >> S >> K;

    int result = 0;
    int N = S.size();

    bool fl = false;
    vector<bool> fa(N + 1, false);
    for (int i = 0; i < N; i++) {
      fl ^= fa[i];

      bool hp = (S[i] == '+') ^ fl;
      if (!hp) {
        if (i + K > N) {
          result = N + 1;
          break;
        }
        result++;
        fl = !fl;
        fa[i + K] = true;
      }
    }

    cout << "Case #" << t << ": ";
    if (result > N) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      cout << result << endl;
    }
  }
  return 0;
}
