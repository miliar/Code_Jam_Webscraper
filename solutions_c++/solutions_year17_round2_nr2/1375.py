#include <bits/stdc++.h>
#include <sys/wait.h>
#include <unistd.h>
using namespace std;

#define int long long

int r, o, y, g, b, v;
void readinput() {
  int x;
  cin >> x >> r >> o >> y >> g >> b >> v;
}

void solve() {
  array<pair<pair<int, int>, char>, 3> arr;
  arr[0] = {{r, 0}, 'R'};
  arr[1] = {{y, 0}, 'Y'};
  arr[2] = {{b, 0}, 'B'};

  sort(arr.begin(), arr.end());

  stringstream ss;
  char last = 0;
  int idx = 0;

  for (int i = 0; i < 3; ++i) {
    if (arr[i].first.first > 0) {
      last = arr[i].second;
      arr[i].first.first--;
      idx++;
      arr[i].first.second = -idx;
      ss << last;
      break;
    }
  }

  while (true) {
    sort(arr.rbegin(), arr.rend());
    if (arr[0].first.first == 0) break;
    bool found = false;
    for (int i = 0; i < 3; ++i) {
      if (arr[i].first.first > 0 && arr[i].second != last) {
        last = arr[i].second;
        idx++;
        arr[i].first.second = -idx;
        arr[i].first.first--;
        ss << last;
        found = true;
        break;
      }
    }
    if (!found) {
      cout << "IMPOSSIBLE" << endl;
      return;
    }
  }
  cout << ss.str() << endl;
}







void solveinternal(int case_num) {
  readinput();
  cout << "Case #" << case_num << ": ";
  solve();
}

int32_t main() {
  int n;
  cin >> n;
  for (int i = 1; i <= n; ++i) {
    solveinternal(i);
  }
}
