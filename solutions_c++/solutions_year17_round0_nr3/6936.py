#include <bits/stdc++.h>
using namespace std;

pair<int, int> solve(int N, int K) {
  priority_queue<int> q;
  q.push(N);
  for (int i = 0; true; ++i) {
    N = q.top();
    q.pop();
    int L = (N-1) / 2;
    int R = (N-1) - L;
    if (i == K-1) {
      return make_pair(R, L);
    }
    q.push(L);
    q.push(R);
  }
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    int N, K;
    cin >> N >> K;
    int y, z;
    tie(y, z) = solve(N, K);
    cout << "Case #" << t << ": " << y << " " << z << "\n";
  }
  return 0;
}
