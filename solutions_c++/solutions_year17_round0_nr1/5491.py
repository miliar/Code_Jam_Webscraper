#include <bits/stdc++.h>
#define X first
#define Y second
#define MP make_pair
#define INF -1
using namespace std;

inline bool isCorrect(string s) {
  int i;
  for (i = 0; i < s.size(); ++i)
    if (s[i] == '-')
      return false;
  return true;
}

int BFS(string S, int K) {
  int N, i, j;
  pair<int, string> tmp;
  queue<pair<int,string> > Q;

  int x = 0;
  N = S.size();
  Q.push(MP(0, S));

  while (!Q.empty()) {
    tmp = Q.front();
    Q.pop();

    if (isCorrect(tmp.Y)) {
      return tmp.X;
    }

    for (i = tmp.X; i < N - K + 1; ++i) {
      for (j = i; j < i + K; ++j) {
        tmp.Y[j] = tmp.Y[j] == '+' ? '-' : '+';
      }
      Q.push(MP(tmp.X + 1, tmp.Y));
      for (j = i; j < i + K; ++j) {
        tmp.Y[j] = tmp.Y[j] == '+' ? '-' : '+';
      }
    }
  }
  return INF;
}

int main() {
  int T, K, i, ans;
  string S;
  cin >> T;
  for (i = 0; i < T; ++i) {
    cin >> S >> K;
    ans = BFS(S, K);
    cout << "Case #" << (i + 1) << ": ";
    if (ans != INF) {
      cout << ans << "\n";
    } else {
      cout << "IMPOSSIBLE" << "\n";
    }
  }
  return 0;
}