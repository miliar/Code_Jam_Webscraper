#include <iostream>
#include <queue>

using namespace std;

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int t;
  cin >> t;
  for (int ti = 0; ti < t; ++ti) {
    int n, k;
    cin >> n >> k;
    priority_queue<int> q;
    q.push(n);
    cout << "Case #" << ti+1 << ": ";
    for (int i = 0; i < k; ++i) {
      int v = q.top(); q.pop();
      v--;
      if (v&1) q.push(v/2), q.push(v/2+1);
      else q.push(v/2), q.push(v/2);
      if (i == k-1) {
        if (v&1) cout << v/2+1 << " " << v/2 << endl;
        else cout << v/2 << " " << v/2 << endl;
      }
    }
  }
}
