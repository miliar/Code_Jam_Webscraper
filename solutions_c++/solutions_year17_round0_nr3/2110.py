#include <bits/stdc++.h>

using namespace std;


int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int T;
  long long N, K;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    cin >> N >> K;
    if (N == K) {
      cout << "0 0\n";
      continue;
    }
    deque<pair<long long, long long>> dq({{N, 1}});
    while (!dq.empty()) {
      const auto& front = dq.front();
      if (front.first % 2 == 0) {
        if (dq.back().first == front.first / 2) {
          dq.back().second += front.second;
        } else {
          dq.emplace_back(front.first / 2, front.second);
        }
        dq.emplace_back(front.first / 2 - 1, front.second);
      } else {
        if (dq.back().first == front.first / 2) {
          dq.back().second += front.second * 2;
        } else {
          dq.emplace_back(front.first / 2, front.second * 2);
        }
      }
      K -= front.second;
      if (K <= 0) {
        cout << front.first / 2 << ' ' << front.first - front.first / 2 - 1 << '\n';
        break;
      }
      dq.pop_front();
    }
  }
}
