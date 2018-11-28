#include <iostream>
#include <queue>

using namespace std;

void solve() {
  int N, K;
  cin >> N >> K;

  priority_queue<int> q;
  q.push(N);

  int y = 0, z = 0;
  for (int i = 0; i < K; i++) {
    int n = q.top();
    q.pop();

    if (n == 1) {
      y = 0;
      z = 0;
    } else {
      y = n / 2;
      z = (n - 1) / 2;
    }
    q.push(y);
    q.push(z);
  }
  cout << y << " " << z << endl;
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    cout << "Case #" << i + 1 << ": ";
    solve();
  }
  return 0;
}
