#include <bits/stdc++.h>

using namespace std;

using ll = long long;
void solve() {
  int n, k;
  cin >> n >> k;
  multiset<int> a{n};
  for (int i = 0; i < k; ++i) {
    int x = *a.rbegin();
    a.erase(a.find(x));
    a.insert((x - 1) / 2);
    a.insert(x - 1 - (x - 1) / 2);
    if (i == k - 1) {
      cout << x - 1 - (x - 1) / 2 << ' ' << (x - 1) / 2 << endl;
      return;
    }
  } 
}

int main() {
  freopen("input.txt", "r", stdin);
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ": ";
    solve();
  }
}