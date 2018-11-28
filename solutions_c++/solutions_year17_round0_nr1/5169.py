#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <string>

using namespace std;

const int N = 1e3 + 5;
int parity[N];

int main() {
  freopen("in.in", "r", stdin);
  freopen("in.out", "w", stdout);
  ios::sync_with_stdio(false);
  cin.tie(0);

  int T, k;
  string S;
  cin >> T;
  for (int tt = 1; tt <= T; tt++) {
    memset(parity, 0, sizeof parity);
    cin >> S >> k;
    for (int i = 0; i < S.size(); i++) {
      S[i] = S[i] == '+' ? 0 : 1;
    }
    int total = 0;
    for (int i = 0; i <= (int)S.size() - k; i++) {
      int curVal = (S[i] + (int)parity[i]) % 2;
      //cout << curVal << endl;
      if (curVal == 1) {
        ++total;
        for(int j = i + 1; j < i + k; j++) {
          ++parity[j];
        }
      }
    }
    cout << "Case #" << tt << ": ";
    for (int i = (int)S.size() - k + 1; i < S.size(); i++) {
      int curVal = (S[i] + (int)parity[i]) % 2;
      if (curVal == 1) {
        total = -1;
        break;
      }
    }

    if (total == -1) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      cout << total << endl;
    }
  }

  return 0;
}
