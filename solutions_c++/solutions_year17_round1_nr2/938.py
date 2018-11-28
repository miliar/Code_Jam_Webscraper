#include <bits/stdc++.h>

using namespace std;

using ll = long long;

struct Event {
  int i, j, k;
  bool start;

  Event (int i, int j, int k, bool start) : i(i), j(j), k(k), start(start) {}

  bool operator<(const Event& other) const {
    if (k < other.k) return true;
    if (k > other.k) return false;
    if (start and not other.start) return true;
    if (other.start and not start) return false;
    if (i < other.i) return true;
    if (i > other.i) return false;
    return j < other.j;
  }
};


int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  
  int T;
  cin >> T;
  for (int tc = 1; tc <= T; tc++) {
    int n, p;
    cin >> n >> p;
    vector<int> r(n);
    for (auto& ri : r) cin >> ri;
    
    vector<Event> events;

    vector<vector<int>> q(n, vector<int>(p));
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < p; j++) {
        cin >> q[i][j];

        int lb_num = q[i][j] * 100;
        int lb_den = 110 * r[i];
        int lb = (lb_num + lb_den - 1) / lb_den;

        int ub_num = q[i][j] * 100;
        int ub_den = 90 * r[i];
        int ub = ub_num / ub_den;

        if (lb > ub) continue;

        events.emplace_back(Event(i, j, lb, true));
        events.emplace_back(Event(i, j, ub, false));
      }
    }

    sort(events.begin(), events.end());

    int ans = 0;
    vector<list<int>> next(n);
    for (auto& event : events) {
      if (event.start) {
        next[event.i].push_back(event.j);

        int ready = 0;
        for (int i = 0; i < n; i++) {
          if (not next[i].empty()) {
            ready++;
          }
        }

        if (ready == n) {
          ans++;

          for (int i = 0; i < n; i++) {
            next[i].pop_front();
          }
        }
      } else {
        for (auto it = next[event.i].begin(); it != next[event.i].end(); ++it) {
          if (*it == event.j) {
            next[event.i].erase(it);
            break;
          }
        }
      }
    }

    cout << "Case #" << tc << ": " << ans << endl;

  }

}
