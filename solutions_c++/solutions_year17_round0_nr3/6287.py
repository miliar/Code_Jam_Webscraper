#include <iostream>
#include <queue>

using namespace std;

int main() {
  int tc;
  cin >> tc;
  for (int t = 0; t < tc; ++t) {
    int n,k;
    cin >> n >> k;
    priority_queue<int> q;
    q.push(n);
    int a, b;
    for (int i = 0; i < k; ++i) {
      int x = q.top();
      q.pop();
      x--;
      a = x/2;
      b = x - x/2;
      q.push(a);
      q.push(b);
    }
    cout << "Case #" << t + 1 << ": " << max(a,b) << " " << min(a,b) << endl;
  }
}
