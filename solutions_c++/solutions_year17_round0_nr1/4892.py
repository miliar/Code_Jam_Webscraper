#include <cstdio>
#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <cstring>
#include <string>
#include <set>
#include <stack>
#define pb push_back

#define mp make_pair
#define f first
#define s second
#define ll long long

using namespace std;


int solve(string S, int K) {
    int moves = 0;
    for (int i = 0; i < S.size(); ++i) {
        if (S[i] == '-' && i + K-1 < S.size()) {
            for (int j = i; j < i + K; ++j) {
                if (S[j] == '-') {
                    S[j] = '+';
                } else {
                    S[j] = '-';
                }
            }
            moves += 1;
        }
    }

    for (int i = 0; i < S.size(); ++i) {
        if (S[i] == '-') {
            return -1;
        }
    }
    return moves;
}
int main() {
  ifstream cin("test.in");
  ofstream cout("test.out");

  int T; cin >> T;
  for (int tc = 1; tc <= T; ++tc) {
      string S; int K;
      cin >> S >> K;
      int ans = solve(S, K);
      cout << "Case #" << tc << ": ";
      if (ans == -1) {
        cout << "IMPOSSIBLE\n";
      } else {
        cout << ans << "\n";
      }
  }
  return 0;
}
