#include <bits/stdc++.h>
using namespace std;

const double EPS = 1e-8;

int main() {
  freopen("C-small-1-attempt0.in", "r", stdin);
  freopen("C-small-1-attempt0.out", "w", stdout);
  int cases; cin >> cases;
  for (int cc = 0; cc < cases; ++cc) {
    cout << "Case #" << cc + 1 << ":";

    int N, K; cin >> N >> K;
    long double U; cin >> U;
    map<long double, int> cnt;
    for (int i = 0; i < N; ++i) {
      long double temp; cin >> temp;
      ++cnt[temp];
    }

    while(fabs(U) > EPS) {
      auto firstIt = cnt.begin();
      auto secondIt = cnt.begin(); ++secondIt;
      long double newP;
      int newCnt;
      if (secondIt == cnt.end() || (secondIt->first - firstIt->first) * firstIt->second > U) {
        newP = firstIt->first + U / firstIt->second;
        newCnt = firstIt->second;
        U = 0.0;
      }
      else {
        U -= (secondIt->first - firstIt->first) * firstIt->second;
        newP = secondIt->first;
        newCnt = firstIt->second + secondIt->second;
        cnt.erase(secondIt);
      }
      cnt.erase(firstIt);
      cnt.insert(make_pair(newP, newCnt));
    }

    long double ans = 1.0;
    for (auto it = cnt.begin(); it != cnt.end(); ++it) {
      for (int i = 0; i < it->second; ++i)
        ans *= it->first;
    }

    cout << " " << fixed << setprecision(15) << ans << "\n";
  }
  return 0;
}
